# -*- coding: utf-8 -*-
import sys
import requests

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


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("usage: python plushcap.py http://test.url/")
    else:
        status_code, content = contact_url(url=sys.argv[1])
        print(status_code)
