# Reddit-text-to-speech-automated-videos
You can generate automated reddit videos, a bot will read comments from reddit and transform it into a video.
- google's text to speech api is being used here to read the comments on a reddit post
- jinja is used to format template and wkhtmltopdf/wkhtmltoimage is used to render .png file of the html file
- moviepy is used to edit the videos automatically
- the only input required is the post link and comment limit
- all comments and the usernames are stored in a .txt file
- you may need to change file paths according to your system in order for it to work
