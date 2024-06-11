import streamlit as st

# st.sidebar.title("sidebar title")
# st.sidebar.text_input("xxx")

with st.sidebar:
    st.title("sidebar title")
    st.text_input("xxx")

st.title("title")

tab_one, tab_two, tab_three = st.tabs(["A", "B", "C"])

with tab_one:
    st.write("a")

with tab_two:
    st.write("b")

with tab_three:
    st.write("c")
