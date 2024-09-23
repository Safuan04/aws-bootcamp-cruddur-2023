from dotenv import load_dotenv
import os

load_dotenv()  # This will load the .env file

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_default_region = os.getenv('AWS_DEFAULT_REGION')
safuan = os.getenv('safuan')

print(aws_access_key_id, aws_secret_access_key, aws_default_region, safuan)

