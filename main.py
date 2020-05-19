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
    folder_names = ["closest_thing_to_magic",
                    "mariners_weirdest_thing_at_sea",
                    "question_hate_getting_asked"]
    urls = ["https://www.reddit.com/r/AskReddit/comments/glpg0f/whats_the_closest_thing_to_magic_in_existence/",
            "https://www.reddit.com/r/AskReddit/comments/gl4g2d/mariners_of_reddit_whats_the_strangest_thing/",
            "https://www.reddit.com/r/AskReddit/comments/gkwoe8/whats_one_question_you_hate_being_asked/"]
# https://www.reddit.com/r/AskReddit/comments/gl2wln/what_is_your_favorite_insult_of_all_time/
# https://www.reddit.com/r/AskReddit/comments/gln8tu/people_who_had_covid19_or_know_someone_who_did/
# https://www.reddit.com/r/AskReddit/comments/gkxiju/what_is_something_that_is_universally_a_dick_move/
    comment_limits = [110,60,90]
    for i in range(1,len(urls)):
        main(folder_names[i],urls[i],comment_limits[i])
        gc.collect()
    # main(folder_names[0],urls[0],comment_limits[0])
