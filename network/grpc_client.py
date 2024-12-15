import logging

import grpc
import grpc_pb2
import grpc_pb2_grpc


logging.basicConfig(level=logging.INFO)


def main():
  # call remote procedure
  with grpc.insecure_channel("localhost:50051") as channel:
    stub = grpc_pb2_grpc.MessageEchoStub(channel)
    request = grpc_pb2.ClientResponse(message="you are the best")
    logging.info("Client sent: %s, of type: %s", request, type(request))
    response = stub.ServerEcho(request)

  logging.info("Client received: %s, of type %s", response, type(response))


if __name__ == "__main__":
  main()