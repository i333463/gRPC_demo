from concurrent import futures
import logging
import time

import grpc

from genproto import easyshop_pb2
from genproto import easyshop_pb2_grpc
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class AccountService(easyshop_pb2_grpc.AccountServiceServicer):
    # def register(self, request, context):
    #     response = easyshop_pb2.RegisterResponse()
    #     response.user_id = request.user_id
    #     response.password = request.password
    #     return response

    # def exist(self, request, context):
    #     return easyshop_pb2.Success_or_not(success_or_not='sudcess')
    #

    def login(self, request, context):
        response = easyshop_pb2.LoginResponse()
        response.user_name = 'myNameIsEric'
        return response
    #
    # def logout(self, request, context):
    #     return easyshop_pb2.Success_or_not(message='1')

    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    easyshop_pb2_grpc.add_AccountServiceServicer_to_server(AccountService(), server)
    health_pb2_grpc.add_HealthServicer_to_server(AccountService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()