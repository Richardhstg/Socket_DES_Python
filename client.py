import socket
from DES import encryption
from DES import decryption

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    while True:
        key = input("key: ")
        if len(key) == 8:
            break
        else:
            print("Key must have 8 character")
    
    message = input("Send Message -> ")  # take input
    message = encryption(message,key)

    while True:
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print("Message:", decryption(data, key))

        message = input("Send Message -> ")
        if message == 'exit':
            break
        message = encryption(message,key)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()