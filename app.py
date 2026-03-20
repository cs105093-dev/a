import time
import random
import streamlit as st

# 頁面設定
st.set_page_config(page_title="賽博酸點擊：城市滅口", layout="wide")

# Cyberpunk 主題 CSS
cyberpunk_css = """
<style>
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: #e9ff6d;
}
.stApp {
    border: 1px solid #00e5ff;
    border-radius: 16px;
    background: rgba(10, 10, 25, 0.82);
}
.css-1q8dd3e, h1, h2, h3, h4 {
    text-shadow: 0 0 15px #00f0ff;
}
button {
    font-size: 1.1rem;
    font-weight: 700;
    color: #ffff8f;
    background-color: #0e0b23;
    border: 2px solid #00ff9d;
    box-shadow: 0 0 18px #00ff9d;
}
button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 28px #00ff9d;
}
</style>
"""
st.markdown(cyberpunk_css, unsafe_allow_html=True)

st.title("🧾 賽博酸點擊：城市滅口")

# 常數
MAX_HP = 120
LOOT_TABLE = ["⛓ 電流手套", "🧠 智能記憶芯片", "⚡ 震盪手雷", "🛡 冰霜護甲", "🔥 能量核心"]

# 初始化狀態
if 'initialized' not in st.session_state or not st.session_state.get('initialized', False):
    st.session_state.initialized = True
    st.session_state.hp = MAX_HP
    st.session_state.score = 0
    st.session_state.scene = "夜市廢墟"
    st.session_state.weather = "霓虹暴雨"
    st.session_state.loot = []
    st.session_state.start_time = time.time()
    st.session_state.is_game_over = False
    st.session_state.voice_line = 0
    st.session_state.action_count = 0
    st.session_state.toxic_message = "你這個垃圾貨，連機器人都看不下去。"

# 遊戲循環
if not st.session_state.is_game_over:
    st.session_state.action_count += 0  # 保持現有狀態

elapsed = int(time.time() - st.session_state.start_time)

# 天氣變色與場景互動
weather_effects = {
    "霓虹暴雨": ("#081a32", "🌧"),
    "電光風暴": ("#1a0730", "⚡"),
    "螢光雪原": ("#0d0c25", "❄️"),
}
if elapsed % 8 == 0:
    st.session_state.weather = random.choice(list(weather_effects.keys()))

bg_color, weather_emoji = weather_effects.get(st.session_state.weather, ("#081a32", "🌧"))
st.markdown(f"<div style='padding:12px;border-radius:10px;background:{bg_color};color:#fff;'>天氣：{st.session_state.weather} {weather_emoji}</div>", unsafe_allow_html=True)

st.markdown(f"### 場景：{st.session_state.scene}")
st.markdown(f"### HP：{st.session_state.hp} / {MAX_HP}  |  分數：{st.session_state.score}  | 已經運行：{elapsed}s")
st.markdown(f"**毒舌酸民**：{st.session_state.toxic_message}")

# 判斷 HP 歸零結束
if st.session_state.hp <= 0:
    st.session_state.is_game_over = True

if st.session_state.is_game_over:
    st.markdown("## 💀 遊戲結束：HP 透支")
    st.error("你被賽博廢土吞噬了。別以為下次會比較好。")
    st.markdown(f"### 最終分數：{st.session_state.score}")
    if st.button("重新開始"):
        st.session_state.initialized = False
        st.session_state.is_game_over = False
        st.session_state.hp = MAX_HP
        st.session_state.score = 0
        st.session_state.scene = "夜市廢墟"
        st.session_state.weather = "霓虹暴雨"
        st.session_state.loot = []
        st.session_state.start_time = time.time()
        st.session_state.voice_line = 0
        st.session_state.action_count = 0
        st.session_state.toxic_message = "你這個垃圾貨，連機器人都看不下去。"
        st.experimental_rerun()
    st.stop()

# 互動按鈕
col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("🖕 毒舌點擊"):
        damage = random.randint(8, 18)
        st.session_state.score += random.randint(10, 25)
        st.session_state.hp = max(0, st.session_state.hp - damage)
        st.session_state.toxic_message = random.choice([
            "你這操作，吐了。",
            "連分數都不配叫成就。",
            "你到底在按什麼？",
            "好歹給我看點血。"
        ])
        st.session_state.action_count += 1
with col2:
    if st.button("🛠 緊急補血"):
        heal = random.randint(12, 24)
        st.session_state.hp = min(MAX_HP, st.session_state.hp + heal)
        st.session_state.score = max(0, st.session_state.score - 8)
        st.session_state.toxic_message = random.choice([
            "終於有點用。",
            "這點補血就想贏？",
            "好吧，就勉強給你。"
        ])
        st.session_state.action_count += 1
with col3:
    can_open_loot = len(st.session_state.loot) > 0
    if st.button("🎁 砸開寶箱") and can_open_loot:
        item = st.session_state.loot.pop(0)
        st.session_state.score += random.randint(15, 35)
        st.session_state.hp = min(MAX_HP, st.session_state.hp + random.randint(6, 14))
        st.balloons()
        st.success(f"獲得：{item}！HP + 衝分！")
    if not can_open_loot:
        st.write("無寶箱可開")


# 隨機寶箱觸發
if st.session_state.action_count > 0 and st.session_state.action_count % 4 == 0:
    new_loot = random.choice(LOOT_TABLE)
    if len(st.session_state.loot) < 3:
        st.session_state.loot.append(new_loot)
st.markdown(f"### 氣袋寶箱：{len(st.session_state.loot)} 個 | 內容：{', '.join(st.session_state.loot) if st.session_state.loot else '暫無'}")

# 場景變化基於分數
if st.session_state.score > 200:
    st.session_state.scene = "高塔資料核心"
elif st.session_state.score > 120:
    st.session_state.scene = "地下黑網"
else:
    st.session_state.scene = "夜市廢墟"

# 進度條與血量動畫回饋
progress = min(1.0, st.session_state.score / 240)
st.progress(progress)

if st.session_state.hp > 80:
    emoji_state = "😎"
elif st.session_state.hp > 40:
    emoji_state = "🥴"
else:
    emoji_state = "☠️"
st.markdown(f"### 狀態：{emoji_state} HP {st.session_state.hp}")

if st.session_state.hp <= 30:
    st.warning("你的系統將斷電，快補血！")

st.info("💡 毒舌酸民會在你操作後嘲諷你，寶箱可加成，HP 歸零遊戲結束。")
