#!/usr/bin/env python3
import socket
import argparse

parser = argparse.ArgumentParser(description="Enter the IP address and Port number")
parser.add_argument("--server", help="Use format <IP>:<Port>")
args = parser.parse_args()

if not args.server:
    ser = input("Please provide IP address and port number <IP>:<Port>\n")
else:
    ser = args.server

server = ser.split(':')

HOST = server[0]
PORT = int(server[1])
ADDR = (HOST, PORT)
FORMAT = 'utf-8'


def client():
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_sock.connect(ADDR)

    print(f"[CLIENT] Connection to server {ADDR[0]} successful!")
    msg = input("--> ")

    while msg.lower().strip() != 'bye':
        cli_sock.send(msg.encode(FORMAT))
        data = cli_sock.recv(1024).decode(FORMAT)
        print("[CLIENT] Message from server:\n>", data)
        msg = input("--> ")
    print("Session terminated")
    cli_sock.close()


if __name__ == "__main__":
    client()

