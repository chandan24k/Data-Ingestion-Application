import os
from util.bookmark import get_job_details, \
    get_next_file_name, save_job_run_details
    
from gitaws_ingest import upload_file_to_s3


def gitaws_ingest_to_s3():
    bucket_name = os.environ.get('BUCKET_NAME')
    folder = os.environ.get('FOLDER')
    job_details = get_job_details('gitaws_ingest')
    job_start_time, next_file = get_next_file_name(job_details)
    job_run_details = upload_file_to_s3(next_file, bucket_name, folder)
    save_job_run_details(job_details, job_run_details, job_start_time)
    return job_run_details


def lambda_ingest(event, context):
    job_run_details = gitaws_ingest_to_s3()

    return {
        'status': 200,
        'body': job_run_details
    }