import praw, re
import datetime
import os
import pdfkit
import imgkit
import random
import jinja2
from jinja2 import Environment, FileSystemLoader, BaseLoader, PackageLoader
from praw.models import MoreComments

def createImages(folder_name,url,comment_limit):
    temp_path_folder = "C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\temp"
    if not os.path.exists(temp_path_folder):
        os.makedirs(temp_path_folder)

    # make a jinja environment and setup
    jinja_env = jinja2.Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
    template = jinja_env.get_template('templates/reddit_sample_template.html')
    template_title = jinja_env.get_template('templates/reddit_title_template.html')

    reddit = praw.Reddit(user_agent=[enter your useragent], client_id=[enter your client_id], client_secret=[enter your cliend secret])

    # put your subreddit post url, subreddits allowed are = ['AskReddit','']
    submission = reddit.submission(url=url)
    # getting subreddit name from the submission
    subreddit_name = str(submission.subreddit)

    #open file handler for saving comments and attributes
    fh = open('C:\\Users\\MOHNISH\\AI\\Reddit_bot\\demo.txt','w')

    title = submission.title
    fh.write(title+'\n')
    fh.write('\n')

    # now to create new folder to save all comment images
    path_for_images = 'C:\\Users\\MOHNISH\\AI\\Reddit_bot\\result_video_folder\\'
    newpath = path_for_images + folder_name
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    # for creating separate title file to store image and mp3
    if not os.path.exists(f"{newpath}\\comment_title"):
        os.makedirs(f"{newpath}\\comment_title")
    jinja_var_title = {'subreddit': subreddit_name,'title_name': title}
    subreddit_title_template = template_title.render(jinja_var_title)

    # writing title of post to the first line of the text file
    with open('output_title.html','w') as f:
        f.write(subreddit_title_template)
    comment_image_path = f"{newpath}\\comment_title\\comment_title.png"
    imgkit.from_file('output_title.html',comment_image_path)


    count_comment = 0

    # create list to count the no of images needed for each comment
    count_real = ['placeholder']

    counter = 0

    # iterating through the comments
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        if counter > comment_limit:
            break
        counter += 1

        punctuation_reg = re.compile('(?<=[.!,?:;-]) +')
        size_in_chars_of_comment = len(top_level_comment.body)

        # check if size of the comment is more than 2000 characters in length
        if(size_in_chars_of_comment>1200):
            continue
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

        # writing comment attributes inside text file to read later
        try:
            user = str(top_level_comment.author)
            upvotes = str(top_level_comment.score)
            content = str(top_level_comment.body)
            content = content.replace('\n','.')
            if(len(content)>0):
                key_content = True
            print(key_content)
            if(user == None or user == ''):
                fh.write('deleted'+'\n')
            else:
                fh.write(user+'\n')
            if(upvotes == None or upvotes == ''):
                fh.write('deleted'+'\n')
            else:
                fh.write(upvotes+'\n')
            if(content == None or content == ''):
                fh.write('deleted\n')
            else:
                fh.write(content+'\n')
                fh.write('\n')
        except:
            fh.write('interesting'+'\n')
            fh.write('\n')
            continue

        # now to create new folders to save punctuation separated images in this folder
        count = 0
        current_comment_str = ''
        logo_number = str(random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
        for i in parts:
            # now create jinja variables for inserting into template
            current_comment_str += i

            # passing variables to jinja template
            jinja_var = {'username': user,'noUpvotes': upvotes,'subcomment': current_comment_str,'number': logo_number}
            sub_img_template = template.render(jinja_var)
            # sub_img = template.render(jinja_var)
            with open('output.html','w') as f:
                f.write(sub_img_template)
            count += 1
            subcomment_number = 'sub_' + str(count) + '.png'
            sub_path = newpath_for_comment + '\\' + subcomment_number
            imgkit.from_file('output.html',sub_path)


    fh.close()
    return newpath, count_real
