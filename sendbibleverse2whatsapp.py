import pywhatkit as kit
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Get the phone number from the environment variable
phone_number = os.getenv("PHONE_NUMBER")
# Send a WhatsApp message to a specific number
phone_number = "+6472340101"  # replace with the recipient's phone number
message = "Hello World"

# Schedule the message to be sent in 1 minute from now
kit.sendwhatmsg(phone_number, message, 22, 30)  # replace 22, 30 with the desired time (hour, minute)s