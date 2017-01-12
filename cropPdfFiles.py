#coding=utf-8
import sys
import os
output_dir="C:\\Users\\kirchhoff\\Desktop\\finished-pdfs\\"
input_dir="C:\\Users\\kirchhoff\\Desktop\\unproecessed-pdfs\\"
briss_path="C:\\Users\\kirchhoff\\PycharmProjects\\test\\briss-0.9\\briss-0.9.jar"
for filename in os.listdir(input_dir):
    os.system("java -jar %s -s %s -d %s" % (briss_path, input_dir+filename,output_dir+filename[:-4]+"-cropped.pdf"))
print "all done!!!"