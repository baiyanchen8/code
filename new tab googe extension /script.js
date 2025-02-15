document.getElementById('terminal-input').addEventListener('keydown', async function (e) {
    if (e.key === 'Enter') {
      const query = this.value.trim();
      this.value = '';
  
      if (!query) return;
  
      if (query.toLowerCase() === 'add group') {
        const groupName = prompt('請輸入新分類名稱：');
        if (groupName) {
          chrome.runtime.sendMessage({ action: 'addGroup', groupName }, (response) => {
            alert(response.message);
            if (response.success) loadBookmarks();
          });
        }
      } 
      else if (query.toLowerCase() === 'add mark') {
        const group = prompt('請輸入分類名稱：');
        const name = prompt('請輸入書籤名稱：');
        const url = prompt('請輸入書籤 URL：');
        if (group && name && url) {
          chrome.runtime.sendMessage({ action: 'addBookmark', group, name, url }, (response) => {
            alert(response.message);
            if (response.success) loadBookmarks();
          });
        }
      }
      else if (query.toLowerCase() === 'remove group') {
        const groupName = prompt('請輸入要刪除的分類名稱：');
        if (groupName) {
          chrome.runtime.sendMessage({ action: 'removeGroup', groupName }, (response) => {
            alert(response.message);
            if (response.success) loadBookmarks();
          });
        }
      }
      else if (query.toLowerCase() === 'remove mark') {
        const group = prompt('請輸入分類名稱：');
        const name = prompt('請輸入要刪除的書籤名稱：');
        if (group && name) {
          chrome.runtime.sendMessage({ action: 'removeBookmark', group, name }, (response) => {
            alert(response.message);
            if (response.success) loadBookmarks();
          });
        }
      }
      else {
        chrome.search.query({ text: query }, () => {
          console.log('🔍 執行 Google 搜尋：', query);
        });
      }
    }
  });
  
  // 動態載入書籤
  function loadBookmarks() {
    chrome.storage.local.get('bookmarks', (result) => {
      const nav = document.getElementById('bookmark');
      nav.innerHTML = '';
      const bookmarks = result.bookmarks || {};
  
      // 按 group 名稱排序
      const sortedGroups = Object.keys(bookmarks).sort();
      sortedGroups.forEach(category => {
        const ul = document.createElement('ul');
        const titleLi = document.createElement('li');
        titleLi.textContent = category;
        ul.appendChild(titleLi);
  
        // 書籤排序
        const sortedLinks = bookmarks[category].sort((a, b) => a.name.localeCompare(b.name));
        sortedLinks.forEach(link => {
          const li = document.createElement('li');
          const a = document.createElement('a');
          a.href = link.url;
          a.textContent = link.name;
          a.target = '_blank';
          li.appendChild(a);
          ul.appendChild(li);
        });
  
        nav.appendChild(ul);
      });
    });
  }
  
  // 初始化書籤
  loadBookmarks();
  