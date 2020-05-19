from moviepy.editor import *
# from reddit_comment_picker import count_real, newpath
# from text_to_speech_reddit import count_audio_real
# from video_compilation import *
import gc

# CHANGE///////////
def make_subclips(newpath, count_real):
    # newpath = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\common_saying_annoys"

    temp_path = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder"

    # no_of_subclips = 0

    for k in range(1,int((len(count_real)-1)/10)+1):
    # CHANGE///////////
    # for k in range(1,int(80/10)+1):
        temp = k*10
        temp_video_clips_appended = []
        for i in range(temp-9,temp+1):
            try:
                print(i)
                path_for_clip = f"{newpath}\\comment_{i}\\comment_{i}.mp4"
                # with VideoFileClip(path_for_clip) as video_comment:
                video_comment = VideoFileClip(path_for_clip)
                video_comment.duration = video_comment.duration - 0.25
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
