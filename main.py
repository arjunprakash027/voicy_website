import sys
import os
from converter import convert_to_speech
from delete_file import *

content = {}
entries = os.listdir('text_files/')
for entry in entries:
    f = open("text_files/{}".format(entry), "r")
    text = ('''{}'''.format(f.read()))
    content[entry] = text
print(content)




if __name__ == "__main__":
    if sys.argv[1] == 'convert':
        create_apikey()
        for i in range (len(list(content))):
            filename = list(content)[i]
            text = list(content.values())[i]
            convert_to_speech(text,filename)
        os.remove("ai-learning-text-to-speech-93061333450a.json")
    else:
        print("Not a valid command")
        print("commands supported now are: \n1.convert \n")