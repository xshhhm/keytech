#!/usr/bin/env python  
# encoding=utf-8
  
# os.walk()��ʹ��  
import os  
import sys  
# ö��dirPathĿ¼�µ������ļ�  
  
def main(path):  
#begin  
    fileDir =  path
    idx = 0
    for a in os.walk(fileDir):  
    #begin  
        print(idx, a[0], a[1], a[2])  
        idx += 1
    #end  
    os.system("pause")  
#end  

def main2(path):  
#begin  
    fileDir = path
    for root, dirs, files in os.walk(fileDir):  
    #begin  
        #for dir in dirs:  
        #begin  
        #   print(os.path.join(root, dir))  
        #end  
        for file in files:  
        #begin  
            print(os.path.join(root, file))  
        #end  
    #end  
    os.system("pause")  
#end  
  
if __name__ == '__main__':  
#begin  
    main2(sys.argv[1])  
#end  