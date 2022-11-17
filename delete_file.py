import os, shutil
def delete_files():
    folder = 'text_files'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        #print(filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def delete_audio():
    folder = 'converted_audio'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        #print(filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
if __name__ == '__main__':
    delete_files()
    delete_audio()