import socket
from DES import encryption
from DES import decryption

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print("Waiting Connection... ")

    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    while True:
        key = input("key: ")
        if len(key) == 8:
            break
        else:
            print("Key must have 8 character")
    
    while True:
        # receive message stream. it won't accept data packet greater than 1024 bytes
        message = conn.recv(1024).decode()
        if not message:
            # if message is not received break
            break

        print("Message:", decryption(message, key))
        
        message = input("Send Message -> ")
        if message == 'exit':
            break
    
        message = encryption(message,key)
        conn.send(message.encode())  # send message to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()