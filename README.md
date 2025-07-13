# WhatsApp Link Analyzer Bot

A WhatsApp bot that checks if a link sent by users is safe, suspicious, or known to be malicious/phishing. The bot uses Google Safe Browsing and can be extended with other APIs like VirusTotal. Built with Python (Flask) and deployed on Render.

---

## Features

- Users send a URL/link to the bot via WhatsApp.
- The bot analyzes the link using Google Safe Browsing.
- It replies with a verdict: **Safe, Suspicious, or Dangerous**, a confidence level, and a brief explanation.
- Fully automated, no manual intervention needed.

---

## Tech Stack

- **Backend:** Python 3, Flask
- **Messaging:** Twilio WhatsApp Sandbox API
- **Security Analysis:** Google Safe Browsing API
- **Deployment:** [Render.com](https://render.com/)
- **(Optional)**: Extend with VirusTotal, urlscan.io, or custom ML models.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/whatsapp-link-analyzer.git
cd whatsapp-link-analyzer
````

### 2. Install dependencies

It’s recommended to use a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in your project root with:

```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886    # or your Twilio WhatsApp number
GOOGLE_SAFE_BROWSING_KEY=your_google_safe_browsing_api_key
```

> **Note:** On Render or other cloud platforms, set these as environment variables in the dashboard, not in a `.env` file.

---

### 4. Run Locally

```bash
python app.py
```

The server will run on `http://localhost:5000` by default.

To expose your local server for Twilio, use [ngrok](https://ngrok.com/):

```bash
ngrok http 5000
```

---

### 5. Connect to Twilio WhatsApp Sandbox

* Join the Twilio WhatsApp Sandbox by following instructions on [Twilio Console](https://www.twilio.com/console/sms/whatsapp/sandbox).
* Set your webhook URL to `https://<your-ngrok-or-cloud-url>/webhook`.

---

### 6. Deploy to Render

1. Push your code to GitHub.
2. Create a new **Web Service** on [Render.com](https://render.com/), connect your repo.
3. Set your environment variables in Render dashboard.
4. Deploy! Your app will be publicly available at `https://your-app.onrender.com`.
5. Update your Twilio webhook URL to this new address.

---

## Project Structure

```
.
├── app.py
├── requirements.txt
├── Procfile
├── README.md
└── (other files)
```

---

## Usage

1. Send a WhatsApp message containing a link to your Twilio sandbox number.
2. The bot will reply with the analysis result (safe, suspicious, dangerous).

---

## Customization

* **Add more checks**: Integrate with VirusTotal, urlscan.io, or build your own heuristics in `app.py`.
* **Logging/reporting**: Use MongoDB or Firebase to store analysis logs.
* **Admin dashboard**: Build with Flask/React for visualizing flagged/scanned URLs.

---

## Security Notes

* All input is sanitized before analysis.
* No user data is stored without consent.
* API calls are made securely.
* Rate-limiting is recommended for production deployments.

---

## License

MIT (or specify your own).

---

## Author

Ashin Kuniyil

---

## Credits

* [Flask](https://flask.palletsprojects.com/)
* [Twilio](https://www.twilio.com/)
* [Google Safe Browsing](https://developers.google.com/safe-browsing/v4)