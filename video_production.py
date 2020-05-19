from moviepy.editor import *
import gc

def make_subclips(newpath, count_real):

    temp_path = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder"

    # creating subclips by taking batches of 10 comments and storing them in temp folder
    for k in range(1,int((len(count_real)-1)/10)+1):
        temp = k*10
        temp_video_clips_appended = []
        for i in range(temp-9,temp+1):
            try:
                print(i)
                path_for_clip = f"{newpath}\\comment_{i}\\comment_{i}.mp4"
                video_comment = VideoFileClip(path_for_clip)
                video_comment.duration = video_comment.duration - 0.25

                # path for transition clips between each comment clip
                path_for_transition = f"C:\\Users\\MOHNISH\\AI\\Reddit_bot\\effects\\VHS_effect_cartoonish.mp4"
                transition_clip = VideoFileClip(path_for_transition)
                final_render = concatenate_videoclips([video_comment,transition_clip])
                temp_video_clips_appended.append(final_render)
            except:
                continue

        print(temp_video_clips_appended)
        final_clips_combined = concatenate_videoclips(temp_video_clips_appended,method="chain")
        final_clips_combined.write_videofile(f"{temp_path}\\temp\\movie_clip_{k}.mp4",threads=4)
        # memory management for clearing out unreference objects (important for moviepy)
        gc.collect()
