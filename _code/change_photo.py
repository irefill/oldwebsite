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

# list of posts
posts = os.listdir(posts_dir)

print(posts)

for post in posts[6:]:
    print(post)
    # list the files in the post directory
    files = os.listdir(posts_dir + post)

    md = [file for file in files if file.endswith(".md")][0]    

    # read .md file
    with open(posts_dir + post + "/" + md, "r", encoding="utf-8") as f:
        text = f.read()        

        # find all images in the post that ends with .jpg, .jpeg or .png
        photos = re.findall(r"([\w-]+\.(png|jpe?g))", text)        

        for photo in photos:        
            print(photo[0])
            # change the link in the post
            print(os.path.basename(photo[0]).split(".")[0] + ".webp")
            text = text.replace(photo[0], os.path.basename(photo[0]).split(".")[0] + ".webp")

        # save the post
    with open(posts_dir + post + "/" + md, "w", encoding="utf-8") as f:        
        f.write(text)

