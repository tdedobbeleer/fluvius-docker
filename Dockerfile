FROM selenium/standalone-chrome:latest

#Python install
RUN apt update
RUN apt install python3-pip -y
RUN pip install selenium flask
