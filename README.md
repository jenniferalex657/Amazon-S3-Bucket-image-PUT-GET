S3 Image Upload & Download (Python)  

This project shows how to upload and download an image using AWS S3 and Python (boto3).  

⸻

Files  

image.jpg        _# Image to upload_  
upload.py        _# Uploads image to S3_  
download.py     _ # Downloads image from S3_  

⸻

Setup (One-Time)  
	1.	Create an AWS account  
	2.	Create an S3 bucket  
	3.	Create an IAM user with S3 permissions  
	4.	Configure AWS locally:  
          aws configure  
  5. Install dependencies:  
          python3 -m pip install boto3 awscli  


⸻

Upload Image  

python3 upload.py  


⸻

Download Image  

python3 download.py  


⸻

How to Know It Worked  
	•	No AWS permission errors   
	•	Image appears in S3 bucket  
	•	Image downloads back locally  

⸻

Purpose  

This project demonstrates basic cloud storage operations using Python and AWS S3.  
