Making my first lambda in AWS to automatically generate subtasks to a specific parent task in Asana when files are added to our S3 bucket.


## What I want this to do
1. Trigger an action upon a file being uploaded
2. Read the file metadata
3. Generate a POST request to create a subtask in Asana
4. Direct this task to a specific parent task in Asana


## Technologies used
AWS Lambda
Asana 
Python SDK