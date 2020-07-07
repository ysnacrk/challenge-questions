
import grpc
import json

import user_pb2
import user_pb2_grpc


"""

Read json file  from /users
Make user object and send to server with generator

"""

def read_json():
    user_list = []

    for i in range(1, 11):
        filename = "users/" + str(i) + ".json"
        file = open(filename)
        for item in json.load(file):
            user = user_pb2.User(
                id = item["id"],
                first_name = item["first_name"],
                last_name = item["last_name"],
                email = item["email"],
                gender = item["gender"],
                ip_address = item["ip_address"],
                user_name = item["user_name"],
                agent = item["agent"],
                country=item["country"],
            )
        
            user_list.append(user)
    return user_list

def generate_data(user_list):
    for i in user_list:
        yield i
    
def record_data(stub):
    user_list = read_json()
    user_iterator = generate_data(user_list)
    response = stub.RecordData(user_iterator)
    print("Finished trip with {} users. Time :  {} " .format(response.user_count , response.elapsed_time))

def run():
    print("client up")
    with grpc.insecure_channel('server_:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        record_data(stub)

    
if __name__ == '__main__':
    run()
