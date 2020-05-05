# Reads out a script using google text to speech api
from gtts import gTTS
import os
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

def work(tid):
	# with open(f"{tid}\\demo.txt", encoding='utf-8') as f:
	# 	lines = f.read().strip().split("\n\n")
    with open(f"{tid}\\demo.txt", 'r') as f:
        lines = f.read().strip().split("\n\n")
	# with open("resources/rules.txt") as f:
	# 	# each line is "badword, replacement"
	# 	bad_words = [(x.split()[0], x.split()[1]) for x in f.readlines()]
    print(lines)

work('C:\\Users\\MOHNISH\\AI\\Reddit_bot')
