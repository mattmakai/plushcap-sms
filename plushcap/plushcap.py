# -*- coding: utf-8 -*-
import sys
import requests

def ping_server(server_name):
    try:
        response = requests.get(server_name)
        return response.status_code, response.content
    except requests.exceptions.ConnectionError:
        return 404, ""


if __name__=='__main__':
    if len(sys.argv) < 2:
        print("usage: python plushcap.py http://test.url/")
    else:
        status_code, content = ping_server(sys.argv[1])
        print(status_code)
