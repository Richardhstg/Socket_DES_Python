import socket
from DES import encryption
from DES import decryption

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    key = input("key: ")
    message = encryption(message,key)

    while message.lower().strip() != 'bye':
        client_socket.send(b"Message:" + message.encode() + b"\nKey:" + key.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print(data)  # show in terminal
        parts = data.replace('\nKey', '').split(":")
        
        decryption(parts[1], parts[2])

        message = input(" -> ")  # take input
        key = input("key: ")
        message = encryption(message,key)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()