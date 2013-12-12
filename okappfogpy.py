#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
# import bottle
import os
import urllib2
html = """
<html>
<body>
   <form method="post" action="test.py">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
   </body>
</html>
"""

def application(environ, start_response):
   print '11startlalala'
   # the environment variable CONTENT_LENGTH may be empty or missing
   try:
      request_body_size = int(environ.get('CONTENT_LENGTH', 0))
   except (ValueError):
      request_body_size = 0

   # When the method is POST the query string will be sent
   # in the HTTP request body which is passed by the WSGI server
   # in the file like wsgi.input environment variable.
   request_body = environ['wsgi.input'].read(request_body_size)
   d = parse_qs(request_body)

   age = d.get('age', [''])[0] # Returns the first age value.
   hobbies = d.get('hobbies', []) # Returns a list of hobbies.

   # Always escape user input to avoid script injection
   age = escape(age)
   hobbies = [escape(hobby) for hobby in hobbies]

   responseWeb = urllib2.urlopen('https://dl.dropboxusercontent.com/u/79132157/abc')
   pic_content = responseWeb.read()

   # f = open('abc','rb')
   # pic_content=f.read()
   response_body=pic_content

   # response_body = html % (age or 'Empty',
   #             ', '.join(hobbies or ['No Hobbies']))

   status = '200 OK'

   response_headers = [
       # ('Content-Type', 'image/png'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]

# print '22startlalala'
# httpd = make_server('localhost', 8080, application)
# print 'startlalala'
# httpd.serve_forever()