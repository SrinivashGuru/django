FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /new_app

WORKDIR /new_app

ADD . /new_app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:$PORT
