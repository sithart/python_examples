import os
from PIL import  Image

files = os.listdir('/home/sitharth/quarantine/python_examples/images')
# print(files)
images = [file for file in files if file.endswith(('jpg', 'png'))]

print(images)

for image in images:
    im = Image.Open(os.path(image))
    print(im)
    # image_name = image.split('.')[0]
    # # print(image_name)
    # im.save(f"madiee-{image_name}.webp", 'webp')


# for image in images:
#     image_name = image.split('.')[0]
