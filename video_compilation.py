from moviepy.editor import *
import numpy as np
import gc
# from moviepy.video.io.VideoFileClip import VideoFileClip
from reddit_comment_picker import count_real, newpath
from text_to_speech_reddit import count_audio_real


# # useful snippets
# img = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png',
#        '7.png', '8.png', '9.png', '10.png', '11.png', '12.png']
#
# clips = [ImageClip(m).set_duration(2)
#       for m in img]
#
# concat_clip = concatenate_videoclips(clips, method="compose")
# concat_clip.write_videofile("test.mp4", fps=24)

# # VIDEO CLIPS
# clip = VideoClip(make_frame, duration=4) # for custom animations (see below)
# clip = VideoFileClip("my_video_file.mp4") # or .avi, .webm, .gif ...
# clip = ImageSequenceClip(['image_file1.jpeg', ...], fps=24)
# clip = ImageClip("my_picture.png") # or .jpeg, .tiff, ...
# clip = TextClip("Hello !", font="Amiri-Bold", fontsize=70, color="black")
# clip = ColorClip(size=(460,380), color=[R,G,B])
#
# # AUDIO CLIPS
# clip = AudioFileClip("my_audiofile.mp3") # or .ogg, .wav... or a video !
# clip = AudioArrayClip(numpy_array, fps=44100) # from a numerical array
# clip = AudioClip(make_frame, duration=3) # uses a function make_frame(t)

# count_real = ['placeholder', 4, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 10, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 13, 1, 1, 1, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 17, 1, 2, 2, 1, 2, 3, 1, 3, 1, 1, 2, 1, 1, 1, 4, 3, 1, 1, 1, 1, 1, 2, 1, 10, 1, 1, 1, 1, 5, 1]
#
# count_audio_real = ['placeholder', 4, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 10, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 14, 1, 1, 2, 1, 2, 3, 1, 3, 1, 1, 2, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 2, 1, 10, 1, 1, 1, 1, 5, 1]

# replace it with the path of the clips folder
# path_defined_for_clips = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\What is the most ef"
path_defined_for_clips = newpath
# newpath = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder"

#////////////////////////////////////////////////////////
# def make_movie(path):
#     # for each comment_{} folder
#     final_compiled_video = []
#     for i in range(1,len(count_real)-1):
#     # for i in range(1,116):
#     # for i in range(1,end):
#         print(i)
#         pid = f"{path_defined_for_clips}\\comment_{i}"
#         # for each comment_{}\\sub_{}.mp3 or sub_{}.png
#         if count_audio_real[i] == count_real[i]:
#             # comment_video = []
#             comment_clips = []
#             # duration_comment_clip = []
#             audio_comment_clip = []
#             for j in range(1,count_real[i]+1):
#                 path_of_sub_audio = f"{pid}\\sub_{j}.mp3"
#                 path_of_sub_image = f"{pid}\\sub_{j}.png"
#                 audio = AudioFileClip(path_of_sub_audio)
#                 audio_comment_clip.append(audio)
#                 # audio = AudioFileClip(path_of_sub_audio)
#                 image = ImageClip(path_of_sub_image).set_duration(audio.duration).set_fps(30).set_position((0.0,0.2),relative=True)
#                 # image.with_duration(audio.duration).with_position(("center","top"))
#                 image = image.resize(1.875)
#                 final_clip = CompositeVideoClip([image],size=(1920,1080),bg_color=(0,0,0)).set_duration(image.duration)
#                 comment_clips.append(final_clip)
#             # concatenate videoclips for single comment clip
#             # comment_video_clip = concatenate_videoclips(comment_video,method="compose")
#             print(audio_comment_clip)
#             total_comment_audio = concatenate_audioclips(audio_comment_clip)
#             comment_video_clip_for_now = concatenate_videoclips(comment_clips,method="chain")
#             comment_video_clip_for_now = comment_video_clip_for_now.set_audio(total_comment_audio)
#             # final_compiled_video.append(comment_video_clip_for_now)
#             comment_video_clip_for_now.write_videofile(f"{pid}\\comment_{i}.mp4", threads=4)
#             # print(comment_video_clip_for_now)
#             # comment_video_clip_for_now.write_videofile("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\movie1.mp4")
#         else:
#             continue

    # final_video = concatenate_videoclips(final_compiled_video,method="chain")
    # # final_video.write_videofile(f"{newpath}\\movie.mp4")
    # return final_video

