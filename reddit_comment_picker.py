import praw, re
import datetime
import os
import pdfkit
import imgkit
import random
# import jinja
import jinja2
from jinja2 import Environment, FileSystemLoader, BaseLoader, PackageLoader
from praw.models import MoreComments

# make a jinja environment and setup
# jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\templates'))
jinja_env = jinja2.Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
# template = jinja_env.get_template('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\templates\\reddit_jinja_template.html')
template = jinja_env.get_template('templates/reddit_sample_template.html')

reddit = praw.Reddit(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0', client_id='teH3QtlEXPNiCA', client_secret="HTRTxJcFd6PWzGD_osnSv2QKGpc")

url = "https://www.reddit.com/r/AskReddit/comments/gcbqi7/what_is_10x_scarier_at_night_than_day/"
submission = reddit.submission(url=url)

#open file handler for saving comments and attributes
fh = open('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\demo.txt','w')

title = submission.title
fh.write(title+'\n')
fh.write('\n')

# now to create new folder to save all comment images
path_for_images = 'C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\'
folder_name = title[0:19]
newpath = path_for_images + folder_name
if not os.path.exists(newpath):
    os.makedirs(newpath)

count_comment = 0

# create list to count the no of images needed for each comment
count_real = ['placeholder']

for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    punctuation_reg = re.compile('(?<=[.!,?:;-]) +')
    split_parts = punctuation_reg.split(top_level_comment.body)
    parts = list(filter(None, split_parts))
    count_real.append(len(parts))

    # now to create new folder to save this comment images
    count_comment += 1
    path_for_image_comment = 'C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\'+folder_name+'\\'
    folder_name_comment = 'comment_' + str(count_comment)
    newpath_for_comment = path_for_image_comment + folder_name_comment
    print(newpath_for_comment)
    if not os.path.exists(newpath_for_comment):
        os.makedirs(newpath_for_comment)

    # split_parts = punctuation_reg.split(top_level_comment.body)
	# parts = list(filter(None, split_parts))
    user = str(top_level_comment.author)
    # print(top_level_comment.author)
    fh.write(user+'\n')
    upvotes = str(top_level_comment.score)
    # print(top_level_comment.score)
    fh.write(upvotes+'\n')
    # print(dir(top_level_comment))
    # print(parts)
    # print(top_level_comment.body)
    content = str(top_level_comment.body)
    fh.write(content+'\n')
    fh.write('\n')

    # now to create new folders to save punctuation separated images in this folder
    count = 0
    current_comment_str = ''
    # logo_number = str(random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
    for i in parts:
        # now create jinja variables for inserting into template
        current_comment_str += i

        jinja_var = {'username': user,'noUpvotes': upvotes,'subcomment': current_comment_str}
        sub_img_template = template.render(jinja_var)
        # sub_img = template.render(jinja_var)
        with open('output.html','w') as f:
            f.write(sub_img_template)
        count += 1
        subcomment_number = 'sub_' + str(count) + '.png'
        sub_path = newpath_for_comment + '\\' + subcomment_number
        # imgkit.from_file('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\template\\output.html', sub_path)
        imgkit.from_file('output.html',sub_path)


fh.close()
