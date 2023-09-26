import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((host, port))
mysock.connect(('data.pr4e.org', 80))
