import streamlit as st
import sys
sys.path.append('Users/takin/Documents/Code/streamlit-playground')
from storage.utils import add_category, get_all_categories

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
categories = get_all_categories()


@st.fragment
def displayCategories():
    for category in categories:
        CategoryListCol.write(category)
     

category_entry = CategoryListCol.text_input(label="Enter a New Category",
                                            label_visibility="hidden",
                                            placeholder="New Item",
                                            max_chars=80)
if category_entry:
    add_category(category_entry)
    st.success(f"Added '{category_entry}'!")
    displayCategories()

BudgetTab.markdown(Budget_titletxt)

TransactionsTab.markdown(Transaction_titletxt)