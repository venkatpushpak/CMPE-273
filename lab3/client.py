import zmq
import sys
import time
import asyncio
# ZeroMQ Context
context = zmq.Context()

x=sys.argv[1:]

sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5680")

sock1 = context.socket(zmq.SUB)
sock1.connect("tcp://127.0.0.1:5681")
sock1.setsockopt_string(zmq.SUBSCRIBE, '')

if __name__ == '__main__':

    while True:
        #print("[" + str(x) + "] :" )
        test=str(input("[" + str(x) + "] :" ))
        sock.send_string("[" + str(x) + "] :" +test)
        message= str(sock1.recv())
        mes=sock.recv()
        ss=str(sys.argv[1:]).split("'")
        #print(message)
        #print(str(ss[1]))
        if str(ss[1]) not in  message:
            print (message)
