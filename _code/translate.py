# read all posts in the directory: 
#   - if the post contains a link irefill.it/content/...
#   - search the image in the directory and copy it there 
#   - change the link in the post
#   - save the post

import os
import re
import shutil
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)


# directory where the posts are
posts_dir = "../content/post/"

# list of posts
posts = os.listdir(posts_dir)

for post in posts:
    # list the files in the post directory
    files = os.listdir(posts_dir + post)

    md = [file for file in files if file.endswith(".it.md")]

    if(len(md) == 0):
        continue
    else:
        print(post)
        md = md[0]
        print(md)
        # read .md file
        with open(posts_dir + post + "/" + md, "r", encoding="utf-8") as f:
            text = f.read()

