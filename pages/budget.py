import streamlit as st

st.page_link("test-page.py",icon="◀️",label="")

titleText='''
# Budget


Get started writing your categories
'''
st.markdown(titleText)
st.divider()
st.text_input("*Enter a category*")