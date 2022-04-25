import os
import shutil

def build():
    #create a venv
    #install requirements
    #create dir upload
    #copy gh_to_s3 to venv\lib\site-packages
    #zip venv\lib\site-packages to upload\function.zip
    #return "upload"

    #create venv
    os.system("python3 -m venv venv")

    #activate venv
    os.system("source venv/bin/activate")

    #install requirements
    os.system("pip install -r lambda_function/requirements.txt")

    #create dir upload
    os.system("mkdir upload")

    #copy gh_to_s3 to venv\lib\site-packages
    os.system("cp gh_to_s3.py venv/lib/python3.6/site-packages/")

    #zip venv\lib\site-packages to upload\function.zip
    shutil.make_archive("upload/function", "zip", "venv/lib/python3.6/site-packages") 

    return "upload"

