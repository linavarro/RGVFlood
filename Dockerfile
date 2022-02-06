FROM reon/geonode:v3.3.0 AS builder

RUN mkdir -p -m 0600 ~/.ssh && \
    ssh-keyscan -H github.com bitbucket.org >> ~/.ssh/known_hosts
RUN --mount=type=ssh pip install git+ssh://git@github.com/RATESResearch/REONapp
RUN pip install -r /usr/src/geonode/requirements.txt
#RUN pip install invoke

# FROM builder AS rgvflood

WORKDIR = /usr/src/geonode

RUN pwd && ls -alh /usr/src/geonode/
COPY settings.py /usr/src/geonode/geonode/
COPY base.html /usr/src/geonode/geonode/templates/
COPY urls.py /usr/src/geonode/
COPY logo.png /usr/src/geonode/geonode/static/geonode/img/2021/12/
COPY background.jpg /usr/src/geonode/geonode/static/geonode/img/2021/12/
COPY theme.json /usr/src/geonode/
WORKDIR = /usr/src/geonode
RUN cd /usr/src/geonode && ls -alh
RUN cd /usr/src/geonode && python manage.py loaddata /usr/src/geonode/theme.json
RUN cd /usr/src/geonode && python manage.py makemigrations --noinput
RUN cd /usr/src/geonode && python manage.py migrate --noinput
RUN cd /usr/src/geonode && python manage.py collectstatic --noinput
# # Export ports
EXPOSE 8000

# We provide no command or entrypoint as this image can be used to serve the django project or run celery tasks
# ENTRYPOINT /usr/src/geonode/entrypoint.sh
