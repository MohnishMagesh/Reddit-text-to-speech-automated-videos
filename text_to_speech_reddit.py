# Reads out a script using google text to speech api
from gtts import gTTS
from reddit_comment_picker import newpath
import os
import re
import sys

# myText = "Hi, this is Google! I'd like to have a word with you in the 1930s"
#
# language = 'en-uk'
#
# output = gTTS(text=myText, lang=language, slow=False)
#
# output.save('output.mp3')
#
# os.system("start output.mp3")

# new list for keeping count of the number of no of sub audio files for a comment_ to later crosscheck with no of pngs
count_audio_real = ['placeholder']

def work(path):
    count_comment_mp3 = 0
	# with open(f"{tid}\\demo.txt", encoding='utf-8') as f:
	# 	lines = f.read().strip().split("\n\n")
    with open(f"{path}\\demo.txt", 'r') as f:
        lines = f.read().strip().split("\n\n")
    # for bad word replacement
	# with open("bad_word_rules.txt") as f_:
    # this is to save mp3 file of the title
    title = lines[0]
    title_text = title
    language = 'en-uk'
    output_title = gTTS(text=title_text, lang=language, slow=False)
    output_title.save(f"{newpath}\\comment_title\\comment_title.mp3")
	# 	# each line is "badword, replacement"
	# 	bad_words = [(x.split()[0], x.split()[1]) for x in f_.readlines()]
    with open(f"{path}\\bad_word_rules.txt") as f_:
        # each line is "badword, replacement"
        bad_words = [(x.split(",")[0], x.split(",")[1][:-1]) for x in f_.readlines()]
    print(lines)

    lister = []

    for i in range(1,len(lines)):
        try:
            comment = lines[i].split("\n")
            actual_comment = comment[2]
            count_comment_mp3 += 1
            # print(actual_comment)
            punctuation_reg = re.compile('(?<=[.!,?:;-]) +')
            split_parts = punctuation_reg.split(actual_comment)
            parts = list(filter(None, split_parts))
            print(parts)
            lister = parts
        except:
            continue


        path_for_project = newpath
        sub_comment_count_mp3 = 0
        for j in lister:
            current_text = j
            language = 'en-uk'
            output = gTTS(text=current_text, lang=language, slow=False)
            sub_comment_count_mp3 += 1
            output.save(f"{path_for_project}\\comment_{count_comment_mp3}\\sub_{sub_comment_count_mp3}.mp3")

        count_audio_real.append(sub_comment_count_mp3)
        # comment_content = comment[2]
    print(bad_words)

    # now for the actual audio files, every punctuation_reg



work('C:\\Users\\MOHNISH\\AI\\Reddit_bot')
