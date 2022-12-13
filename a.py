

import os
import subprocess

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

# copy 
dir_target = '/Users/jiechau_huang/Downloads/video'
dir_this = '/Users/jiechau_huang/it_books_course/2021_1019_coursera_bigdata_ml_fundamentals_google/wk1'
for file in get_files(dir_this):
    # file is string
    if file.endswith('vtt'):
        #print(file)
        file_new = file.split(' ')[0]
        file_new = file_new + '.vtt'
        #print(file_new)
        #
        result = subprocess.run(['/bin/cp',dir_this + '/' + file, dir_target + '/' + file_new],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding="utf-8")

    if file.endswith('mp4'):
        #print(file)
        file_new = file.split(' ')[0]
        file_new = file_new + '.mp4'
        #print(file_new)
        result = subprocess.run(['/bin/cp',dir_this + '/' + file, dir_target + '/' + file_new],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding="utf-8")

# make new file
for file in get_files(dir_target):
    if file.endswith('mp4'):
        print(file)
        file_base = file.split('.')[0]
        file_new = file_base + '_subtitle.mp4'
        #print(file_base)
        #print(file_new)
        # ./ffmpeg -i a.mp4 -vf subtitles=a.vtt b.mp4
        result = subprocess.run(['./ffmpeg', '-i', file, '-vf', 'subtitles=' + file_base + '.vtt', file_new])
   



