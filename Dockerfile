FROM python:3-alpine

#Python install
RUN pip install selenium flask

ADD fluvius.py /opt/fluvius.py
WORKDIR /opt

ENTRYPOINT [ "flask", "--app", "fluvius", "run" ]
