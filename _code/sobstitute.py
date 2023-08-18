# read all posts in the directory: 
#   - if the post contains a link irefill.it/content/...
#   - search the image in the directory and copy it there 
#   - change the link in the post
#   - save the post

import os
import re
import shutil

# directory where the posts are
posts_dir = "./content/post/"

# directory where the images are
images_dir = "C:/Users/Sebastian Cavada/uploads"

# directory where the images will be copied
images_dest_dir = "./static/uploads"

# list of posts
posts = os.listdir(posts_dir)

for post in posts[6:]:
    print(post)
    # list the files in the post directory
    files = os.listdir(posts_dir + post)

    md = [file for file in files if file.endswith(".md")][0]

    # read .md file
    with open(posts_dir + post + "/" + md, "r", encoding="utf-8") as f:
        text = f.read()

        # find all links that beginst with http://irefill.it/wp-content/
        links = re.findall(r"http://irefill.it/wp-content/.*", text)
        print(links)

        for link in links:
            new_link = link.replace("http://irefill.it/wp-content/uploads", images_dir).split(")")[0]
            print(new_link)

            # copy the image to the folder
            shutil.copy(new_link, posts_dir + post)            

            # change the link in the post
            text = text.replace(link, os.path.basename(new_link)+")")

    # save the post
    with open(posts_dir + post + "/" + md, "w", encoding="utf-8") as f:
        
        f.write(text)
    

# list of images
images = os.listdir(images_dir)

