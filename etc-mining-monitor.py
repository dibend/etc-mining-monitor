import requests
import matplotlib.pyplot as plt
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import config  # Import the configuration settings

# Style for the plot
plt.style.use("bmh")
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['figure.dpi'] = 200

# Fetch the crypto mining payment data
response = requests.get(config.API_URL)
data = response.json()

# Process the data
amounts_and_timestamps = [
    (payment['amount'] / 1e9, datetime.fromtimestamp(payment['timestamp']))
    for payment in data['payments']
]

# Extract the amounts and timestamps into separate lists
amounts, timestamps = zip(*amounts_and_timestamps)

# Plot the amounts against the timestamps
plt.scatter(timestamps, amounts, c='green', edgecolors='black')
plt.title("Crypto Mining Payment Amounts Over Time")
plt.xlabel("Date")
plt.ylabel("Amount in ETC")
plt.xticks(rotation=45)

# Save the plot to a BytesIO object
buf = BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
plt.close()

# Create an HTML email message with an embedded image
msg = MIMEMultipart('related')
msg['Subject'] = 'Crypto Mining Payments'
msg['From'] = config.SENDER_EMAIL
msg['To'] = config.RECIPIENT_EMAIL

# Attach the plot image
msg.attach(MIMEText('<img style="max-width: 75%;" src="cid:image1">', 'html'))
img = MIMEImage(buf.read(), 'png')
img.add_header('Content-ID', '<image1>')
msg.attach(img)

# Send the email via SMTP
with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
    server.starttls()
    server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
    server.sendmail(config.SENDER_EMAIL, config.RECIPIENT_EMAIL, msg.as_string())

print("Email sent successfully!")
