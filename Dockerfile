FROM python:3-alpine

#Python install
RUN pip install selenium flask gunicorn

ADD fluvius.py /opt/fluvius.py
WORKDIR /opt

ENTRYPOINT [ "gunicorn", "-w 4", "'fluvius:app'" ]
