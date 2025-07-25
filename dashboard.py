
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

if st.button("Fetch Jobs"):
    with st.spinner("Fetching jobs..."):
        jobs = fetch_jobs()
        st.session_state.df = filter_data(jobs, keywords)
        st.success("Jobs fetched and filtered successfully!")
        if st.session_state.df.empty:
            st.warning("No jobs found with the given keywords.")
        else:
            st.success("Found {} jobs.".format(len(st.session_state.df)))
            st.dataframe(st.session_state.df)

if st.button("Send Email"):
    if not st.session_state.df.empty:
        st.session_state.df.to_csv("filtered_jobs.csv", index=False)
        send_email(len(st.session_state.df))
        st.success("Email sent successfully!")
    else:
        st.error("No jobs to email. Please fetch first.")




