import rides_pb2 as pb

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3'],
)
print(request)

# Marshalling
data = request.SerializeToString()  # String means "byte string" here. It actually serialises to binary
print('type:', type(data))
print('size:', len(data))

# Unmarshalling
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)