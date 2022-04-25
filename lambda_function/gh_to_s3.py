

from git import Repo

import os


def lambda_handler(event, context):
    # Clone repo from github
    Repo.clone_from(event['git_url'], './repo')

    # Run file to build the project
    import repo.build as build

    #Fazer a funcao de build retornar o path do diretorio
    upload_dir = build.build()


    # Upload the project to S3
    upload_s3_string = f"aws s3 cp ./repo/{upload_dir} s3://{event['bucket_name']}/{upload_dir}/ --recursive"
    try:
        os.system(upload_s3_string)
    except Exception as e:
        print(e)

