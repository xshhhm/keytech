# -*- coding:utf-8 -*-
import re
import os
import os.path
import time
import sys


def change_name(path):
    dst = file(sys.argv[2], 'w')
    i = 0
    for root, dirs, files in os.walk(path):
        root_split = root.split("/")
        ren_ext = ""
        label = -1
        if len(root_split) == 2:
            print root_split
            if root_split[-1] == "pos":
                ren_ext = "pos"
                label = 1
            elif root_split[-1] == "neg":
                ren_ext = "neg"
                label = 0
            else:
                ren_ext = ""
                label = -1
            print ren_ext
        for img in files:
            img_ext = ['bmp','jpeg','gif','psd','png','jpg', 'JPG', 'BMP', 'PNG']
            split_name = img.split('.')
            file_ext = split_name[-1]
            img_len = len(img)
            file_ext_len = len(file_ext)
            img_name = img[0:img_len-file_ext_len-1]
            if file_ext in img_ext:
                old_name = root_split[-1] + "/" + img
                print old_name
                dst.write(old_name)
                dst.write(" ")
                dst.write(str(label))
                dst.write("\n")
                #print root, dirs, img
                i+= 1
    print i
    dst.close()

if __name__ == "__main__":
    img_dir = sys.argv[1]
    img_dir = img_dir.replace('\\','/')
    
    start = time.time()
    change_name(img_dir)
    c = time.time() - start

    print('%0.2f'%(c))
