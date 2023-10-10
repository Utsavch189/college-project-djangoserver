# pull the official base image
FROM python:3.10.12-alpine

# set work directory
WORKDIR /usr/app

ADD req.txt . 
# means if requirements.txt changes then only build command install requirements.txt otherwise not

RUN set -ex \
    && apk add --no-cache --virtual .build-deps build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/req.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps


# install dependencies
RUN pip install -r req.txt

ADD . .

RUN python manage.py makemigrations
RUN python manage.py migrate

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "mysite.wsgi:application"]
