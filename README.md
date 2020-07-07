# gRPC & redis & docker

## Açıklama;

gRPC teknolojisini yeni yeni öğrendiğim için sunucu ve istemci tarafını pythonla yapabildim. 


## Çalıştırmak için;

``` 
docker-compose up

```

Redis verilerini görebilmek için Redis-CLI ile kontrol edebilirsiniz;

``` 

redis-cli

lrange 'user' 0 100

```

## Yararlandığım kaynak

- [gRPC.io](https://grpc.io/docs/languages/python/basics/)