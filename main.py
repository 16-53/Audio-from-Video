from datetime import date

import moviepy.editor


def get_sound(path):
    video = moviepy.editor.VideoFileClip(path)
    audio = video.audio
    today = str(date.today())
    return audio.write_audiofile("1653-" + today + ".mp3")

get_sound(input())
