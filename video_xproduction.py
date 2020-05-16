from moviepy.editor import *
# from video_production import , temp_path, newpath
# from video_production import *
# from reddit_comment_picker import count_real, temp_path_folder, newpath

def final_movie(newpath, count_real):
    def make_title_clip(path):
        pid_title = f"{path}\\comment_title"
        path_of_title_image = f"{pid_title}\\comment_title.png"
        path_of_title_audio = f"{pid_title}\\comment_title.mp3"
        audio = AudioFileClip(path_of_title_audio)
        # audio_comment_clip.append(audio)
        # audio = AudioFileClip(path_of_sub_audio)
        image = ImageClip(path_of_title_image).set_duration(audio.duration).set_fps(5).set_position("center")
        # image.with_duration(audio.duration).with_position(("center","top"))
        image = image.resize(0.9)
        final_clip = CompositeVideoClip([image],size=(1920,1080),bg_color=(0,0,0)).set_duration(image.duration)
        # final_clip.write_videofile(f"{pid_title}\\comment_title.mp4")
        # add transition clip here
        path_for_transition = f"C:\\Users\\MOHNISH\\AI\\Reddit_bot\\effects\\VHS_effect_cartoonish.mp4"
        transition_clip = VideoFileClip(path_for_transition)
        final_render = concatenate_videoclips([final_clip,transition_clip])
        final_render.write_videofile(f"{path}\\comment_title\\comment_title.mp4")

    temp_path = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\temp"
    # CHANGE///////////
    # newpath = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\common_saying_annoys"

    # no_of_subclips = int((len(count_real)/10)-1)
    # temp_path = temp_path_folder
    temp_video_clips_appended_2 = []

    # make comment clip from scratch
    make_title_clip(newpath)
    path_for_title_clip = f"{newpath}\\comment_title\\comment_title.mp4"
    video_comment = VideoFileClip(path_for_title_clip)
    # add transition clip here
    path_for_transition = f"C:\\Users\\MOHNISH\\AI\\Reddit_bot\\effects\\VHS_effect_cartoonish.mp4"
    transition_clip = VideoFileClip(path_for_transition)
    final_render = concatenate_videoclips([video_comment,transition_clip])

    temp_video_clips_appended_2.append(final_render)
    # for i in range(1,no_of_subclips+1):
    # CHANGE////////////
    # for i in range(1,8+1):
    for i in range(1,int((len(count_real)-1)/10)+1):
        video_subclips_final = []
        print(i)
        path_for_clip = f"{temp_path}\\movie_clip_{i}.mp4"
        # with VideoFileClip(path_for_clip) as video_comment:
        video_comment_2 = VideoFileClip(path_for_clip)
        temp_video_clips_appended_2.append(video_comment_2)
    final_clips_combined = concatenate_videoclips(temp_video_clips_appended_2,method="chain")

    # set the audio to some music
    audio_music = AudioFileClip("C:\\Users\\MOHNISH\\AI\\Reddit_bot\\effects\\KM_sneaky.mp3").audio_loop(duration=final_clips_combined.duration)
    mixed_audio = CompositeAudioClip([audio_music,final_clips_combined.audio])
    final_clips_combined.audio = mixed_audio

    final_clips_combined.write_videofile(f"{newpath}\\finally.mp4")

# video = VideoFileClip("myvideo.mp4")
# audio = AudioFileClip("myaudio.mp3").loop(duration= video.duration)
# video.audio = audio
