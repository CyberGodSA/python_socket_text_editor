import socket
import time
import sys

from tkinter import *

f = open(r'C:\Users\Danil\PycharmProjects\lab_socket_editor\client_history.txt', 'a')
f.write('---------------------------------------------------------------------\n')
host = ''
header = 'H'

filename = None


def get_host():
    global host
    print('Input server ip adress: ')
    host = input()


def send_text():
    data = textPad.get('1.0', END)
    sock.send(bytes(data, encoding='utf-8'))


# main
if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    get_host()

sock = socket.socket()
sock.connect((host, 1035))

while True:
    text__ = sock.recv(1024).decode('utf-8')
    if not text__: break
    root = Tk()
    root.title("Client Text Editor")
    textPad = Text(root, width=100, height=80)

    textPad.insert('1.0', text__)

    menu = Menu(root)
    root.config(menu=menu)
    menu.add_command(label="Send", command=send_text)

    textPad.bind("<KeyPress>", send_text)

    textPad.pack()
    root.mainloop()

f.close()
sock.close()
