# -*- coding: utf-8 -*-
import sys
import requests

HTTP_OK = 200
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500

def contact_url(url):
    """
        Attempts to access the URL specified as a parameter. Returns the
        status code and the content for the request once it is complete.
    """
    try:
        response = requests.get(url)
        return response.status_code, response.content
    except requests.exceptions.ConnectionError:
        return 404, ""

def handle_response(status_code):
    if status_code == HTTP_OK:
        return '%s is online and returning 200 OK' % sys.argv[1]
    elif status_code == HTTP_FORBIDDEN:
        return 'Unable to access %s due to lack of permissions.' % sys.argv[1]
    elif status_code == HTTP_NOT_FOUND:
        return '%s was not found or is not available.' % sys.argv[1]
    elif status_code == HTTP_INTERNAL_SERVER_ERROR:
        return '%s is not working properly. Internal server error.' % \
            sys.argv[1]


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("usage: python plushcap.py http://test.url/")
    else:
        status_code, content = contact_url(url=sys.argv[1])
        print(handle_response(status_code))
