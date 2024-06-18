FROM python:3-alpine

#Python install
RUN pip install selenium flask gunicorn

ADD fluvius.py /opt/app.py
WORKDIR /opt

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "-w", "4", "app:app"]
