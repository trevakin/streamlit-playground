import streamlit as st

# Page Index
home = st.Page(
    "test-page.py",
    title="Home"
)

titleText='''
# Akin Budgeting Software

Simple Personal Fianance Manager
'''

st.markdown(titleText)
CategoriesTab, BudgetTab, TransactionsTab = st.tabs(["Categories","Budget","Transactions"])



Category_titletxt = "### Categories"
Budget_titletxt = "### Budget"
Transaction_titletxt = "### Transactions"

CategoriesTab.markdown(Category_titletxt)
CategoryListCol, CategTabCol2 = CategoriesTab.columns(2)
CategoryListCol.caption("Category List")
category_list = []

while True:
    category_entry = CategoryListCol.text_input(label="Enter a New Category",label_visibility="hidden", placeholder="New Item", max_chars=80)
    if category_entry:
        category_list.append(category_entry)
        st.empty()
    else: break

BudgetTab.markdown(Budget_titletxt)

TransactionsTab.markdown(Transaction_titletxt)