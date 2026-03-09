import streamlit as st

if 'data_store' not in st.session_state:
    st.session_state.data_store = []

st.title("Мениджър на книжен фонд")

st.header("Регистрация на нов запис")

input_name = st.text_input("Заглавие на изданието")
input_user = st.text_input("Име на автора")
input_sum = st.number_input("Цена в лева", min_value=0.0, step=0.1)

if st.button("Запази данните"):
    if input_name.strip() and input_user.strip():
        record = {
            "name": input_name.strip(),
            "author": input_user.strip(),
            "value": round(input_sum, 2)
        }
        st.session_state.data_store.append(record)
        st.success("Информацията е отразена в системата.")
    else:
        st.error("Попълнете име и автор.")

if st.button("Преглед на всички записи"):
    if not st.session_state.data_store:
        st.info("Списъкът е празен.")
    else:
        st.subheader("Наличен списък")
        for item in st.session_state.data_store:
            st.text(f"Заглавие: {item['name']}")
            st.text(f"Автор: {item['author']}")
            st.text(f"Цена: {item['value']:.2f}")
            st.divider()

st.header("Справка по автор")

find_text = st.text_input("Търсено име")

if st.button("Изпълни справка"):
    if not find_text.strip():
        st.warning("Въведете име за проверка.")
    else:
        results = False
        keyword = find_text.lower().strip()

        for item in st.session_state.data_store:
            if keyword in item["author"].lower():
                st.write(f"Намерено: {item['name']} - {item['author']}")
                results = True

        if not results:
            st.info("Няма данни за този автор.")


