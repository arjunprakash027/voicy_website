import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1
import json
import logging
logging.basicConfig(filename="debug.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ai-learning-text-to-speech-93061333450a.json"


def convert_to_speech(text,filename):
    with open('settings.json', 'r') as openfile:
        setting_file = json.load(openfile)
        print(setting_file)
    #print(setting_file)
    client = texttospeech_v1.TextToSpeechClient()

    synthesis_input = texttospeech_v1.SynthesisInput(ssml = text)

    voice1 = texttospeech_v1.VoiceSelectionParams(
        language_code = 'en-us',
        ssml_gender = texttospeech_v1.SsmlVoiceGender.FEMALE
    )
    voice2 = texttospeech_v1.VoiceSelectionParams(
        name = setting_file['name'],
        language_code = 'en-US',
        ssml_gender = texttospeech_v1.SsmlVoiceGender.FEMALE
    )

    logger.info("converting {} on process".format(filename))
    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding = texttospeech_v1.AudioEncoding.MP3,
        speaking_rate = setting_file['speaking_rate']
    )

    response1 = client.synthesize_speech(
        input = synthesis_input,
        voice = voice2,
        audio_config = audio_config
    )

    with open('converted_audio/{}.mp3'.format("".join(filename[:-4].split())),'wb',) as output:
        output.write(response1.audio_content)

if __name__ ==  '__main__':
    content = {}
    entries = os.listdir('text_files/')
    for entry in entries:
        print(entry)
        f = open("text_files/{}".format(entry), "r",encoding='utf-8')
        text = ('''{}'''.format(f.read()))
        content[entry] = text
    for i in range (len(list(content))):
        filename = list(content)[i]
        text = list(content.values())[i]
        #print(text)
        convert_to_speech(text,filename)
    
