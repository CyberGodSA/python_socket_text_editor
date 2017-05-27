import socket
import time

history = r'C:\Users\Danil\PycharmProjects\lab_socket_editor\server_history.txt'
text = open(r'C:\Users\Danil\PycharmProjects\lab_socket_editor\text.txt', 'r')
header = "H"


def who(conn):
    cmd = 'info '
    author = 'The author: Hartwig Danil'
    task = 'The task: 1. Socket Text Editor'
    conn.send(bytes(header + cmd + author, encoding='utf-8'))
    write_history('server_send: ' + author)
    time.sleep(0.1)
    conn.send(bytes(header + cmd + task, encoding='utf-8'))
    write_history('server_send: ' + task)


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
write_history('connected to: ' + addr)
conn.send(bytes(text.read(), encoding='utf-8'))

while True:
    text = conn.recv(1024).decode('utf-8')
    if text == "who":
        who(conn)
    elif text == "end":
        break
    else:
        print(text)

    write_history('server_get: ' + text)

conn.close()
