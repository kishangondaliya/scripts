import os
import shutil
import glob

# Give parent folder of all sub folders and only keep those folders which needs to be copied
diro = '/path/to/images/and/annotations'

dst_dir_img = "/path/to/images"
dst_dir_anot = "/path/to/anots"

for x in os.listdir(diro):
	print x
	src_dir = os.path.join(diro, x)
	for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
	    shutil.copy(jpgfile, dst_dir_img)
	for txtfile in glob.iglob(os.path.join(src_dir, "*.txt")):
	    shutil.copy(txtfile, dst_dir_anot)
