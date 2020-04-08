#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
# import sys
# sys.path.append("..")
from proto import toupper_pb2, toupper_pb2_grpc

_HOST = 'localhost'
_PORT = '50051'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = toupper_pb2_grpc.ToUpperStub(channel=conn)
    response = client.Upper(toupper_pb2.UpperRequest(name='hello,world!'))
    print("received: " + response.message)

if __name__ == '__main__':
    run()

