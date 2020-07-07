FROM python:3.8


RUN mkdir /client
COPY . /client
WORKDIR /client

RUN pip3 install grpcio
RUN pip3 install grpcio-tools

EXPOSE 50051

CMD [ "python3", "client.py" ]
