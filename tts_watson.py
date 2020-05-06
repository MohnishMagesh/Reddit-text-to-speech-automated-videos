from gtts import gTTS

count_comment_mp3 = 1
current_text = "I like to hallucinate in the dark, it makes me stutter."
language = 'en-uk'
output = gTTS(text=current_text, lang=language, slow=False)
sub_comment_count_mp3 = 1
output.save(f"{path_for_project}\\comment_{count_comment_mp3}\\sub_{sub_comment_count_mp3}.mp3")
