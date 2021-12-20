#!/usr/bin/env python3
from __future__ import print_function
import requests
import json
import time
import sys
import base64
import jsonpickle
import random

def doRawImage(addr, debug=False):
    # prepare headers for http request
    headers = {'content-type': 'image/png'}
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    # send http request with image and receive response
    image_url = addr + '/api/rawimage'
    response = requests.post(image_url, data=img, headers=headers)
    if debug:
        # decode response
        print("Response is", response)
        print(json.loads(response.text))

def doAdd(addr, debug=False):
    headers = {'content-type': 'application/json'}
    # send http request with image and receive response
    add_url = addr + "/api/add/5/10"
    response = requests.post(add_url, headers=headers)
    if debug:
        # decode response
        print("Response is", response)
        print(json.loads(response.text))

def doDotProduct(addr, debug=False):
    headers = {'content-type': 'application/json'}
    # send http request with image and receive response
    dot_url = addr + "/api/dotproduct"
    firstval = [random.random()] * 100
    secondval = [random.random()] * 100
    values = {
        'a': firstval,
        'b': secondval
    }
    response = requests.post(dot_url, data=jsonpickle.encode(values), headers=headers)
    if debug:
        # decode response
        print("Response is", response)
        print(json.loads(response.text))

def doJsonImage(addr, debug=False):
    headers = {'content-type': 'application/json'}
    # send http request with image and receive response
    jsonimg_url = addr + "/api/jsonimage"
    jsonimg = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    b64raw = base64.b64encode(jsonimg)
    b64str = b64raw.decode("ascii")
    values = {
        'image': b64str
    }
    response = requests.post(jsonimg_url, data=jsonpickle.encode(values), headers=headers)
    if debug:
        # decode response
        print("Response is", response)
        print(json.loads(response.text))

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
    print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
    print(f"and <reps> is the integer number of repititions for measurement")

host = sys.argv[1]
cmd = sys.argv[2]
reps = int(sys.argv[3])

addr = f"http://{host}:5000"
print(f"Running {reps} reps against {addr}")

if cmd == 'rawImage':
    start = time.perf_counter()
    for x in range(reps):
        doRawImage(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'add':
    start = time.perf_counter()
    for x in range(reps):
        doAdd(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'jsonImage':
    start = time.perf_counter()
    for x in range(reps):
        doJsonImage(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'dotProduct':
    start = time.perf_counter()
    for x in range(reps):
        doDotProduct(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
else:
    print("Unknown option", cmd)