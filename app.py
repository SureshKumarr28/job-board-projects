from flask import Flask, render_template, request
import boto3
from botocore.exceptions import NoCredentialsError

# Initialize Flask application
app = Flask(__name__)

# AWS S3 configurations
S3_BUCKET_NAME = 'your_s3_bucket_name'
AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'

# Initialize S3 client
s3_client = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply')
def apply():
    return render_template('application_form.html')

@app.route('/submit_application', methods=['POST'])
def submit_application():
    try:
        # Get form data
        fullName = request.form['fullName']
        email = request.form['email']
        resume = request.files['resume']

        # Upload resume file to S3 bucket
        s3_client.upload_fileobj(resume, S3_BUCKET_NAME, f'{fullName}_resume.pdf')

        # Store applicant details as text in S3
        applicant_details = f'Full Name: {fullName}\nEmail: {email}\n'
        s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=f'{fullName}_details.txt', Body=applicant_details)

        return 'Application submitted successfully!'
    except NoCredentialsError:
        return 'AWS credentials not available. Unable to submit application.', 500
    except Exception as e:
        return f'Error submitting application: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
