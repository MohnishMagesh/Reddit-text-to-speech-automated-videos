from moviepy.editor import *
# from video_production import , temp_path, newpath
# from video_production import *
# from reddit_comment_picker import count_real, temp_path_folder, newpath

# temp_path = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\temp"
# newpath = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\What is the most ef"

no_of_subclips = int((len(count_real)/10)-1)
temp_path = temp_path_folder
temp_video_clips_appended_2 = []
for i in range(1,no_of_subclips+1):
# for i in range(1,2+1):
    video_subclips_final = []
    print(i)
    path_for_clip = f"{temp_path}\\movie_clip_{i}.mp4"
    # with VideoFileClip(path_for_clip) as video_comment:
    video_comment_2 = VideoFileClip(path_for_clip)
    temp_video_clips_appended_2.append(video_comment_2)
final_clips_combined = concatenate_videoclips(temp_video_clips_appended_2,method="chain")
final_clips_combined.write_videofile(f"{newpath}\\finally.mp4")
