import os
def filesplitz():
    entries = os.listdir('text_files/')
    orginal_files = []
    for entry in entries:
        orginal_files.append(entry)
        with open('text_files/{}'.format(entry),encoding = 'utf-8') as infp:
            files = [open('text_files/{}{}.txt'.format(entry[:-3],i), 'w' , encoding = 'utf-8') for i in range(3)]
            for i, line in enumerate(infp):
                #print(line)
                files[i % 3].write(line)
            for f in files:
                f.close()
    print(orginal_files)
    for file in orginal_files:
        os.remove("text_files/{}".format(file))

if __name__ == '__main__':
    filesplitz()