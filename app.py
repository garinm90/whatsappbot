import os
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

print(ACCOUNT_SID)
print(AUTH_TOKEN)