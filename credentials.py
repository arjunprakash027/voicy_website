
import json
import streamlit as st

def create_apikey(): 
    private_key_id = st.secrets["private_key_id"]
    private_key = st.secrets["private_key"]
    client_id = st.secrets["client_id"]
    dictionary = {
    "type": "service_account",
    "project_id": "ai-learning-text-to-speech",
    "private_key_id": private_key_id,
    "private_key": private_key,
    "client_email": "my-tts-sa@ai-learning-text-to-speech.iam.gserviceaccount.com",
    "client_id": client_id,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/my-tts-sa%40ai-learning-text-to-speech.iam.gserviceaccount.com"
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("ai-learning-text-to-speech-93061333450a.json", "w") as outfile:
        outfile.write(json_object)