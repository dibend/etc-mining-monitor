# Crypto Mining Payments Notification

This project fetches crypto mining payment data, plots the payment amounts over time, and sends an email notification with the plot attached.

## Prerequisites

- Python 3.x
- `requests` library
- `matplotlib` library
- `smtplib` library

You can install the required Python packages using pip:

```bash
pip install requests matplotlib
```

## Configuration

Create a configuration file named `config.py` in the project directory. This file will contain all the sensitive information required for the script.

### Example `config.py`

```python
# config.py

API_URL = "https://example.com/api/accounts/your_account_id"
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = 587
SMTP_USERNAME = 'your_smtp_username'
SMTP_PASSWORD = 'your_smtp_password'
SENDER_EMAIL = 'Your Name <your_email@example.com>'
RECIPIENT_EMAIL = 'recipient_email@example.com'
```

### Setting Up Your Own `config.py`

1. **API URL**: 
   - Replace `https://example.com/api/accounts/your_account_id` with the URL from which you want to fetch the crypto mining payment data.

2. **SMTP Server**:
   - You need an SMTP server to send emails. Common options include:
     - **Amazon SES**: Sign up at [Amazon SES](https://aws.amazon.com/ses/) and follow the documentation to get your SMTP credentials.
     - **Gmail SMTP**: Use Gmail's SMTP server. Refer to the [Gmail SMTP documentation](https://support.google.com/a/answer/176600?hl=en) for setup instructions.

3. **SMTP Credentials**:
   - Replace `your_smtp_username` and `your_smtp_password` with your actual SMTP username and password. For Amazon SES, refer to the [Amazon SES documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html).

4. **Email Addresses**:
   - `SENDER_EMAIL`: The email address that will appear as the sender. Ensure that this email is verified with your SMTP service if required.
   - `RECIPIENT_EMAIL`: The email address that will receive the notification. You can add multiple recipients by separating them with commas.

### Compatible Email Services

- **Amazon SES**: [Amazon SES](https://aws.amazon.com/ses/) offers a reliable, scalable, and inexpensive email service. Ensure you have set up and verified your sender email address.
- **Gmail SMTP**: If you prefer using Gmail, you can use Gmail's SMTP server. Refer to the [Gmail SMTP documentation](https://support.google.com/a/answer/176600?hl=en) for setup instructions.

## Usage

Run the script to fetch the data, create the plot, and send the email:

```bash
python script.py
```

## Script

The main script (`script.py`) performs the following steps:
1. Fetches the crypto mining payment data from the specified API.
2. Processes the data to extract payment amounts and timestamps.
3. Creates a scatter plot of the payment amounts over time.
4. Embeds the plot in an HTML email.
5. Sends the email using the specified SMTP server.
```

This `README.md` provides detailed instructions, an example `config.py` with placeholders, and guidance on how to set up and use the script.
