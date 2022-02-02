import streamlit as st
import time



#Constants
final_page = 8
final_attempt = 5
sleep_time_after_trial = 3
time_while_showing_number = 1
time_until_next_number = 0.5



def save(service):
    range_ = "data!A1:F1"
    value_input_option = "RAW"
    insert_data_option = "INSERT_ROWS"
    spreadsheet_id = "1dH_LJ24e-yLGhZywKnQnSfYKE75Ad7DHu4sCfZGJL6g"

    data = [[
        st.session_state.id, 
        st.session_state.result[0], 
        st.session_state.result[1], 
        st.session_state.result[2], 
        st.session_state.result[3], 
        st.session_state.result[4]
    ]]

    request = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, 
        range=range_, 
        valueInputOption=value_input_option, 
        insertDataOption=insert_data_option, 
        body={"values":data}
    )

    request.execute()

def start_page(start_btn_callback):
    
    with open('start_page_text.html', 'r') as file:
        body = file.read().replace('\n', '')

    st.markdown(body, unsafe_allow_html = True)
    
    col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
    with col3:
        st.button("START", key = "start_btn", on_click = start_btn_callback)
        
        


def end_page():

    with open('end_page_text.html', 'r') as file:
        body = file.read().replace('\n', '')

    st.markdown(
            body.format(
                id = st.session_state.id, 
                score_one = st.session_state.result[0], 
                score_two = st.session_state.result[1], 
                score_three = st.session_state.result[2], 
                score_four = st.session_state.result[3], 
                score_five = st.session_state.result[4]
            ),
            unsafe_allow_html = True
        )


def next_btn_callback(service):
    #correct answer case:
    if st.session_state.user_answer == st.session_state.correct_answer:
        #last trial of last attempt
        if st.session_state.attempt == final_attempt and st.session_state.page == final_page:
            st.session_state.page = -1
            st.session_state.attempt_score += 1
            st.session_state.result.append(st.session_state.attempt_score)
            save(service)
        #last trial of the current attempt
        elif st.session_state.page == final_page:
            st.session_state.page = 1
            st.session_state.attempt += 1
            st.session_state.attempt_score += 1
            st.session_state.result.append(st.session_state.attempt_score)
            st.session_state.attempt_score = 0
        #non-final trial 
        else:
            st.session_state.page += 1
            st.session_state.attempt_score += 1
    else:
        #non-final attempt
        if st.session_state.attempt != final_attempt:
            st.session_state.page = 1
            st.session_state.attempt += 1
            st.session_state.result.append(st.session_state.attempt_score)
            st.session_state.attempt_score = 0
        #final attempt
        else:
            st.session_state.page = -1
            st.session_state.result.append(st.session_state.attempt_score)
            save(service)


def exp_page(
    amount_of_digits,
    generate_correct_answer,
    service
    ):

    with open('exp_page_text.html', 'r') as file:
        body = file.read().replace('\n', '')
    
    st.markdown(
        body.format(
            current_attempt = st.session_state.attempt, 
            current_trial = amount_of_digits - 2,
            max_attempts = final_attempt,
            max_trials = final_page
        ),
        unsafe_allow_html = True
    )

    #this function is seperate as it should not be rerun if nothing changes.
    random_numbers = generate_correct_answer(amount_of_digits, st.session_state.attempt)

    with st.empty():
        for i in range(0, amount_of_digits):
            body = "<p style=\"text-align: center; font-size:600%\">{}</p>".format(random_numbers[i])
            time.sleep(time_until_next_number)
            st.markdown(body, unsafe_allow_html = True)
            time.sleep(time_while_showing_number)
            st.empty()
        st.empty()
        time.sleep(sleep_time_after_trial)
    
    # with st.form("my_form"):
    #     st.text_input("Enter:", max_chars = amount_of_digits, value = "", key = "user_answer")
    #     st.form_submit_button("NEXT", on_click = next_btn_callback, args = (service,))
    with st.contaier():
        st.text_input("Enter:", max_chars = amount_of_digits, value = "", key = "user_answer")
        st.button("NEXT", on_click = next_btn_callback, args = (service,))
    
    
    