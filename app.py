
from gradio_client import Client
import streamlit as st 
import os 

try : 
    client = Client('https://b2a4d91f6ac46a3c3a.gradio.live/')

    def check_prompt(prompt) : 

        '''
        Function to check the prompt

        Args:
        prompt : str : The prompt to be checked

        Returns:
        bool : The boolean value indicating whether the prompt is valid or not
        '''

        try : 
            prompt.replace('' , '')
            return True 
        except : return False

    def check_mesaage() : 
        '''
        Function to check the messages
        '''

        if 'messages' not in st.session_state : st.session_state.messages = []

    check_mesaage()

    for message in st.session_state.messages : 

        with st.chat_message(message['role']) : st.markdown(message['content'])

    prompt = st.chat_input('Ask me anything')

    if check_prompt(prompt) :

        with st.chat_message('user'): st.markdown(prompt)

        st.session_state.messages.append({
            'role' : 'user' , 
            'content' : prompt
        })

        if prompt != None or prompt != '' : 

            with st.spinner('Hold Tight , Getting your answer !!') : response = client.predict(prompt)

            with st.chat_message('assistant') : st.markdown(response)

            st.session_state.messages.append({
                'role' : 'assistant' , 
                'content' : response
            })

except : st.error('Couldnt connect to the backend, please contact the devloper')


# res = client.predict('What is the purpose of including three breaks during each session in the hyperoxic hypoxic protocol')

# print(res)
