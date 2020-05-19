# Reads out a script using google text to speech api
from gtts import gTTS
import os
import re
import sys

def work(path,newpath):
    count_comment_mp3 = 0
    count_audio_real = ['placeholder']

    # open comments text file and split them
    with open(f"{path}\\demo.txt", 'r') as f:
        lines = f.read().strip().split("\n\n")

    # first line of the text file is always the title
    title = lines[0]
    title_text = title
    language = 'en-uk'
    output_title = gTTS(text=title_text, lang=language, slow=False)
    output_title.save(f"{newpath}\\comment_title\\comment_title.mp3")

    # remove bad words from the comment and replace them
    with open(f"{path}\\bad_word_rules.txt") as f_:
        # each line is "badword, replacement"
        bad_words = [(x.split(",")[0], x.split(",")[1][:-1]) for x in f_.readlines()]
    print(lines)

    lister = []

    # replace bad word in title
    for word in bad_words:
        title = title.replace(word[0], word[1])

    # iterate through comments and split into parts for storytelling vibe
    for i in range(1,len(lines)+1):
        try:
            comment = lines[i].split("\n")
            actual_comment = comment[2]

            # replace bad words in the actual comment
            for word in bad_words:
                actual_comment = actual_comment.replace(word[0], word[1])
            count_comment_mp3 += 1
            punctuation_reg = re.compile('(?<=[.!,?:;-]) +')
            split_parts = punctuation_reg.split(actual_comment)
            parts = list(filter(None, split_parts))
            print(parts)
            lister = parts
        except:
            continue

        sub_comment_count_mp3 = 0
        try:
            path_for_project = newpath
            for j in lister:
                current_text = j
                language = 'en-uk'
                output = gTTS(text=current_text, lang=language, slow=False)
                sub_comment_count_mp3 += 1
                output.save(f"{path_for_project}\\comment_{count_comment_mp3}\\sub_{sub_comment_count_mp3}.mp3")

            count_audio_real.append(sub_comment_count_mp3)
        except:
            count_audio_real.append(sub_comment_count_mp3)
            continue
    return count_audio_real
