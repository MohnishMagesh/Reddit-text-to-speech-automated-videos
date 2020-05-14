from moviepy.editor import *
# from reddit_comment_picker import count_real, newpath
# from text_to_speech_reddit import count_audio_real
# from video_compilation import *
import gc

# CHANGE///////////
newpath = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\school_game_loading_tips"

# compilation_clips = []
# for i in range(1,len(count_real)-1):
# for i in range(1,93):
#     try:
#         print(i)
#         path_for_clip = f"{newpath}\\comment_{i}\\comment_{i}.mp4"
#         video_comment = VideoFileClip(path_for_clip)
#         compilation_clips.append(video_comment)
#     except:
#         continue
#
# print(compilation_clips)
# final_clips_combined = concatenate_videoclips(compilation_clips,method="chain")
# final_clips_combined.write_videofile(f"{newpath}\\final_movie.mp4")

temp_path = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder"

# no_of_subclips = 0

# for k in range(1,int((len(count_real)-1)/10)+1):
# CHANGE///////////
for k in range(1,int(35/10)+1):
    temp = k*10
    temp_video_clips_appended = []
    for i in range(temp-9,temp+1):
        try:
            print(i)
            path_for_clip = f"{newpath}\\comment_{i}\\comment_{i}.mp4"
            # with VideoFileClip(path_for_clip) as video_comment:
            video_comment = VideoFileClip(path_for_clip)
            # temp_video_clips_appended.append(video_comment)
            # add transition clip here
            path_for_transition = f"C:\\Users\\MOHNISH\\AI\\Reddit_bot\\effects\\VHS_effect_cartoonish.mp4"
            transition_clip = VideoFileClip(path_for_transition)
            final_render = concatenate_videoclips([video_comment,transition_clip]) #////
            # temp_video_clips_appended.append(video_comment) #////
            temp_video_clips_appended.append(final_render) #////
        except:
            continue

    print(temp_video_clips_appended)
    final_clips_combined = concatenate_videoclips(temp_video_clips_appended,method="chain")
    final_clips_combined.write_videofile(f"{temp_path}\\temp\\movie_clip_{k}.mp4",threads=4)
    gc.collect()
    # no_of_subclips += 1

# no_of_subclips_str = str(no_of_subclips)
