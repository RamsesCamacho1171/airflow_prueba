FROM ubuntu 
RUN apt-get update 
RUN apt-get install -y python3 
RUN echo 1.0 >> /etc/version && apt-get install -y git \
    && apt-get install -y iputils-ping 
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
#WORKDIR
RUN mkdir /datos
WORKDIR /datos
RUN touch f1.txt
RUN mkdir /datos1
WORKDIR /datos1
RUN touch f2.txt


#ADD
ADD a.py .
ADD DockerFiles docker
ADD https://datosabiertos.impi.gob.mx/IMPICifras/Invenciones16.csv /datos/
#ENTRYPOINT
ENTRYPOINT [ "python3","a.py" ]