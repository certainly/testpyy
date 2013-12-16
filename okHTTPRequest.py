#!/usr/bin/env python
#coding=utf8

import httplib, urllib

httpClient = None


def getRequest():
    try:
        httpClient = httplib.HTTPConnection('localhost', 8051, timeout=30)
        httpClient.request('GET', '/')

        #response是HTTPResponse对象
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


def postRequest():
    try:
        params = urllib.urlencode({'name': 'tom', 'age': 22})
        headers = {"Content-type": "application/x-www-form-urlencoded"
                        , "Accept": "text/plain"}

        httpClient = httplib.HTTPConnection("localhost", 8051, timeout=30)
        httpClient.request("POST", "/", params, headers)

        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders() #获取头信息
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def test():
    # print 'look%s',parse_qs(environ['QUERY_STRING'])
    print''
# getRequest()
postRequest()