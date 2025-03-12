import logging
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
This script provides a pattern for monitoring log messages and sending email alerts
for critical errors and failed jobs.

Key Features:
- Configuring logging to capture critical errors
- Sending email alerts for issues detected in log files
- Customizing email content with error summaries
"""

# 1. Configure Logging
LOG_FILE = "app.log"
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),  # Save logs to a file
        logging.StreamHandler()  # Print logs to console
    ]
)
logger = logging.getLogger("ErrorMonitor")

# 2. Function to Check Logs for Critical Errors
def check_logs_for_errors(log_file):
    """Scans the log file for critical errors and returns a summary."""
    if not os.path.exists(log_file):
        return "No log file found."
    
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    error_messages = [line for line in lines if "CRITICAL" in line or "ERROR" in line]
    return "\n".join(error_messages) if error_messages else "No critical errors detected."

# 3. Function to Send Email Alerts
def send_email_alert(subject, body, recipient_email, sender_email, sender_password):
    """Sends an email with the provided subject and body."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email alert sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# 4. Example Usage (Uncomment to run)
# logger.info("This is an info message")
# logger.error("This is an error message")
# logger.critical("This is a critical error!")

# error_summary = check_logs_for_errors(LOG_FILE)
# if "CRITICAL" in error_summary or "ERROR" in error_summary:
#     send_email_alert("Log Alert: Critical Errors Detected", error_summary, "recipient@example.com", "your_email@gmail.com", "your_password")

