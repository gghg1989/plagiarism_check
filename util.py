import os
import tarfile
import glob
import shutil
from os import path
import csv

def extract():
    submissions_path = 'submissions/'
    extracted_path = "submissions/"
    counter = 0
    students_dir = os.listdir(submissions_path)
    for f in students_dir:
        if not f.endswith('.tar.gz'):
            print(f+" is not a .tar.gz file. Skip!")
            continue
        print("extracting:" + f)
        name = f.split('_')[0]
        if not os.path.isdir(extracted_path+name):
            os.mkdir(extracted_path+name)
        file = submissions_path + f
        with tarfile.open(file) as tf:
            tf.extractall(extracted_path+name)
        counter += 1

def rename(file_name):
    counter = 0
    renamed = 0
    submissions_path = 'submissions/'
    students_dir = os.listdir(submissions_path)
    for d in students_dir:
        counter += 1
        if not path.exists(submissions_path+d+'/'+file_name):
            if path.exists(submissions_path+d+'/seqcircuit.c'):
                shutil.copyfile(submissions_path+d+'/seqcircuit.c', submissions_path+d+'/hw5/'+file_name)
                renamed += 1
        print(d + "is processed.")
    print(str(counter) + "is processed, " + str(renamed) + "is renamed.")

def strip_hw_dir():
    submissions_path = 'submissions/'
    students_dir = os.listdir(submissions_path)
    for d in students_dir:
        student_hw_path = submissions_path+'/'+d+'/'
        if not os.path.isdir(student_hw_path):
            continue
        destination_path = submissions_path+'/'+d+'/'
        files = os.listdir(student_hw_path)
        for f in files:
            if str(f) == '':
                continue
            # print(f)
            shutil.move(student_hw_path+f, destination_path+f)
        if os.path.isdir(student_hw_path):
            shutil.rmtree(student_hw_path)

def group_files(file_name):
    submissions_path = 'submissions/'
    output_path = 'output/' + file_name + '/'
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    students_dir = os.listdir(submissions_path)
    for d in students_dir:
        student_hw_path = submissions_path+'/'+d+'/'
        # target_path = output_path + d + '/'
        # if not os.path.isdir(target_path):
        #     os.mkdir(target_path)
        if path.exists(student_hw_path+file_name):
            shutil.copyfile(student_hw_path+file_name, output_path+file_name[:-1]+d+'.c')