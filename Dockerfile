# -----------------------------------------------------------------------------
# docker-minecraft-server
#
# Builds a basic docker image that can run a Minecraft server
# (http://minecraft.net/).

# https://github.com/rlenferink/docker-minecraft/blob/master/Dockerfile
# -----------------------------------------------------------------------------

# Base image is the latest LTS version of Ubuntu
FROM   ubuntu:18.04

# Make sure we don't get notifications we can't answer during building.
ENV    DEBIAN_FRONTEND noninteractive

RUN    mkdir mc

# /data contains static files and database
VOLUME ["/mc"]

WORKDIR //mc

# Download and install everything from the repos.
#RUN    apt-get -y update; apt-get -y upgrade;
RUN    apt-get update --fix-missing && apt-get install -y fontconfig --fix-missing
#RUN    apt-get --yes install curl oracle-java8-installer ; apt-get clean

RUN    apt-get --yes install python3.7 wget git curl init openjdk-17-jdk

# Cpolar

RUN    curl -L https://www.cpolar.com/static/downloads/install-release-cpolar.sh | bash

# Server build

RUN    git clone https://github.com/abaaba-team/docker-minecraft-server.git && cd docker-minecraft-server 

#--------------------------------------
# Load in all of our config files.
#ADD    ./scripts/start /start
#
# Fix all permissions
#RUN    chmod +x /start
#
# 25565 is for minecraft
#EXPOSE 25565
#--------------------------------------



# /start runs it.
#CMD    ["/start"]
