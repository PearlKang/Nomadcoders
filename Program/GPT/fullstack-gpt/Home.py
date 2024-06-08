import streamlit as st
from langchain.prompts import PromptTemplate

st.write("hello")

st.write([1, 2, 3, 4])

st.write({"x": 1})

st.write(PromptTemplate)

p = PromptTemplate.from_template("xxxx")

st.write(p)
