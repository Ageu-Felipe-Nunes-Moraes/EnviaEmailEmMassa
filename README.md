# Email Sender

This is a Python script for sending emails using the `smtplib` library. It is useful for sending personalized messages with attachments to multiple recipients from a list.

## Features

- **Personalized Email Sending:** The script allows sending emails with personalized HTML messages to specific recipients.
- **Attachments:** It is possible to add attachments to the emails, such as PDF documents.
- **Signature Image:** Adds a signature image to the email.
- **Reading Email List:** The script reads a list of emails from a text file to send emails to multiple recipients.

## Installation Requirements

- Python 3.x

## Required Libraries

- `smtplib`: For sending emails via the SMTP protocol.
- `os`: To interact with the operating system and manage files.
- `email.mime`: To construct the parts of the email message.
- `email.encoders`: To encode the attachments in base64.

## How to Use

1. Ensure you have Python installed on your system.
2. Edit the script and enter the necessary information, such as subject, sender, password, email body, and the path to the email list file.
3. Run the script.
4. Wait for the emails to be sent to the recipients.

## How to Contribute

If you wish to contribute to this script, feel free to fork the repository, make your modifications, and submit a pull request.

## Author

This script was developed by Ageu Felipe Nunes Moraes. For questions or suggestions, contact [ageumoraes67@gmail.com](mailto:ageumoraes67@gmail.com).

## Disclaimer

This script is for educational purposes only and has no affiliation with email services or other mentioned companies.
