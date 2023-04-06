# coca-cola

Just for fun.

## Environment

## How to install it

```shell
sudo dnf install python3
pip install -r requirements.txt
python main.py
```

```shell
sudo dnf install docker-ce
sudo docker build -t coca-cola .
sudo docker run -it -p 5000:5000 --rm --name coca-cola coca-cola
```

## How to use it

```shell
curl 127.0.0.1:5000/v1/check/ping
# expected response is 'pong'
```