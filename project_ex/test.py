import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

pwd = os.getenv('password')
print ("Password: ", pwd)

from mathcalc import add


