// 包含 ESP32 的相關庫
#include <Arduino.h>

// 定義 LED 的腳位
#define LED_PIN 2

void setup() {
  // 將 LED_PIN 設定為輸出
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 將 LED_PIN 設定為高電位（亮燈）
  digitalWrite(LED_PIN, HIGH);
  // 延遲一段時間（例如500毫秒）
  delay(500);
  // 將 LED_PIN 設定為低電位（熄滅）
  digitalWrite(LED_PIN, LOW);
  // 再次延遲一段時間
  delay(500);
}
