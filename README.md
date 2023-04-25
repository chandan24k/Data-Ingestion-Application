### Data-Ingestion-Application

# Features
A.	STEP-1: Create S3 bucket required to upload files downloaded from Gharchive.org

B.	STEP-2: Create two DynamoDB tables “jobs” and “job_run_details.” - Pull notebook files to create DynamoDB Tables

C.	STEP-3: Develop Python code as below and Zip it as git-aws.zip - Pull Code from app folder and from util folder

D.	STEP-4: Upload code as zip file  “git-aws.zip” to S3 bucket under code folder.

E.	STEP-5: Create Lambda function - gitaws-ingestor

F.	STEP-6: Create Event Bridge Schedular to schedule and automate Ingestion process
