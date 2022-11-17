import streamlit as st
import os
from converter import *
from delete_file import *
from download_mp import *
from credentials import *
from pdf_to_txt import *
from filesplit import *
from joinmp3 import *
import os
import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ai-learning-text-to-speech-93061333450a.json"

create_apikey()
page = st.sidebar.radio("Select a page",
("Converter",
"settings",
"intro"))

if page == "Converter":
    st.title("VOICY")
    image_file = st.file_uploader("Choose a file",type=['.txt','.pdf'])
    

    if image_file is not None:
        st.text(image_file)
        delete_files()
        delete_audio()
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        if image_file.type == "text/plain":
            st.write(file_details)
            with open(os.path.join("text_files",image_file.name),"wb") as f: 
                f.write(image_file.getbuffer())
                f.close()         
            st.success("Converting {} to speech".format(image_file.name))

            content = {}
            entries = os.listdir('text_files/')
            for entry in entries:
                f = open("text_files/{}".format(entry), "r")
                text = ('''{}'''.format(f.read()))
                content[entry] = text
                f.close()
            for i in range (len(list(content))):
                filename = list(content)[i]
                text = list(content.values())[i]
                #print(text)
                convert_to_speech(text,filename)
            
            entries = os.listdir('converted_audio/')
            for entry in entries:
                audio_file = open('converted_audio/{}'.format(entry), 'rb')
                audio_bytes = audio_file.read()

                st.audio(audio_bytes, format='audio/mp3')
                st.markdown(get_binary_file_downloader_html("converted_audio/{}".format(entry), '{}'.format(entry)), unsafe_allow_html=True)
                audio_file.close()
            os.remove("ai-learning-text-to-speech-93061333450a.json")

        else:
            st.write(file_details)
            with open(os.path.join("text_files",image_file.name),"wb") as f: 
                f.write(image_file.getbuffer())
                f.close()         
            st.success("Converting {} to speech".format(image_file.name))
            convert_pdf_to_text(f"text_files/{image_file.name}")
            os.remove("text_files/{}".format(image_file.name))
            filesplitz()
            content = {}
            entries = os.listdir('text_files/')
            for entry in entries:
                f = open("text_files/{}".format(entry), "r",encoding = 'utf-8')
                text = ('''{}'''.format(f.read()))
                content[entry] = text
                f.close()
            for i in range (len(list(content))):
                filename = list(content)[i]
                text = list(content.values())[i]
                #print(text)
                convert_to_speech(text,filename)

            entries = os.listdir('converted_audio/')
            orginal_files = []
            for entry in entries:
                audiofiles = "converted_audio/{}".format(entry)
                orginal_files.append(audiofiles)
            concatenate_audio_moviepy(orginal_files,"converted_audio/{}.mp3".format(image_file.name))
            for file in orginal_files:
                os.remove("{}".format(file))

            entries = os.listdir('converted_audio/')
            for entry in entries:
                audio_file = open('converted_audio/{}'.format(entry), 'rb')
                audio_bytes = audio_file.read()

                st.audio(audio_bytes, format='audio/mp3')
                st.markdown(get_binary_file_downloader_html("converted_audio/{}".format(entry), '{}'.format(entry)), unsafe_allow_html=True)
                audio_file.close()
            os.remove("ai-learning-text-to-speech-93061333450a.json")
            



if page == "settings":
    with open('settings.json', 'r') as f:
            data = json.load(f)
    voice = st.selectbox('select model',
    ('{}'.format(data['name']), 'en-IN-Wavenet-B','en-US-Wavenet-I'))

    speed = st.selectbox('select speed',
    ('{}'.format(data['speaking_rate']), '0.5', '1.0','1.5','2.0'))


    if st.button('Save settings'):
        with open('settings.json', 'r') as f:
            data = json.load(f)
            data['name'] = voice
            data['speaking_rate'] = float(speed)

        os.remove('settings.json')
        with open('settings.json', 'w') as f:
            json.dump(data, f, indent=4)
if page == "intro":
    audio_file = open('intro.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')