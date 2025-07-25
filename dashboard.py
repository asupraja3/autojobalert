
from email_utils import *
from fetch_jobs import *
from preprocess import *
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Automatic Job Alert", layout="wide", page_icon=":mailbox_with_mail:")

st.title("Automatic Job Alert")

st.markdown("Automated remote job scraping & email alerts using Remotive API.")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

keywords = st.text_input("Enter the keywords to find jobs","AI,ML").split(",")



