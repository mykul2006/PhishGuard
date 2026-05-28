# PhishGuard
Cybersecurity project for detecting phishing emails and malicious URLs using heuristic analysis and threat scoring.

## Features

- Detects phishing keywords in emails
- Analyzes suspicious URLs
- Calculates threat scores
- Web interface using Streamlit

## Technologies Used

- Python
- Streamlit
- tldextract

## Project Structure

PhishGuard/

app.py
email_analyzer.py
url_analyzer.py
risk_engine.py

## Example Detection

Email:
URGENT! Verify now.

URL:
https://paypal-login-secure.xyz

Output:
Threat Score: 55

Warnings:
- urgent
- verify now
- Suspicious TLD

## How to Run

```bash
streamlit run app.py
