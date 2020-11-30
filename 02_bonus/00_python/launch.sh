#!/bin/sh

echo "Building an image."
docker build . -t fin

echo "Running python script."
docker run fin

#docker run fin "./financial.py" "MSFT" "Cost of Revenue"
