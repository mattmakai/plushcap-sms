# -*- coding: utf-8 -*-
import sys
import time

import requests
from twilio.rest import TwilioRestClient

from plushutils import get_env_setting

CONNECTION_ERROR = -100

responses = {CONNECTION_ERROR: "is down or did not respond to the request.",
             200: "is online and returning 200 OK.",
             403: "is online but is denying the request due to lack of " + \
                  "permission.",
             404: "is online but the webpage at that URL was not found.",
             500: "is online but returning an internal server error.",
}

def contact_url(url):
    """
        Attempts to access the URL specified as a parameter. Returns the
        status code and the content for the request once it is complete.
    """
    try:
        response = requests.get(url)
        return response.status_code, response.content
    except requests.exceptions.ConnectionError:
        return CONNECTION_ERROR, ""


def check_url(url, twilio_client, twilio_from_number, alert_number, 
    frequency=60):
    """
        Loops in a separate thread checking a given URL. Sends a notification
        if the website goes down, 500 errors or gives a 404.
    """
    while True:
        status_code, content = contact_url(url)
        if status_code != 200:
            # alert time
            send_alert(url, status_code, twilio_client, twilio_from_number, 
                alert_number)
        time.sleep(60)


def send_alert(url, status_code, twilio_client, twilio_from_number, 
    alert_number):
    """
        Sends an SMS alert to a phone number with the current status code
        of the URL.
    """
    if responses.has_key(status_code):
        message = ("The server at %s " + responses[status_code]) % url
    else:
        message = ("Alert: status code received from %s is %i " + \
                   "instead of 200 OK.") % (sys.argv[1], status_code)
    twilio_client.messages.create(to=alert_number, from_=twilio_from_number,
        body=message)
            

def monitor(url, frequency=60, twilio_account_sid=None, twilio_auth_token=None,
            twilio_from_number=None, alert_number=None):
    """
        Monitors the given URL. Default frequency is once a minute. Twilio 
        account SID and auth token are required for notifications and will be 
        pulled from the environment variables TWILIO_ACCOUNT_SID and 
        TWILIO_AUTH_TOKEN if not specified.
    """
    if not twilio_account_sid or not twilio_auth_token:
        # initialize with environment vars instead of function parameters
        twilio_client = TwilioRestClient()
    else:
        twilio_client = TwilioRestClient(twilio_account_sid, twilio_auth_token)
    if not twilio_from_number:
        twilio_from_number = get_env_setting('TWILIO_FROM_NUMBER')
    if not alert_number:
        alert_number = get_env_setting('ALERT_NUMBER')
    check_url(url, twilio_client, twilio_from_number, alert_number, frequency)


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("usage: python plushcap.py http://test.url/")
        print("also ensure that TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, " + \
              "TWILIO_FROM_NUMBER\nand ALERT_NUMBER are set as " + \
              "environment variables")
    else:
        url = sys.argv[1]
        status_code, content = monitor(url)
        if responses.has_key(status_code):
            print(("The server at %s " + responses[status_code]) % url)
        else:
            print("Alert: status code received from %s is %i instead of " + \
                  "200 OK." % (sys.argv[1], status_code))
