# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from genproto import easyshop_pb2 as easyshop__pb2


class AccountServiceStub(object):
  """-----------------Account Service-----------------
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.exist = channel.unary_unary(
        '/easyshop.AccountService/exist',
        request_serializer=easyshop__pb2.Account.SerializeToString,
        response_deserializer=easyshop__pb2.Success_or_not.FromString,
        )
    self.register = channel.unary_unary(
        '/easyshop.AccountService/register',
        request_serializer=easyshop__pb2.RegisterRequest.SerializeToString,
        response_deserializer=easyshop__pb2.RegisterResponse.FromString,
        )
    self.login = channel.unary_unary(
        '/easyshop.AccountService/login',
        request_serializer=easyshop__pb2.LoginRequest.SerializeToString,
        response_deserializer=easyshop__pb2.LoginResponse.FromString,
        )
    self.logout = channel.unary_unary(
        '/easyshop.AccountService/logout',
        request_serializer=easyshop__pb2.LogoutRequest.SerializeToString,
        response_deserializer=easyshop__pb2.Success_or_not.FromString,
        )


class AccountServiceServicer(object):
  """-----------------Account Service-----------------
  """

  def exist(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logout(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccountServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'exist': grpc.unary_unary_rpc_method_handler(
          servicer.exist,
          request_deserializer=easyshop__pb2.Account.FromString,
          response_serializer=easyshop__pb2.Success_or_not.SerializeToString,
      ),
      'register': grpc.unary_unary_rpc_method_handler(
          servicer.register,
          request_deserializer=easyshop__pb2.RegisterRequest.FromString,
          response_serializer=easyshop__pb2.RegisterResponse.SerializeToString,
      ),
      'login': grpc.unary_unary_rpc_method_handler(
          servicer.login,
          request_deserializer=easyshop__pb2.LoginRequest.FromString,
          response_serializer=easyshop__pb2.LoginResponse.SerializeToString,
      ),
      'logout': grpc.unary_unary_rpc_method_handler(
          servicer.logout,
          request_deserializer=easyshop__pb2.LogoutRequest.FromString,
          response_serializer=easyshop__pb2.Success_or_not.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'easyshop.AccountService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
