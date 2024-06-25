# fluvius-docker

Selenium docker container which posts a form from fluvius.be. I couldn't find an API to speak to, so it's done the hard way. I'm not in any way responsible for misuse. This is a method anyone can reproduce with a bit of knowledge. Use it wisely.

The server endpoint is:
```
http://ip:port/api/fluvius/{ean}/status
```

If you don't feel like using the docker image, just use the python script by running the commands (take a look in the Docker file of this repo, copy the reqs and start the service).
