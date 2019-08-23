from concurrent import futures
import logging
import time

import grpc
import db as db

from genproto import easyshop_pb2
from genproto import easyshop_pb2_grpc
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class AccountService(easyshop_pb2_grpc.AccountServiceServicer):
    def register(self, request, context):

        response = easyshop_pb2.RegisterResponse()
        conn = db.get_connection()
        user_name = db.select_user_by_user_id(conn, request.user_id)

        if user_name == '':
            db.create_user(db.get_connection(), request.user_id, request.user_name, request.password)
            response.user_id = request.user_id
            response.password = request.password

        return response

    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING)

    # def exist(self, request, context):
    #     return easyshop_pb2.Success_or_not(success_or_not='sudcess')
    #
    # def login(self, request, context):
    #     return easyshop_pb2.LoginResponse(message='Goodbye, %s!' % request.name)
    #
    # def logout(self, request, context):
    #     return easyshop_pb2.Success_or_not(message='1')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    easyshop_pb2_grpc.add_AccountServiceServicer_to_server(AccountService(), server)
    health_pb2_grpc.add_HealthServicer_to_server(AccountService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()