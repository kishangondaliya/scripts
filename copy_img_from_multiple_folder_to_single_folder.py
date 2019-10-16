#
# Script copies all .jpg files from multiple directories to single directory
# Ideal usecase: Copy COCO type dataset to use as Kitti
#

import os
import shutil
import glob


diro = '/path/to/source/folder/containing/multiple/folders'

dst_dir = "/path/to/destination/folder"

for x in os.listdir(diro):
	print x
	src_dir = os.path.join(diro, x)
	for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
	    shutil.copy(jpgfile, dst_dir)
