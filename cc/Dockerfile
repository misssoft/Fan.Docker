FROM ubuntu:14.04

LABEL version="1.0"
LABEL description="Oxford MMM Pathogen Pipeline"
LABEL maintainer="crooks.it@ndm.ox.ac.uk"

#Fresh update packages
RUN apt update && \
    apt-get install -y software-properties-common

##Update essential libraries
# RUN apt-get update -y &&\
#     apt-get install -y  \    
#     build-essential     \
#     curl                \
#     git                 \
#     g++-4.4             \
#     libbz2-dev          \
#     liblzma-dev         \
#     libncurses5-dev     \
#     nfs-common          \
#     portmap             \
#     python-dev          \
#     python-lxml         \
#     python-pycurl       \
#     python-pip          \ 
#     samtools htop       \
#     sed                 \
#     zip                 \
#     zlib1g-dev        &&\
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# #Install Oracle Java 1.7
# WORKDIR /opt
# COPY tools/jre-7u80-linux-x64.tar.gz .
# RUN  tar -xvzf jre-7u80-linux-x64.tar.gz -C &&\
#      rm "jre-7u80-linux-x64.tar.gz" &&\
#      update-alternatives --install /usr/bin/java java jre1.7.0_80/bin/java 100

# #Install python and libraries
# RUN pip install numpy biopython pysam==0.8.3

# #Create compass user
# RUN groupadd fuse && \
#     useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups sudo,fuse compass && \
#     echo `echo "compass\ncompass\n" | passwd compass` && \
#     chown compass:compass /home/compass

# #Set up directories
# RUN mkdir /home/compass/pipeline /data &&\
#     chown compass:compass /data

# #Define env variables
# ENV HOME=/home/compass
# ENV PIPELINE=$HOME/pipeline
# ENV PATH=${PATH}:$PIPELINE/compass

# #Copy source code of the COMPASS and dependencies
# USER compass
# WORKDIR /home/complass/pipeline
# COPY compass .
# COPY tools .
# VOLUME ['/home/compass/pipeline', '/data']
# ENTRYPOINT ["/bin/bash"]












