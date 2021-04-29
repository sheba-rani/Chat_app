#!/usr/bin/env python3
import socket
import argparse

parser = argparse.ArgumentParser(description="Enter the IP address and Port number")
parser.add_argument("--server", "-ip", help="IP address")
parser.add_argument("--port", "-p", help="Port number")
args = parser.parse_args()

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5060
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

if not args.server:
    ser = HOST
else:
    ser = args.server

if not args.port:
    port = PORT
else:
    port = args.port

print(f"No IP address and Port number entered by user!\nThe Host server is {ser} and port is {port}.")


def server():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind(ADDR)
    print("Starting server...")

    serv_sock.listen()
    print("Waiting for Client to connect")
 
    conn, addr = serv_sock.accept()
    print(f"[SERVER] Connection from client {addr[0]} has been established!")

    while True:
        data = conn.recv(1024).decode(FORMAT)
        if not data:
            break
        print("[SERVER] Message from client:\n>", data)
        data = input("--> ")
        conn.send(data.encode(FORMAT))
    print("Client disconnected!")
    conn.close()


if __name__ == "__main__":
    server()

