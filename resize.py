# Author: Kishan Go.

import os
import cv2
import sys
import glob
import argparse

def resize(root, width, height):
    root = os.path.abspath(root)
    img_path = os.path.join(root, "image_2")
    resize_img_path = os.path.join(root, "image_2_resize")
    anot_path = os.path.join(root, "label_2")
    resize_anot_path = os.path.join(root, "label_2_resize")
    
    IMAGE_WIDTH = width
    IMAGE_HEIGHT = height
    
    if not os.path.exists(img_path):
        raise Exception("Image folder not found, expected \"image_2\"")
    if not os.path.exists(anot_path):
        raise Exception("Annotation folder not found, expected \"label_2\"")
    
    if not os.path.exists(resize_img_path):
        os.makedirs(resize_img_path)
    if not os.path.exists(resize_anot_path):
        os.makedirs(resize_anot_path)
    
    for img in os.listdir(img_path):
    
        # Image read
        im = cv2.imread(os.path.join(img_path, img))
    
        # Get scales
        orig_h, orig_w, _ = [float(v) for v in im.shape]
        x_scale = IMAGE_WIDTH/orig_w
        y_scale = IMAGE_HEIGHT/orig_h
    
        # Image resize and save
        im = cv2.resize(im, (IMAGE_WIDTH, IMAGE_HEIGHT), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(resize_img_path, img), im)
    
        # read anot
        anot = img[:-3] + 'txt'
        f = open(os.path.join(anot_path, anot), "r")
        lines = f.readlines()
        f.close()
    
        # Get bboxes
        bboxs = []
        for i, line in enumerate(lines):
           lines[i] = line.strip().split(' ')
           bboxs.append(map(float, lines[i][4:8]))
            
        # Apply scales and save anot
        f = open(os.path.join(resize_anot_path, anot), 'w')
    
        for i, line in enumerate(lines):
            tmp = bboxs[i][0]*x_scale
            lines[i][4] = tmp if tmp <= IMAGE_WIDTH else IMAGE_WIDTH

            tmp = bboxs[i][2]*x_scale
            lines[i][6] = tmp if tmp <= IMAGE_WIDTH else IMAGE_WIDTH

            tmp = bboxs[i][1]*y_scale
            lines[i][5] = tmp if tmp <= IMAGE_HEIGHT else IMAGE_HEIGHT

            tmp = bboxs[i][3]*y_scale
            lines[i][7] = tmp if tmp <= IMAGE_HEIGHT else IMAGE_HEIGHT
            for j, _ in enumerate(lines[i]):
                lines[i][j] = str(lines[i][j])
            f.write(' '.join(lines[i]) + '\n')
    
        f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, required=True, default="", help="Dataset directory which contents KITTI format dataset, having folder \"image_2\" and \"label_2\"")
    parser.add_argument("--w", type=int, required=True, default=224, help="Image width")
    parser.add_argument("--h", type=int, required=True, default=224, help="Image height")
    args = parser.parse_args()
    resize(args.dir, args.w, args.h)
