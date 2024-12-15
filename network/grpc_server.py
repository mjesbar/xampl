import logging

import grpc
import grpc_pb2
import grpc_pb2_grpc

from concurrent import futures


logging.basicConfig(level=logging.INFO)


class MessageEchoServicer(grpc_pb2_grpc.MessageEchoServicer):
  def ServerEcho(self, request, context):
    logging.info("Server received: %s, of type: %s", request, type(request))
    response = grpc_pb2.ServerResponse(message=request.message)
    logging.info("Server responded: %s, of type: %s", response, type(response))
    return response

    
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  grpc_pb2_grpc.add_MessageEchoServicer_to_server(
      MessageEchoServicer(), server
  )
  server.add_insecure_port("[::]:50051")
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
  logging.info("Server started at localhost:50051")
  serve()