'''
Written by: Luu Gia Thuy
http://luugiathuy.com/2011/03/simple-web-proxy-python/
'''
​
import os,sys,_thread,socket
​
#********* CONSTANT VARIABLES *********
BACKLOG = 50            # how many pending connections queue will hold
MAX_DATA_RECV = 4096    # max number of bytes we receive at once
DEBUG = False           # set to True to see the debug msgs
​
​
#********* MAIN PROGRAM ***************
def main():
​


  # check the length of command running
  if (len(sys.argv) < 2):
    print ("usage: proxy <port>")
    return sys.stdout
​
  # host and port info.
  host = ''               # blank for localhost
  port = int(sys.argv[1]) # port from argument
​
  try:
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
​
    # associate the socket to host and port
    s.bind((host, port))
​
    # listenning
    s.listen(BACKLOG)
​
  except socket.error:
    if s:
        s.close()
    print("Could not open socket")
    sys.exit(1)
​
  # get the connection from client
  while 1:
    conn, client_addr = s.accept()
​
    # create a thread to handle request
    _thread.start_new_thread(proxy_thread(conn, client_addr), (conn, client_addr))
​
  s.close()
​
#********* PROXY_THREAD ***************
def proxy_thread(con, cAddr):
    # print("Thread created: {} - {}".format(con,cAddr))
    # get the request from browser
    request = con.recv(MAX_DATA_RECV)
​
    # parse the first line
    first_line = request.split('n')[0]
​
    # get url
    url = first_line.split(' ')[1]
​
    if (DEBUG):
        print(first_line)
        print("\n")
        print("URL: {}".format(url))
        print("\n")
​
    # find the webserver and port
    http_pos = url.find("://")          # find pos of ://
    if (http_pos==-1):
        temp = url
    else:
        temp = url[(http_pos+3):]       # get the rest of url
​
        port_pos = temp.find(":")           # find the port pos (if any)
​
    # find end of web server
    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos = len(temp)
​
    webserver = ""
    port = -1
    if (port_pos==-1 or webserver_pos < port_pos):      # default port
        port = 80
        webserver = temp[:webserver_pos]
    else:       # specific port
        port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
        webserver = temp[:port_pos]
​
    print("Connect to: {}:{}".format(webserver, port))
​
    try:
        # create a socket to connect to the web server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(request)         # send request to webserver
​
        while 1:
        # receive data from web server
            data = s.recv(MAX_DATA_RECV)
​
        if (len(data) > 0):
            # send to browser
            conn.send(data)
​
        s.close()
        con.close()
    except socket.error:
        if s:
            s.close()
        if con:
            con.close()
            print("Runtime Error:").format(message)
            sys.exit(1)
​
if __name__ == '__main__':
  main()