from datetime import datetime
import rides_pb2 as pb

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3'],
    type=pb.POOL,
    location=pb.Location(
        lat=32.5270941,
        lng=34.9404309,
    )
)

# Python time cannot be used, so conversion is necessary
dt = datetime(2025, 10, 27, 16, 14, 5)
request.time.FromDatetime(dt)
print(request)

# ToDatetime
dt2 = request.time.ToDatetime()
print(type(dt2), dt2)

# now
from google.protobuf.timestamp_pb2 import Timestamp
now = Timestamp()
now.GetCurrentTime()
print(now)