# This python3 script will generate random # of objects from given directory.
# i.e. Get 10 random images from bunch of 500 image-set.
# Useful to get test images from dataset

# Author: Kishan Go.

import os
import random
import argparse
import shutil




def main(root, n):
    root = os.path.abspath(root)
    root_n = root + '_' + str(n)

    if not os.path.exists(root_n):
        os.makedirs(root_n)

    obj_list = os.listdir(root)
    obj_len = len(obj_list)
    assert (obj_len >= n), "Less objects found in object directory!"

    f = open(root_n + '.txt', 'w')
    for i in random.sample(range(0, obj_len), n):
        f.write(obj_list[i] + '\n')
        shutil.copy(os.path.join(root, obj_list[i]), os.path.join(root_n, obj_list[i]))

    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, required=True, default="", help="Objects directory")
    parser.add_argument("--n", type=int, required=True, help="Number of random objects to get")
    args = parser.parse_args()
    main(args.dir, args.n)
