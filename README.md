# Python API to fetch MAC detail + Docker Container
Built api of [mac adress](https://macaddress.io/) with docker container.

## Installation
Follow the steps to install docker [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

## Usage
Build docker image and container and run it.

First clone the repo and run below command

Create a docker image.
```
sudo docker build -t sample_image_name .
```

Now, run docker image
```
sudo docker run sample_image_name:latest 44:38:39:ff:ef:57
```

Above command will always print `Company Name` and if wrong address then return error message.

## Note
Create a file called `config.yaml` in same directory.
```
apikey:
  macaddress: API_KEY
```
Replace API_KEY with your one.
