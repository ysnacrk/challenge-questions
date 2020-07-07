# gRPC & redis & docker

## Açıklama;

- Go dilini çok yatkın olmadığım için ve gRPCyi yeni yeni öğrendiğim için istemci ve sunucu tarafını Python ile yazıldı.  
- Stream mesaj yapısını kullanmamın nedeni sunucuda verilerin tek tek bakılabilir olması.  

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