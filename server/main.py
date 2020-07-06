import grpc
import redis
import time

from concurrent import futures

import user_pb2
import user_pb2_grpc


"""

Getting user data and saving to redis
and send user count and elapsed time


"""
redis  = redis.Redis()

class UserServicer(user_pb2_grpc.UserService):
    
    def RecordData(self, request_iterator, context):
        user_count = 0
        start_time = time.time()

        for user in request_iterator:

            redis.rpush('users' , str(user))
            user_count += 1


        elapsed_time = time.time() - start_time

        return user_pb2.Response(user_count = user_count , elapsed_time = str(elapsed_time))

def run():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserServicer() , server)

    server.add_insecure_port('[::]:50051') 
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    run()