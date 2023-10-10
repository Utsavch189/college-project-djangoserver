# pull the official base image
FROM python:3.10.12-alpine

# set work directory
WORKDIR /usr/app

ADD req.txt . 
# means if requirements.txt changes then only build command install requirements.txt otherwise not

# install dependencies
RUN pip install -r req.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "mysite.wsgi:application"]
