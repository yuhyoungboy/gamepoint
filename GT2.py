import streamlit as st

# Tiêu đề ứng dụng
st.title("Game Điểm Số Nhiều Người Chơi")

# Khởi tạo danh sách người chơi và điểm số
if 'players' not in st.session_state:
    st.session_state.players = {}
if 'current_cai' not in st.session_state:
    st.session_state.current_cai = None

# Nhập số lượng người chơi
num_players = st.number_input("Nhập số lượng người chơi:", min_value=1, max_value=10, value=2)

# Nhập tên người chơi
for i in range(num_players):
    player_name = st.text_input(f"Nhập tên người chơi {i+1}:", key=f"player_{i}")

    # Thêm người chơi vào danh sách
    if player_name and player_name not in st.session_state.players:
        st.session_state.players[player_name] = 0

# Chọn người làm Cái
if st.session_state.players:
    st.session_state.current_cai = st.selectbox("Chọn người làm Quản trò:", options=list(st.session_state.players.keys()))

# Các nút để cập nhật điểm số cho từng người chơi
if st.session_state.current_cai:
    selected_player = st.radio("Chọn người chơi để cập nhật kết quả:", options=list(st.session_state.players.keys()))

    # Kết quả của trò chơi
    if st.button("Thua -1"):
        st.session_state.players[selected_player] -= 1
        st.session_state.players[st.session_state.current_cai] += 1
    if st.button("Thắng +1"):
        st.session_state.players[selected_player] += 1
        st.session_state.players[st.session_state.current_cai] -= 1

    if st.button("Ngũ Linh +2"):
        st.session_state.players[selected_player] += 2
        st.session_state.players[st.session_state.current_cai] -= 2

    if st.button("Quản trò Ngũ Linh -2"):
        for player in st.session_state.players:
            if player != selected_player:
                st.session_state.players[player] -= 2
        st.session_state.players[st.session_state.current_cai] += 2 * sum(1 for player in st.session_state.players if player != selected_player)

# Hiển thị điểm số của tất cả người chơi
st.write("Điểm số hiện tại:")
for name, score in st.session_state.players.items():
    st.write(f"{name}: {score}")
