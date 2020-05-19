from moviepy.editor import *
import numpy as np
import gc

def make_movie(newpath, count_real, count_audio_real):
    path_defined_for_clips = newpath

    def make_title_clip(path):

        # getting path of the comment title
        pid_title = f"{path}\\comment_title"
        path_of_title_image = f"{pid_title}\\comment_title.png"
        path_of_title_audio = f"{pid_title}\\comment_title.mp3"
        audio = AudioFileClip(path_of_title_audio)

        # adding title image to the imageclip
        image = ImageClip(path_of_title_image).set_duration(audio.duration).set_fps(5).set_position("center")
        image = image.resize(1)
        final_clip = CompositeVideoClip([image],size=(1920,1080),bg_color=(26,26,27)).set_duration(image.duration)

        # add transition clip here
        path_for_transition = f"C:\\Users\\MOHNISH\\AI\\Reddit_bot\\effects\\VHS_effect_cartoonish.mp4"
        transition_clip = VideoFileClip(path_for_transition)
        final_render = concatenate_videoclips([final_clip,transition_clip])
        final_render.write_videofile("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\temp\\comment_title.mp4")


    def process_clips(i):
        print(i)
        pid = f"{path_defined_for_clips}\\comment_{i}"

        # for each comment_{}\\sub_{}.mp3 or sub_{}.png
        if count_audio_real[i] == count_real[i]:
            comment_clips = []
            audio_comment_clip = []

            # combining audio and image for each subclip of the comment
            for j in range(1,count_real[i]+1):
                path_of_sub_audio = f"{pid}\\sub_{j}.mp3"
                path_of_sub_image = f"{pid}\\sub_{j}.png"
                try:
                    audio = AudioFileClip(path_of_sub_audio)
                    audio_comment_clip.append(audio)
                    image = ImageClip(path_of_sub_image).set_duration(audio.duration).set_fps(30).set_position((0.0,0.08),relative=True)
                    image = image.resize(1.875)

                    # combining audio and image of subclip of comment
                    final_clip = CompositeVideoClip([image],size=(1920,1080),bg_color=(26,26,27)).set_duration(image.duration)
                    comment_clips.append(final_clip)
                except:
                    continue

            print(audio_comment_clip)
            total_comment_audio = concatenate_audioclips(audio_comment_clip)
            comment_video_clip_for_now = concatenate_videoclips(comment_clips,method="chain")
            comment_video_clip_for_now = comment_video_clip_for_now.set_audio(total_comment_audio)
            comment_video_clip_for_now.write_videofile(f"{pid}\\comment_{i}.mp4", threads=4)


    for comment_no in range(1,len(count_real)):
        try:
            process_clips(comment_no)
        except:
            continue
        gc.collect()
    make_title_clip(path_defined_for_clips)
