import zmq
import time
import asyncio

# ZeroMQ Context
context = zmq.Context()

sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5680")
sock1 = context.socket(zmq.PUB)
sock1.bind("tcp://127.0.0.1:5681")


if __name__ == '__main__':

    while True:
        mes=sock.recv()
        print(str(mes))
        
        sock1.send_string(str(mes))
        sock.send_string(str(mes))
