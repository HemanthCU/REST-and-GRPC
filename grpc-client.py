#!/usr/bin/env python3
from __future__ import print_function
import time
import sys
import base64
import random
import grpc

import service_pb2
import service_pb2_grpc

def doRawImage(debug=False):
    stub = service_pb2_grpc.RawImageStub(channel)
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    response = stub.RawImageDimens(service_pb2.rawImageMsg(img=img))

    if debug:
        print("Response is", response)

def doAdd(debug=False):
    stub = service_pb2_grpc.AddStub(channel)
    response = stub.AddNums(service_pb2.addMsg(a=5, b=10))

    if debug:
        print("Response is", response)

def doDotProduct(debug=False):
    stub = service_pb2_grpc.DotProductStub(channel)
    firstval = [random.random()] * 100
    secondval = [random.random()] * 100
    response = stub.DotProd(service_pb2.dotProductMsg(a=firstval, b=secondval))

    if debug:
        print("Response is", response)

def doJsonImage(debug=False):
    stub = service_pb2_grpc.JsonImageStub(channel)
    jsonimg = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    b64raw = base64.b64encode(jsonimg)
    b64str = b64raw.decode("ascii")
    response = stub.JsonImageDimens(service_pb2.jsonImageMsg(jsonimg=b64str))

    if debug:
        print("Response is", response)

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
    print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
    print(f"and <reps> is the integer number of repititions for measurement")

host = sys.argv[1]
cmd = sys.argv[2]
reps = int(sys.argv[3])

addr = f"{host}:5001"
channel = grpc.insecure_channel(addr)
print(f"Running {reps} reps against {addr}")
with channel:
    if cmd == 'rawImage':
        start = time.perf_counter()
        for x in range(reps):
            doRawImage()
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'add':
        start = time.perf_counter()
        for x in range(reps):
            doAdd()
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'jsonImage':
        start = time.perf_counter()
        for x in range(reps):
            doJsonImage()
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    elif cmd == 'dotProduct':
        start = time.perf_counter()
        for x in range(reps):
            doDotProduct()
        delta = ((time.perf_counter() - start)/reps)*1000
        print("Took", delta, "ms per operation")
    else:
        print("Unknown option", cmd)