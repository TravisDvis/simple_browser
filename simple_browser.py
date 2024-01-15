import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url_input = input('Enter url: ')
url_input_ext = input('Enter url extension: ')

mysock.connect((str(url_input), 80))
cmd_str = 'GET ' + 'http://'+ str(url_input) + '/' + str(url_input_ext) + ' HTTP/1.0\r\n\r\n'
cmd = cmd_str.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = ' ')

mysock.close()