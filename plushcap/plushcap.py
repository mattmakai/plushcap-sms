# -*- coding: utf-8 -*-
import sys
import requests

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


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("usage: python plushcap.py http://test.url/")
    else:
        status_code, content = contact_url(url=sys.argv[1])
        if responses.has_key(status_code):
            print(("The server at %s " + responses[status_code]) % sys.argv[1])
        else:
            print("Server response was unknown, status code: " + status_code)
