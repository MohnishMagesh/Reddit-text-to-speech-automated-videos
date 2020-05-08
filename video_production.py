from moviepy.editor import *
# from reddit_comment_picker import count_real, newpath
# from text_to_speech_reddit import count_audio_real

newpath = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\What is 10x scarier"

compilation_clips = []
# for i in range(1,len(count_real)-1):
for i in range(1,93):
    try:
        print(i)
        path_for_clip = f"{newpath}\\comment_{i}\\comment_{i}.mp4"
        video_comment = VideoFileClip(path_for_clip)
        compilation_clips.append(video_comment)
    except:
        continue

print(compilation_clips)
final_clips_combined = concatenate_videoclips(compilation_clips,method="chain")
final_clips_combined.write_videofile(f"{newpath}\\final_movie.mp4")
