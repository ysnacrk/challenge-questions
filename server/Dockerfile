FROM python:3.8


RUN mkdir /server
COPY . /server
WORKDIR /server

RUN pip3 install grpcio
RUN pip3 install grpcio-tools
RUN pip3 install redis

EXPOSE 50051

CMD [ "python3", "server.py" ]
