# gRPC Sample App
Example of a gRPC server and client using Python.

## Instructions
1. Generate `rides/rides_pb2.py` and `rides/rides_pb2_grpc.py` from `proto/rides.proto`:
```
python -m grpc_tools.protoc \
    -Iproto \
    --python_out=rides \
    --grpc_python_out=rides \
    proto/rides.proto
```
2. Run the server: `python rides/server.py`
3. Try the different examples that illustrate specific parts of gRPC

    - `01_marshalling.py`. Marshalling and unmarshalling a request
    - `02_enumeration.py`. Working with an ENUM type
    - `03_nested.py`. Nesting definitions
    - `04_timestamp.py`. Using datetimes
    - `05_json.py`. Comparison between JSON and Protocol Buffers
4. Run the client in two different ways: 
    a. Client/server: `python rides/client.py`. 
        The car requests a new ride.
        The server will return a ride ID.
    b. Streaming: `python rides/client.py events`. 
        The car streams its location to the server, which tracks it.
        The client will send 7 random events to the server, which will acknowledge them.

## Tools
Python

## Author
Miki Tebeka, from the LinkedIn Learning course [*gRPC in Python*](https://www.linkedin.com/learning/grpc-in-python) (2022).