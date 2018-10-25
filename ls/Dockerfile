FROM ubuntu:18.04

MAINTAINER oxford-mmm

#Fresh update packages
RUN apt update && \
    apt-get install -y software-properties-common

RUN groupadd fuse && \
    useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups sudo,fuse lodestone && \
    echo `echo "lodestone\nlodestone\n" | passwd lodestone` && \
    chown lodestone:lodestone /home/lodestone

#Define env variables
ENV HOME=/home/lodestone

#Copy source code and dependencies
RUN mkdir $HOME/app $HOME/tools

COPY app $HOME/app
COPY tools $HOME/tools

#Set up user
USER lodestone
WORKDIR $HOME/app

#Install aspera
RUN cd $HOME/tools && \
    ./aspera-connect-3.7.4.147727-linux-64.sh

ENV PATH="$PATH:~/.aspera/connect/bin/"

ENTRYPOINT ["/bin/bash"]




