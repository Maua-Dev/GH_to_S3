import os
import shutil

def build():

    repo_name = 'upload'

    create_venv= "python -m venv venv;"

    activate_venv= "source venv/bin/activate;"

    install_requirements= "pip install -r lambda_function/requirements.txt;"

    create_dir_upload = f"mkdir {repo_name};"

    copy_to_site_packages = "cp lambda_function/gh_to_s3.py venv/lib/python3.8/site-packages;"

    os.system(f"{create_venv} {activate_venv} {install_requirements} {create_dir_upload} {copy_to_site_packages}")

    #zip venv\lib\site-packages to upload\function.zip
    shutil.make_archive("upload/function", "zip", "venv/lib/python3.8/site-packages") 

    return repo_name
