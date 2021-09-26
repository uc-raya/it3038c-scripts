import socket

hosts = ['www.google.com', 'www.uc.edu', 'www.bing.com']

print('Working from host: ' + socket.getfqdn())

for h in hosts:
    print(h + ': ' + socket.gethostbyname(h))