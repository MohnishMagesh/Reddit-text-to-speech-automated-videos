import reddit_comment_picker
import text_to_speech_reddit
import video_compilation
import video_production
import video_xproduction
import gc

def main(folder_name,url,comment_limit):
    """ --- this is the kind of format you can expect to enter ---
    folder_name = "what_sucks_about_your_age"
    url = "https://www.reddit.com/r/AskReddit/comments/gkfaeh/what_sucks_about_being_your_age/"
    comment_limit = 50
    """
    newpath, count_real = reddit_comment_picker.createImages(folder_name,url,comment_limit)
    count_audio_real = text_to_speech_reddit.work('C:\\Users\\MOHNISH\\AI\\Reddit_bot',newpath)
    video_compilation.make_movie(newpath, count_real, count_audio_real)
    video_production.make_subclips(newpath, count_real)
    video_xproduction.final_movie(newpath, count_real)

if __name__ == "__main__":
    folder_names = ["biggest_misconception_as_child",
                    "friend_introduced_glad",
                    "declassified_govt_info"]
    urls = ["https://www.reddit.com/r/AskReddit/comments/gkghvf/what_was_the_biggest_misconception_that_you_had/",
            "https://www.reddit.com/r/AskReddit/comments/gktfx1/whats_something_youre_glad_your_friend_introduced/",
            "https://www.reddit.com/r/AskReddit/comments/edwa4h/what_are_some_lesserknown_secondary_uses_for_an/"]
    comment_limits = [60,50,60]
    for i in range(1,len(urls)):
        main(folder_names[i],urls[i],comment_limits[i])
        gc.collect()
