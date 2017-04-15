import socket
import time

hypertext = r'C:\Users\Danil\PycharmProjects\lab_socket_editor\hypertext.txt'
tcp = r'C:\Users\Danil\PycharmProjects\lab_socket_editor\tcp.txt'
www = r'C:\Users\Danil\PycharmProjects\lab_socket_editor\www.txt'
history = r'C:\Users\Danil\PycharmProjects\lab_socket_editor\server_history.txt'
header = 'H'
text = open(r'C:\Users\Danil\PycharmProjects\lab_socket_editor\text.txt', 'r')


def write_history(s):
    global history
    f = open(history, 'a')
    f.write(time.asctime(time.localtime(time.time())) + '\t' + s + '\n')
    f.close()


# main
sock = socket.socket()
sock.bind(('', 1035))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)
conn.send(bytes(text.read(), encoding='utf-8'))

while True:
    text = conn.recv(1024).decode('utf-8')
    print(text)
