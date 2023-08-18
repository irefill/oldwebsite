from pathlib import Path
from PIL import Image

def convert_to_webp_jpg(image_path):
    image = Image.open(image_path)    
    res = str(image_path).replace(".jpg", ".webp")
    image.save(res, "WEBP")

def convert_to_webp_jpeg(image_path):
    image = Image.open(image_path)    
    res = str(image_path).replace(".jpeg", ".webp")
    image.save(res, "WEBP")

def convert_to_webp_png(image_path):
    image = Image.open(image_path)    
    res = str(image_path).replace(".png", ".webp")
    image.save(res, "WEBP")

# for each folder in the content/post directory
for folder in Path("../content/post").iterdir():
    if folder.is_dir():
        # for each file in the folder
        for file in folder.iterdir():
            print("converting " + str(file))
            # if it is a jpg file
            if file.suffix == ".jpg":
                #check if the .webp file already exists
                if Path(str(file).replace(".jpg", ".webp")).exists():
                    print("webp file already exists")
                    continue
                else:
                    # convert it to webp
                    convert_to_webp_jpg(file)
            # if it is a jpeg file
            elif file.suffix == ".png":
                if Path(str(file).replace(".png", ".webp")).exists():
                    print("webp file already exists")
                    continue
                else:
                    #convert it to webp
                    convert_to_webp_png(file)
            elif file.suffix == ".jpeg":                
                if Path(str(file).replace(".jpeg", ".webp")).exists():
                    print("webp file already exists")
                    continue
                else:
                    #convert it to webp
                    convert_to_webp_jpeg(file)