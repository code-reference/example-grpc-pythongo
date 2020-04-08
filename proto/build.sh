protoc -I proto toupper.proto --go_out=plugins=grpc:proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./toupper.proto
