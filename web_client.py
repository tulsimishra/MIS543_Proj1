# import necessary modules
import sys
from urlparse import urlparse
from socket import *

# obtain the two parameters from commend line
param_url = sys.argv[1]
param_file = sys.argv[2]

# parse the url 
url_parsed = urlparse(param_url)
# you can obtain the following attributes from url_parsed
# e.g param_url = 'http://www.eller.arizona.edu:2016/index.html'
# url_parsed.hostname: Hostname = 'www.eller.arizona.edu'
# url_parsed.port: port number = 2016
# url_parsed.path: path of the file = '/index.html'

s = socket(AF_INET, SOCK_STREAM)

##### your code goes here ... #####
# 1. Construct the IP address and port number
# 2. Construct the http GET request (with Host and Connection headers)
# 3. Connect to the server, and read the response
# 4. Save the body of the HTTP response to param_file (skip the header)
# 5. If the HTTP response is anything rather than 200 OK, write the response header to param_file
# 6. Close the connection and the file

print "\nFinishing downloading ..."


