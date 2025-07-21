import streamlit as st

pages = {
    "Tools": [
        st.Page("pages/MainPage.py", title="Homepage", icon="🏡"),
        st.Page("pages/AdvancesPage.py", title="Advanced", icon="🚀"),
    ],
    "Resources": [
        st.Page("pages/HelpsPage.py", title="Help & Documentation", icon="📚"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()
