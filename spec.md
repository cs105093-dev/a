## spec.md - 奇幻冒險 Clicker 遊戲（Streamlit）

### 1. 專案概述
- 遊戲名稱：`魔幻熱血點擊大作戰`
- 風格：奇幻冒險（Fantasy）
- 玩法：瘋狂點擊（Clicker）
- 個性：熱血教官（Enthusiastic）
- 輸贏判定：計時器結束（Timer）
- 驚喜元素：背景天氣變色（Weather）

---

## 2. 技術需求（必須）

### 2.1 框架
- 使用 `Streamlit`。
- 入口：`app.py`。

### 2.2 狀態管理
- 全部遊戲狀態都應該放在 `st.session_state`：
  - `hp`（生命值）
  - `score`（分數）
  - `scene`（場景名稱）
  - `weather`（天氣狀態）
  - `start_time`（遊戲啟動時間）
  - `is_game_over`（遊戲結束旗標）
  - `coach_prompt`（教官語氣提示）

---

## 3. 主題 & CSS

### 3.1 奇幻冒險主題
- 運用魔法、森林、星空、紫色/靛藍色調。
- 標題與按鈕需具備奇幻風設計感。

### 3.2 CSS 實作
- 加入自訂 CSS：
  - 背景漸層：`linear-gradient(...)`
  - 文字色：`#f0e6ff` / `#f5b041`
  - 按鈕風格：放大、粗體、發光、圓角
  - 狀態框（HP / 天氣）動態框顏色

---

## 4. 個性：熱血教官 AI 提示詞氣
- 準備 3~5 種熱血提示詞：
  - 低分：激勵「別停，最後一刻爆發！🔥」
  - 中分：鼓勵「太猛了！再衝一波！💪」
  - 高分：極勵「你是傳說！繼續破表！⚡」
- 每次按鈕互動後根據 `score` 更新 `coach_prompt`。
- 遊戲結束提示句：
  - 「時間到！好樣的！」 or 「你的 HP 歸零了，重整旗鼓！」

---

## 5. 遊戲循環（完整流程）

1. 初始化
   - 判斷 `if 'initialized' not in st.session_state`
   - 設定初始值：`hp=100`, `score=0`, `scene='魔法森林'`, `weather='晴天'`, `start_time=time.time()`, `is_game_over=False`, `coach_prompt=...`

2. 互動（按鈕）
   - `st.button("🔮 魔法點擊")`
     - `score += rand(5,15)`
     - `hp -= rand(2,6)`
   - `st.button("🍵 能量補給")`
     - `hp += rand(8,20)`, 上限 `100`
     - `score -= 5`（或小懲罰）

3. 狀態更新
   - 計時 `elapsed = int(time.time() - start_time)`
   - 剩餘：`remaining = max(0, TIMER - elapsed)`
   - 時間歸零或 `hp <= 0` -> `is_game_over=True`
   - 天氣變色機制：
     - 每隔 5~10 秒循環變換
     - `weather` 從 `晴天、微風、雷雨、極光` 中隨機/循環
     - `bg_color` 隨之變換

4. 渲染
   - 進度條：`st.progress(score / 150)`
   - 狀態顯示：
     - `st.markdown("### 場景")`
     - `st.markdown("### HP/分數/剩餘時間")`
     - `st.markdown("### 教官語氣")`
   - 視覺回饋：
     - 天氣色彩區塊（`<div style="background-color: ...">...`)
     - Emoji 動畫：`☀️`, `🍃`, `⛈️`, `🌌` + 停滯/準備
   - 遊戲結束畫面：`st.markdown("🏁 遊戲結束")` + 最終結果 +「重新開始」按鈕

---

## 6. 視覺回饋（強制項目）

- 背景變色與天氣切換提示，至少一處使用 `st.markdown(html, unsafe_allow_html=True)`。
- Emoji 動態：
  - HP > 50：`🧙‍♂️`
  - 20 < HP <= 50：`⚔️`
  - HP <= 20：`💀`
- 進度條 + 狀態閃爍提示。

---

## 7. 交付內容

- `spec.md`（本文件）
- `app.py`（可直接執行）
- README 附註：
  - 執行命令：`streamlit run app.py`
  - 遊戲機制簡介（點擊/補血/倒數）
  - 可能的擴充建議（聯網排行榜、音效、怪物隨機事件）