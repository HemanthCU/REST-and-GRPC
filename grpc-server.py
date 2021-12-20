#!/usr/bin/env python3
import base64
import io
import grpc
from PIL import Image
from concurrent import futures

import service_pb2
import service_pb2_grpc

class RawImageServicer(service_pb2_grpc.RawImageServicer):

    def RawImageDimens(self, request, context):
        iobuffer = io.BytesIO(request.img)
        try:
            img = Image.open(ioBuffer)
            response = {
                'width': img.size[0],
                'height': img.size[1]
            }
        except:
            response = {'width': 0, 'height': 0}
        return service_pb2.imageReply(width=response['width'], height=response['height'])

class AddServicer(service_pb2_grpc.AddServicer):

    def AddNums(self, request, context):
        sum = request.a + request.b
        return service_pb2.addReply(sum=sum)

class DotProductServicer(service_pb2_grpc.DotProductServicer):

    def DotProd(self, request, context):
        res = 0
        try:
            a = request.a
            b = request.b
            if (len(a) != len(b)):
                res = 0
            else:
                for i in range(len(a)):
                    res += a[i] * b[i]
        except:
            res = 0
        return service_pb2.dotProductReply(dotproduct=res)


class JsonImageServicer(service_pb2_grpc.JsonImageServicer):

    def JsonImageDimens(self, request, context):
        b64str = request.jsonimg
        b64raw = b64str.encode("ascii")
        img = base64.b64decode(b64raw)
        iobuffer = io.BytesIO(img)
        try:
            img = Image.open(ioBuffer)
            response = {
                'width': img.size[0],
                'height': img.size[1]
            }
        except:
            response = {'width': 0, 'height': 0}
        return service_pb2.imageReply(width=response['width'], height=response['height'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    service_pb2_grpc.add_AddServicer_to_server(AddServicer(), server)
    service_pb2_grpc.add_RawImageServicer_to_server(RawImageServicer(), server)
    service_pb2_grpc.add_DotProductServicer_to_server(DotProductServicer(), server)
    service_pb2_grpc.add_JsonImageServicer_to_server(JsonImageServicer(), server)

    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
