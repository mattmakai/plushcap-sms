# -*- coding: utf-8 -*-
import requests
import sys

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


def check_url(url, frequency=60):
    """
        Loops in a separate thread checking a given URL. Sends a notification
        if the website goes down, 500 errors or gives a 404.
    """
    while True:
        time.sleep(60)
        status_code, content = contact_url(url)
        if status_code != 200:
            # alert time
            pass


def monitor(url, frequency=60, twilio_account_sid="", twilio_auth_token=""):
    """
        Monitors the given URL. Default frequency is once a minute. Twilio account
        SID and auth token are required for notifications and will be pulled from
        the environment variables TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN if not
        specified.
    """
    check_url(url, frequency)


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("usage: python plushcap.py http://test.url/")
    else:
        status_code, content = contact_url(url=sys.argv[1])
        if responses.has_key(status_code):
            print(("The server at %s " + responses[status_code]) % sys.argv[1])
        else:
            print("Server response was unknown, status code: " + status_code)
