#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import logging

import grpc
# import sys
# sys.path.append("..")
from proto import toupper_pb2, toupper_pb2_grpc

_HOST = 'localhost'
_PORT = '50051'

def run():
    with grpc.insecure_channel(_HOST + ':' + _PORT) as channel:
        stub = toupper_pb2_grpc.ToUpperStub(channel)
        response = stub.Upper(toupper_pb2.UpperRequest(name='hello,world!'))
    print("received: " + response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()

