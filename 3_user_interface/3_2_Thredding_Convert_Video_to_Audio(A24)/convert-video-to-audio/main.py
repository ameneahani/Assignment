import time
from moviepy.editor import VideoFileClip


addresses = ['VideoClip/Babak Jahanbakhsh - Mirim Jonoob (Live Version) 720p.mp4',
          'VideoClip/chavoshi - alaj.mp4',
          'VideoClip/Hamid Askari - Be Delam Moond (Live Version) 480p.mp4',
          'VideoClip/Mohsen Ebrahimzadeh - Doostam 720p.mp4',
          'VideoClip/Reza Sadeghi - Doroghe Ghashang 720p.mp4']
time_start = time.time()
i = 1
for address in addresses:
    video = VideoFileClip(address)
    video.audio.write_audiofile(f'audio{i}.mp3')
    i += 1

time_end = time.time()
print(time_end- time_start)