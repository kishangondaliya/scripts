
import os, os.path, shutil,sys
import io
from PIL import Image

opath = '/path/to/kitti/dataset'

folder_path = opath + "image_2/"
images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
f = open(opath +'aspect.txt' , 'a')


def calculate_aspect(width: int, height: int) -> str:
    temp = 0

    def gcd(a, b):
        """The GCD (greatest common divisor) is the highest number that evenly divides both width and height."""
        return a if b == 0 else gcd(b, a % b)

    if width == height:
        return 1, 1

    if width < height:
        temp = width
        width = height
        height = temp

    divisor = gcd(width, height)

    x = int(width / divisor) if not temp else int(height / divisor)
    y = int(height / divisor) if not temp else int(width / divisor)

    return x, y



for image in images:
    path = folder_path+image
    img = Image.open(path)
    w = img.size[0]
    h = img.size[1]
    x, y = calculate_aspect(w, h)
    divi = float(x)/float(y)
    if divi < 0.50 or divi > 2.7:
        name = image[:-3]
        kitti_path = 'label_2_kitti/' + name + 'txt'
        voc_path = 'label_2_voc/' + name + 'xml'
        #shutil.move(path, opath + 'trash/image_2/' + image)
        #shutil.move(opath + kitti_path, opath + 'trash/' + kitti_path)
        #shutil.move(opath + voc_path, opath + 'trash/' + voc_path)

        f.write(image + '\n')
        #f.write(image + " width: " + str(w) + " height: " + str(h) + " aspect ratio: " + str(x)+":"+str(y) + " divisor: "+ str(divi) + "\n")
