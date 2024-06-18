# fluvius-docker
Selenium docker container which posts a form from fluvius.be.

The service needs 2 ENV variables to function properly:

- EAN: Your EAN number
- SELENIUM_SERVER: The service uses Selenium to post a form. Specify the address (DNS or IP, ports and paths are hard-coded).

The Selenium instance is not provided within the container. You can add it in the docker-compose.yaml file as follows:

```
services:
  fluvius:
    container_name: fluvius
    image: "tdedobbeleer/fluvius:latest"
    environment:
      - EAN=541x
      - SELENIUM_SERVER=selenium
    ports:
      - "5000:5000"
    links:
      - selenium:selenium
  selenium:
    container_name: selenium
    image: "selenium/standalone-chrome"
```

The server endpoint is:
```
http://IP:port/api/v1/fluvius/delay
```
