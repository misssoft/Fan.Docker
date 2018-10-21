FROM ubuntu:14.04

MAINTAINER oxford-mmm

#Fresh update packages
RUN apt update && \
    apt-get install -y software-properties-common

#Update essential libraries
RUN apt-get update -y &&\
    apt-get install -y zlib1g-dev \
    libncurses5-dev     \
    libbz2-dev          \
    liblzma-dev         \
    g++-4.4             \
    build-essential     \
    curl                \
    zip                 \
    git                 \
    sed                 \
    python-pip          \
    nfs-common          \
    portmap             \
    python-dev          \
    python-pycurl       \
    python-lxml         \
    samtools htop     &&\
    apt-get clean     &&\
    apt-get purge     &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Install Oracle Java 1.7
COPY tools/jre-7u80-linux-x64.tar.gz /opt/
RUN  tar -xvzf /opt/jre-7u80-linux-x64.tar.gz -C /opt &&\
     rm "/opt/jre-7u80-linux-x64.tar.gz" &&\
     mv /opt/jre1.7.0_80  /opt/java17 &&\
     update-alternatives --install /usr/bin/java java /opt/java17/bin/java 100

#Install python and libraries
RUN pip install numpy biopython pysam==0.8.3

#Create compass user
RUN groupadd fuse && \
    useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups sudo,fuse compass && \
    echo `echo "compass\ncompass\n" | passwd compass` && \
    chown compass:compass /home/compass


RUN mkdir /home/compass/PIPELINE /data &&\
    chown compass:compass /data

#Define env variables
ENV HOME=/home/compass
ENV PIPELINE=$HOME/PIPELINE
ENV PATH=${PATH}:$PIPELINE/compass

#Copy source code of the COMPASS and dependencies
COPY compass $PIPELINE/compass
COPY gorm-tools $PIPELINE/gorm-tools

USER compass
VOLUME ['/home/compass/PIPELINE', '/data']
WORKDIR /data
ENTRYPOINT ["/bin/bash"]












