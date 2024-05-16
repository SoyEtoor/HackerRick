FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /hackerrick
WORKDIR /hackerrick
COPY requirements.txt /hackerrick/
RUN pip install -r requirements.txt
COPY . /hackerrick
CMD python manage.py runserver 0.0.0.0:8080
