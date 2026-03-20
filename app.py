import time
import random
import streamlit as st

# 設定網頁標題與版面
st.set_page_config(page_title="魔幻點擊冒險", layout="centered")

# Fantasy 風格 CSS
fantasy_css = """
<style>
body {
    background: linear-gradient(135deg, #130f40, #533a71);
    color: #f0e6ff;
}
.stApp {
    border: 2px solid #8e44ad;
    border-radius: 18px;
    padding: 18px;
    background: rgba(10, 8, 22, 0.75);
}
.css-1q8dd3e {
    color: #f5b041 !important;
}
button {
    font-size: 1.15rem;
    font-weight: bold;
}
</style>
"""
st.markdown(fantasy_css, unsafe_allow_html=True)

st.title("🧙‍♂️ 熱血教官的奇幻點擊冒險")

# 遊戲常數
GAME_DURATION = 30  # 秒
MAX_HP = 100

# 初始化遊戲狀態
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.hp = MAX_HP
    st.session_state.score = 0
    st.session_state.scene = "魔法森林"
    st.session_state.weather = "晴天"
    st.session_state.start_time = time.time()
    st.session_state.game_over = False
    st.session_state.coach_message = "準備好衝刺了嗎？熱血教官在這裡為你打氣！🔥"

# 計時器更新
elapsed = int(time.time() - st.session_state.start_time)
remaining = max(0, GAME_DURATION - elapsed)

# 天氣變色與 Emoji 動畫視覺回饋
weather_options = [
    ("晴天", "#4FC3F7", "☀️"),
    ("微風", "#A5D6A7", "🍃"),
    ("雷雨", "#65748B", "⛈️"),
    ("極光", "#9C27B0", "🌌"),
]

if elapsed > 0 and elapsed % 7 == 0:
    st.session_state.weather, bg_color, weather_emoji = random.choice(weather_options)
else:
    for w, color, emoji in weather_options:
        if w == st.session_state.weather:
            bg_color = color
            weather_emoji = emoji
            break

st.markdown(f"<div style='padding: 12px; border-radius: 12px; background-color: {bg_color};'>目前天氣：{st.session_state.weather} {weather_emoji}</div>", unsafe_allow_html=True)

st.markdown(f"### 場景：{st.session_state.scene}")
st.markdown(f"### HP：{st.session_state.hp} / {MAX_HP}  |  分數：{st.session_state.score} |  剩餘時間：{remaining}s")

st.markdown(f"**教官語氣**：{st.session_state.coach_message}")

# 遊戲流程（初始化->互動->狀態更新->渲染）
if not st.session_state.game_over:
    if remaining <= 0 or st.session_state.hp <= 0:
        st.session_state.game_over = True

if st.session_state.game_over:
    st.markdown("## 🏁 遊戲結束！")
    if st.session_state.hp <= 0:
        st.error("你被怪物擊倒了，但教官說：『再來一次，打出更強的自己！💪』")
    else:
        st.success("時間到！來看看你拿到的魔法寶箱吧！🎁")
    st.markdown(f"### 最終分數：{st.session_state.score}")
    if st.button("重新開始"):
        st.session_state.initialized = False
        st.experimental_rerun()
    st.stop()

# 互動按鈕
col1, col2 = st.columns(2)
with col1:
    if st.button("🌟 魔法點擊"):
        st.session_state.score += random.randint(5, 15)
        st.session_state.hp = max(0, st.session_state.hp - random.randint(2, 6))
        st.session_state.coach_message = "幹得好！持續點擊，火力全開！🔥"
        st.experimental_rerun()
with col2:
    if st.button("🍵 治癒補血"):
        heal = random.randint(8, 20)
        st.session_state.hp = min(MAX_HP, st.session_state.hp + heal)
        st.session_state.score = max(0, st.session_state.score - 5)
        st.session_state.coach_message = "補血完成，保持伐竹上陣！⚔️"
        st.experimental_rerun()

# 熱血教官提示，提升 AI 語氣個性
if st.session_state.score > 60:
    st.success("教官激勵：你已經是半神英雄了，繼續維持！💥")
elif st.session_state.score > 30:
    st.info("教官鼓舞：太棒了，立即養成連按習慣！💪")
else:
    st.warning("教官挑戰：不要害怕失敗，下一次點擊就是爆發！🔥")

# 進度條視覺化
progress = min(1.0, st.session_state.score / 150)
st.progress(progress)

# 顯示英雄狀態小動畫 (透過 Emoji 變化)
emoji_state = "🧙‍♂️" if st.session_state.hp > 40 else "⚔️" if st.session_state.hp > 15 else "💀"
st.markdown(f"### 英雄狀態：{emoji_state} {st.session_state.hp}HP")

st.info("💡 請使用按鈕互動並觀察倒數計時，遊戲會在時間/HP歸零後結束。")
