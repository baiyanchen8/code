chrome.runtime.onInstalled.addListener(() => {
    console.log('🔧 擴充功能已安裝 - 書籤管理系統啟動！');
  
    // 初始化書籤資料（若不存在）
    chrome.storage.local.get('bookmarks', (result) => {
      if (!result.bookmarks) {
        const initialBookmarks = {
          google: [
            { name: "google", url: "https://www.google.com.tw/?gfe_rd=cr&dcr=0&ei=fpi3WuOHIcb48Ae3t7XYDA" },
            { name: "youtube", url: "https://www.youtube.com/?gl=TW&hl=zh-tw" }
          ],
          tool: [
            { name: "mp4 to mp3", url: "https://cdkm.com/tw/mp4-to-mp3" }
          ]
        };
        chrome.storage.local.set({ bookmarks: initialBookmarks }, () => {
          console.log('📂 初始化書籤資料完成！');
        });
      }
    });
  });
  
  // 監聽訊息（來自 content script 的指令）
 // 監聽訊息：新增、刪除 group/mark
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  const { action } = request;

  chrome.storage.local.get('bookmarks', (result) => {
    const bookmarks = result.bookmarks || {};

    if (action === 'addGroup') {
      const { groupName } = request;
      if (bookmarks[groupName]) {
        sendResponse({ success: false, message: `分類 "${groupName}" 已存在！` });
      } else {
        bookmarks[groupName] = [];
        chrome.storage.local.set({ bookmarks }, () => {
          sendResponse({ success: true, message: `分類 "${groupName}" 新增成功！` });
        });
      }
    }

    if (action === 'addBookmark') {
      const { group, name, url } = request;
      if (!bookmarks[group]) {
        sendResponse({ success: false, message: `分類 "${group}" 不存在！` });
        return;
      }
      bookmarks[group].push({ name, url });
      bookmarks[group].sort((a, b) => a.name.localeCompare(b.name));
      chrome.storage.local.set({ bookmarks }, () => {
        sendResponse({ success: true, message: `書籤 "${name}" 新增成功！` });
      });
    }

    if (action === 'removeGroup') {
      const { groupName } = request;
      if (bookmarks[groupName]) {
        delete bookmarks[groupName];
        chrome.storage.local.set({ bookmarks }, () => {
          sendResponse({ success: true, message: `分類 "${groupName}" 已刪除！` });
        });
      } else {
        sendResponse({ success: false, message: `分類 "${groupName}" 不存在！` });
      }
    }

    if (action === 'removeBookmark') {
      const { group, name } = request;
      if (!bookmarks[group]) {
        sendResponse({ success: false, message: `分類 "${group}" 不存在！` });
        return;
      }
      const index = bookmarks[group].findIndex(item => item.name === name);
      if (index !== -1) {
        bookmarks[group].splice(index, 1);
        chrome.storage.local.set({ bookmarks }, () => {
          sendResponse({ success: true, message: `書籤 "${name}" 已刪除！` });
        });
      } else {
        sendResponse({ success: false, message: `書籤 "${name}" 不存在！` });
      }
    }
  });

  return true; // 非同步回應
});
