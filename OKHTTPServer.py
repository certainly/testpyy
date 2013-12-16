#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

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
p404_page = """<html>
<head>
<title>404 Not33333 Found</title>
</head>
<body>
404 Noteeee found
</body>
</html>
"""

def handleGet(environ, start_response):
   # Returns a dictionary containing lists as values.
   d = parse_qs(environ['QUERY_STRING'])

   # In this idiom you must issue a list containing a default value.
   age = d.get('age', [''])[0] # Returns the first age value.
   hobbies = d.get('hobbies', []) # Returns a list of hobbies.

   # Always escape user input to avoid script injection
   age = escape(age)
   hobbies = [escape(hobby) for hobby in hobbies]

   response_body = html % (age or 'Empty',
               ', '.join(hobbies or ['No Hobbies']))

   f = open('fx.txt','rb')
   pic_content=f.read()
   response_body=pic_content
   status = '200 OK'

   # Now content type is text/html
   response_headers = [
       # ('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]


def application(environ, start_response):


   if environ['PATH_INFO'] == '/out':
        response_body = p404_page # blank page, like original NModel version
        status = '200 OK'
        pass
   elif(environ['REQUEST_METHOD'] == 'GET'):
       return handleGet(environ, start_response)
   else:

       # the environment variable CONTENT_LENGTH may be empty or missing
       print 'look %s' % (environ['REQUEST_METHOD'])
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
       print 'age= %r' % age
       hobbies = d.get('hobbies', []) # Returns a list of hobbies.

       # Always escape user input to avoid script injection
       age = escape(age)
       hobbies = [escape(hobby) for hobby in hobbies]


       f = open('fx.txt','rb')
       pic_content=f.read()
       response_body=pic_content

       # response_body = html % (age or 'Empty',
       #             ', '.join(hobbies or ['No Hobbies']))

       status = '200 OK'

   response_headers = [
       # ('Content-Type', 'image/png'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]


httpd = make_server('localhost', 8051, application)
httpd.serve_forever()