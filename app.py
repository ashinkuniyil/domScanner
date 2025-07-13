from flask import Flask, request
import os
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
import re
import validators
import requests

load_dotenv()
app = Flask(__name__)

def extract_url(text):
    # Basic regex for URLs
    url_regex = r'(https?://[^\s]+)'
    matches = re.findall(url_regex, text)
    if matches:
        url = matches[0]
        if validators.url(url):
            return url
    return None


def check_safe_browsing(url):
    key = os.getenv('GOOGLE_SAFE_BROWSING_KEY')
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={key}"
    payload = {
        "client": {
            "clientId": "yourcompany",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["THREAT_TYPE_UNSPECIFIED", "MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    resp = requests.post(endpoint, json=payload)
    if resp.status_code == 200:
        result = resp.json()
        if 'matches' in result:
            return False, "Google Safe Browsing flagged this URL as dangerous."
        else:
            return True, "No issues found by Google Safe Browsing."
    return None, "Safe Browsing check failed."


# @app.route('/webhook', methods=['POST'])
# def whatsapp_webhook():
#     incoming_msg = request.values.get('Body', '').strip()
#     print(f"Received: {incoming_msg}")   # This will show in your terminal!
#     return "Webhook received!", 200

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()
    url = extract_url(incoming_msg)
    if url:
        safe, reason = check_safe_browsing(url)
        if safe is None:
            msg.body("Could not check the link right now. Try again later.")
        elif safe:
            msg.body(f"✅ Link appears safe.\nReason: {reason}")
        else:
            msg.body(f"⚠️ Warning! This link is potentially dangerous.\nReason: {reason}")
    else:
        msg.body("Please send a valid link (starting with http or https).")
    return str(resp)

@app.route('/')
def home():
    return "WhatsApp Bot is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
