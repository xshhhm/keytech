# -*- coding:utf-8 -*-
import re
import os
import os.path
import time
import sys


def change_name(path):
    i = 0
    for root, dirs, files in os.walk(path):
        root_split = root.split("/")
        ren_ext = ""
        if len(root_split) == 2:
            print root_split
            if root_split[-1] == "pos":
                ren_ext = "pos"
            elif root_split[-1] == "neg":
                ren_ext = "neg"
            else:
                ren_ext = ""
            print ren_ext
        for img in files:
            img_ext = ['bmp','jpeg','gif','psd','png','jpg', 'JPG', 'BMP', 'PNG']
            split_name = img.split('.')
            file_ext = split_name[-1]
            img_len = len(img)
            file_ext_len = len(file_ext)
            img_name = img[0:img_len-file_ext_len-1]
            if file_ext in img_ext:
                new_name = root + "/" + str(i) + "_" + ren_ext+ "."+file_ext
                old_name = root + "/" + img
                print old_name, new_name
                os.rename(old_name, new_name)
                #print root, dirs, img
                i+= 1
    print i

if __name__ == "__main__":
    img_dir = sys.argv[1]
    img_dir = img_dir.replace('\\','/')
    
    start = time.time()
    change_name(img_dir)
    c = time.time() - start

    print('%0.2f'%(c))
