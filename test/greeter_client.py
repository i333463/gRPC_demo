from __future__ import print_function
import logging

import grpc

from test import hellogRPC_pb2, hellogRPC_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hellogRPC_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hellogRPC_pb2.HelloRequest(name='Eric'))

        response_bye = stub.SayGoodbye(hellogRPC_pb2.GoodbyeRequest(name='Eric'))
    print("Greeter client received: " + response.message)

    print("Greeter client received: " + response_bye.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()