def make_title_clip(path):
    pid_title = f"{path}\\comment_title"
    path_of_title_image = f"{pid_title}\\comment_title.png"
    path_of_title_audio = f"{pid_title}\\comment_title.mp3"
    audio = AudioFileClip(path_of_title_audio)
    # audio_comment_clip.append(audio)
    # audio = AudioFileClip(path_of_sub_audio)
    image = ImageClip(path_of_title_image).set_duration(audio.duration).set_fps(5).set_position("center")
    # image.with_duration(audio.duration).with_position(("center","top"))
    image = image.resize(1)
    final_clip = CompositeVideoClip([image],size=(1920,1080),bg_color=(0,0,0)).set_duration(image.duration)
    # final_clip.write_videofile(f"{pid_title}\\comment_title.mp4")
    # add transition clip here
    path_for_transition = f"C:\\Users\\MOHNISH\\AI\\Reddit_bot\\effects\\VHS_effect_cartoonish.mp4"
    transition_clip = VideoFileClip(path_for_transition)
    final_render = concatenate_videoclips([final_clip,transition_clip])
    final_render.write_videofile("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\temp")

# make_movie(path_defined_for_clips)
# make_title_clip(path_defined_for_clips)

def process_clips(i):
    print(i)
    pid = f"{path_defined_for_clips}\\comment_{i}"
    # for each comment_{}\\sub_{}.mp3 or sub_{}.png
    if count_audio_real[i] == count_real[i]:
        # comment_video = []
        comment_clips = []
        # duration_comment_clip = []
        audio_comment_clip = []
        for j in range(1,count_real[i]+1):
            path_of_sub_audio = f"{pid}\\sub_{j}.mp3"
            path_of_sub_image = f"{pid}\\sub_{j}.png"
            audio = AudioFileClip(path_of_sub_audio)
            audio_comment_clip.append(audio)
            # audio = AudioFileClip(path_of_sub_audio)
            image = ImageClip(path_of_sub_image).set_duration(audio.duration).set_fps(30).set_position((0.0,0.2),relative=True)
            # image.with_duration(audio.duration).with_position(("center","top"))
            image = image.resize(1.875)
            final_clip = CompositeVideoClip([image],size=(1920,1080),bg_color=(0,0,0)).set_duration(image.duration)
            comment_clips.append(final_clip)
        # concatenate videoclips for single comment clip
        # comment_video_clip = concatenate_videoclips(comment_video,method="compose")
        print(audio_comment_clip)
        total_comment_audio = concatenate_audioclips(audio_comment_clip)
        comment_video_clip_for_now = concatenate_videoclips(comment_clips,method="chain")
        comment_video_clip_for_now = comment_video_clip_for_now.set_audio(total_comment_audio)
        # final_compiled_video.append(comment_video_clip_for_now)
        comment_video_clip_for_now.write_videofile(f"{pid}\\comment_{i}.mp4", threads=4)
        # print(comment_video_clip_for_now)
        # comment_video_clip_for_now.write_videofile("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\movie1.mp4")
    # else:
    #     continue


for comment_no in range(1,len(count_real)-1):
    process_clips(comment_no)
    gc.collect()
make_title_clip(path_defined_for_clips)


# total_video = []

# for k in range(1,int((len(count_real)-1)/10)):
#     temp = k*10
#     video_clip_part = make_movie(path_defined_for_clips,start=temp-9,end=temp)
#     total_video.append(video_clip_part)
#     print(total_video)
#
# full_and_final = concatenate_videoclips(total_video,method="chain")
# full_and_final.write_videofile(f"{newpath}\\movie.mp4")
