eval `ssh-agent -s`
ssh-add /srv/RGVFlood/.ssh/deploykey
COMPOSE_DOCKER_CLI_BUILD=1
DOCKER_BUILDKIT=1
docker-compose down -v --rmi local
docker-compose build geonode
DOCKER_BUILDKIT=1 docker build --no-cache --progress=plain --ssh default .
docker-compose up -d
