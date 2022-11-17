from moviepy.editor import concatenate_audioclips, AudioFileClip
import os

def concatenate_audio_moviepy(audio_clip_paths, output_path):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)

entries = os.listdir('converted_audio/')
orginal_files = []

if __name__ == '__main__':
    for entry in entries:
        audiofiles = "converted_audio/{}".format(entry)
        orginal_files.append(audiofiles)
    concatenate_audio_moviepy(orginal_files,"converted_audio/output.mp3")
    for file in orginal_files:
        os.remove("{}".format(file))