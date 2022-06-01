# -----------------------------------------------------------------------------
# docker-minecraft-server
#
# Builds a basic docker image that can run a Minecraft server
# (http://minecraft.net/).

# https://github.com/rlenferink/docker-minecraft/blob/master/Dockerfile
# -----------------------------------------------------------------------------

FROM   ubuntu:18.04

# Make sure we don't get notifications we can't answer during building.
ENV    DEBIAN_FRONTEND noninteractive

RUN    mkdir mc

# /data contains static files and database
VOLUME ["/mc"]

WORKDIR //mc

# Download and install everything from the repos.
RUN    apt-get -y update; apt-get -y upgrade;

RUN    apt-get --yes install python3.7 wget git curl init 

RUN    apt-get --yes install openjdk-17-jdk-headless
# Cpolar
# Server build

CMD    curl -L https://www.cpolar.com/static/downloads/install-release-cpolar.sh | bash && git clone https://github.com/abaaba-team/docker-minecraft-server.git && cd docker-minecraft-server && python3 Test.py | bash && bash
