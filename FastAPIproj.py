from fastapi import FastAPI 
from fourthsept import get_system_info
import boto3 #this change was made on 10th sepetember

s3 = boto3.resource('s3')#this one was made on 10/9/26 too

app=FastAPI(title ="DevOPS utilities API")
@app.get("/hello")
def hello():
    return{"message":"Welcome to the first day of making my DevOPS utilities API"}

@app.get("/metrics")
def metrics():
    """
    This function displays
    system metrics
    """
    return get_system_info()

@app.get("/aws/s3")  # Creates a GET endpoint to retrieve all S3 buckets
def get_buckets():
    buckets = []  # Creates an empty list to store bucket names
    
    for bucket in s3.buckets.all():  # Iterates through all S3 buckets in the AWS account
        buckets.append(bucket.name)  # Adds each bucket's name to the list
    
    return buckets  # Returns the list of bucket names as the API response