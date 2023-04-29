FROM python:3.10

COPY requirements.txt requirements.txt 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY application_default_credentials.json application_default_credentials.json
ENV GOOGLE_APPLICATION_CREDENTIALS=/application_default_credentials.json
