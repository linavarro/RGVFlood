FROM reon/buster:v1.0
LABEL GeoNode development team

RUN mkdir -p /usr/src/geonode

# add bower and grunt command
# https://github.com/GeoNode/geonode.git
# RUN cd /usr/src && pip install git+https://github.com/GeoNode/geonoge.git@3.3.0#egg=geonode
#COPY . /usr/src/geonode/
RUN git clone -b 3.3.0 https://github.com/GeoNode/geonode /usr/src/geonode

WORKDIR /usr/src/geonode

COPY monitoring-cron /etc/cron.d/monitoring-cron
RUN chmod 0644 /etc/cron.d/monitoring-cron
RUN crontab /etc/cron.d/monitoring-cron
RUN touch /var/log/cron.log
RUN service cron start

COPY wait-for-databases.sh /usr/bin/wait-for-databases

COPY tasks.py /usr/src/geonode/
COPY entrypoint.sh /usr/src/geonode/
COPY requirements.txt /usr/src/geonode/

RUN chmod +x /usr/bin/wait-for-databases
RUN chmod +x /usr/src/geonode/tasks.py \
    && chmod +x /usr/src/geonode/entrypoint.sh

COPY celery.sh /usr/bin/celery-commands
RUN chmod +x /usr/bin/celery-commands

COPY celery-cmd /usr/bin/celery-cmd
RUN chmod +x /usr/bin/celery-cmd

# Install "geonode-contribs" apps
RUN cd /usr/src; git clone https://github.com/GeoNode/geonode-contribs.git -b master
# Install logstash and centralized dashboard dependencies
RUN cd /usr/src/geonode-contribs/geonode-logstash; pip install --upgrade  -e . \
    cd /usr/src/geonode-contribs/ldap; pip install --upgrade  -e .

RUN pip install --upgrade --no-cache-dir  --src /usr/src -r requirements.txt
RUN ls -alh .
RUN pip install --upgrade  -e .

RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput
