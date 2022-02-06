FROM reon/rgvflood:v0.1 AS builder

RUN mkdir -p -m 0600 ~/.ssh && \
    ssh-keyscan -H github.com bitbucket.org >> ~/.ssh/known_hosts
RUN pip install git+ssh://git@github.com/RATESResearch/REONapp

FROM builder AS rgvflood

COPY settings.py /usr/src/geonode/geonode/
COPY base.html /usr/src/geonode/geonode/templates/
COPY urls.py /usr/src/geonode/
COPY logo.png /usr/src/geonode/geonode/static/geonode/img/2021/12/
COPY background.jpg /usr/src/geonode/geonode/static/geonode/img/2021/12/
COPY theme.json /usr/src/geonode/
RUN python manage.py loaddata /usr/src/geonode/theme.json
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput
# Export ports
EXPOSE 8000

# We provide no command or entrypoint as this image can be used to serve the django project or run celery tasks
# ENTRYPOINT /usr/src/geonode/entrypoint.sh
