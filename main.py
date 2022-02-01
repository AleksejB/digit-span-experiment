import streamlit as st
import time
import random
from googleapiclient import discovery
from google.oauth2 import service_account
from pages import *
import uuid



#Functions
def start_btn_callback():
    st.session_state.page = 1


def make_gsheet_service():
    keys = [
        "type", 
        "project_id", 
        "private_key_id", 
        "private_key", 
        "client_email", 
        "client_id", 
        "auth_uri", 
        "token_uri", 
        "auth_provider_x509_cert_url", 
        "client_x509_cert_url"
    ]
    values = [
        st.secrets.type, 
        st.secrets.project_id, 
        st.secrets.private_key_id, 
        st.secrets.private_key, 
        st.secrets.client_email, 
        st.secrets.client_id, 
        st.secrets.auth_uri, 
        st.secrets.token_uri, 
        st.secrets.auth_provider_x509_cert_url, 
        st.secrets.client_x509_cert_url
    ]
    
    creds_dict = dict(zip(keys, values))

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_INFO = creds_dict

    creds = None
    creds = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_INFO, scopes=SCOPES)    

    service = discovery.build('sheets', 'v4', credentials = creds)
    return service


@st.cache(max_entries = 1)
def generate_correct_answer(amount_of_digits, attempt):
    #attempt isnt used, it is just needed so that streamlit knows to recalculate the numbers 
    #if the attempt has changed. (see @st.cache docs)
    random_numbers = []
    for i in range(0, amount_of_digits):
        rand_number = random.randrange(0, 10)
        random_numbers.append(rand_number)

    correct_answer = ""
    for i in random_numbers:
        correct_answer += str(i)
    
    st.session_state.correct_answer = correct_answer
    return random_numbers

def generate_correct_answer_str():
    random_numbers = generate_correct_answer(3, 1)
    answer = ""
    for i in random_numbers:
        answer += str(i)
    return answer



#Start
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'attempt' not in st.session_state:
    st.session_state.attempt = 1
if 'correct_answer' not in st.session_state:
    st.session_state.correct_answer = generate_correct_answer_str()
if 'result' not in st.session_state:
    st.session_state.result = []
if 'attempt_score' not in st.session_state:
    st.session_state.attempt_score = 0
if 'id' not in st.session_state:
    st.session_state.id = str(uuid.uuid4())

service = make_gsheet_service()
page = st.session_state.page

if page == 0:
    start_page(
        start_btn_callback
    )
elif page == -1:
    end_page()
else:
    exp_page(
        page + 2,
        generate_correct_answer,
        service
    )