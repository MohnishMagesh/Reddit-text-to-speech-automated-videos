from moviepy.editor import *
import numpy as np

path_defined_for_clips = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\What is 10x scarier"

# def make_movie(path):
#     for i in range(1,len(count_real)-1):
#         pid = f"{path_defined_for_clips}\\comment_{i}"
#         if count_audio_real[i] == count_real[i]:
#             for j in range(1,count_real[i]):
#                 path_of_sub_audio = f"{pid}\\sub_{j}.mp3"
#                 path_of_sub_image = f"{pid}\\sub_{j}.png"
#                 audio = AudioFileClip(path_of_sub_audio)
#                 image = ImageClip(path_of_sub_image)
#                         .set_duration(audio.duration)
#                         .set_fps(5)
#                         .set_pos(card_upper_corner)
#                         .set_audio(audio)

comment_clips = []
# duration_comment_clip = []
audio_comment_clip = []
for j in range(1,5):
    pid = f"{path_defined_for_clips}\\comment_1"
    path_of_sub_audio = f"{pid}\\sub_{j}.mp3"
    path_of_sub_image = f"{pid}\\sub_{j}.png"
    audio = AudioFileClip(path_of_sub_audio)
    audio_comment_clip.append(audio)
    # image = ImageClip(path_of_sub_image).set_duration(audio.duration).set_fps(5).set_audio(audio).set_position(("center","top"))
    image = ImageClip(path_of_sub_image).set_duration(audio.duration).set_fps(5).set_position((0.0,0.2),relative=True)
    # image.with_duration(audio.duration).with_position(("center","top"))
    image = image.resize(1.875)
    final_clip = CompositeVideoClip([image],size=(1920,1080),bg_color=(0,0,0)).set_duration(image.duration)
    # final_clip.write_videofile("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\movie1.mp4")
    comment_clips.append(final_clip)
    # duration_comment_clip.append(image.duration)
total_comment_audio = concatenate_audioclips(audio_comment_clip)
comment_video_clip_for_now = concatenate_videoclips(comment_clips,method="chain")
comment_video_clip_for_now = comment_video_clip_for_now.set_audio(total_comment_audio)
print(comment_video_clip_for_now)
comment_video_clip_for_now.write_videofile("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\movie1.mp4")
