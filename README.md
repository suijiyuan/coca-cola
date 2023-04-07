# coca-cola

Just for fun.

## Environment

| Software         | Version            |
|------------------|--------------------|
| Operation System | Rockey Linux 9 x64 |
| Docker           | 23.0.2             |

## How to install it

```shell
sudo dnf config-manager \
 --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install docker-ce
sudo docker build -t coca-cola .
sudo docker run -it -p 8000:8000 --rm --name coca-cola coca-cola
```

## How to use it

```shell
curl 127.0.0.1:5000/v1/check/ping
# expected response is 'pong'
```