import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Criar socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET - IPV4 and SOCK_STREAM has by default TCP
# Bind do socket
s.bind(ADDR)


# Function to establish new connections
def start_server():
    # Listen
    s.listen(3) #queue of 5 connections
    print(f"[LISTENING] On: {SERVER}")

    while True:
        conn, addr = s.accept() # Accept connections and start new thread to handle it
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[# CONNECTIONS] {threading.activeCount() -1}")
# end of fucntion start_server ----------------------------------

# Function to handle clients connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] Address: {addr}.")

    connected = True
    # Decodde msgs while connected
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: # Verifify that it is not null
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            # Verifify is it's a closing msg
            if (msg == DISCONNECT_MESSAGE):
                connected == False

            print(f"[{addr}] {msg}")

    # CLose connection
    conn.close()
# end of fucntion handle_client ----------------------------------


print("Server is starting .....")
start_server()
