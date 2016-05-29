# Getting Base Image
FROM ubuntu:latest

# Author info
MAINTAINER asatake

# Build
RUN apt-get update
RUN apt-get install -y emacs
RUN apt-get install -y curl
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN pip3 install --upgrade pip

# Port
EXPOSE 22 80
