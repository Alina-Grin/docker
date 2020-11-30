#!/bin/sh
echo "Building an Image"
docker build . -t ts-img

echo "Container running in detach mode"
docker run -d --name teamspeak --rm -p 9987:9987/udp -p 10011:10011 -p 30033:30033 ts-img

echo "Connect via local client to $(docker-machine ip Char) and password and token."
docker logs teamspeak | grep "password"
#docker rmi $(docker images -q)
