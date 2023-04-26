# Data-Ingestion-Application

## Architecture
![image](https://user-images.githubusercontent.com/128548207/234573450-0b862959-4913-4990-adaa-0cf230dc9912.png)


## STEPS
A.	STEP-1: Create S3 bucket required to upload files downloaded from Gharchive.org

B.	STEP-2: Create two DynamoDB tables “jobs” and “job_run_details.” - Pull notebook files to create DynamoDB Tables

C.	STEP-3: Develop Python code and Zip it as git-aws.zip - Pull Code from app folder and from util folder and zip it.

D.	STEP-4: Upload code as zip file  “git-aws.zip” to S3 bucket under code folder.

E.	STEP-5: Create Lambda function - gitaws-ingestor - Use AWS Management console.

F.	STEP-6: Create Event Bridge Schedular to schedule and automate Ingestion process - Use AWS Management console.


## Features

### S3

![image](https://user-images.githubusercontent.com/128548207/234573787-e9d28bf9-644c-4d1d-ba42-918be3c7277e.png)

### DynamoDB

![image](https://user-images.githubusercontent.com/128548207/234574073-93d32546-2f60-4470-90d0-3feeaa6198fe.png)

### Lambda Function

![image](https://user-images.githubusercontent.com/128548207/234574376-1fc92e9a-3cde-4152-9792-71fb0ef4d74e.png)

### Event Bridge

![image](https://user-images.githubusercontent.com/128548207/234574625-82c1f2d9-137a-4d2c-9a24-360782aa04c0.png)

Set Target as Lambda function :-
![image](https://user-images.githubusercontent.com/128548207/234574782-20f0f583-109c-4775-bf6c-03a906b78fbf.png)

### CloudWatch

![image](https://user-images.githubusercontent.com/128548207/234574998-c180fc9c-c722-4587-8e76-7a1666578898.png)

CloudWatch Log streams to monitor/validate automated lambda function triggered through Event Bridge schedules of every 15 mins
![image](https://user-images.githubusercontent.com/128548207/234575085-e3f84aad-e37e-4610-b930-12cdfa1e6a5d.png)


