#!/bin/sh

#!/usr/bin/env sh

set -o errexit
set -o nounset

readonly cmd="$*"

kafka_ready () {
  # Check that postgres is up and running on port `5432`:
  dockerize -wait "tcp://${BOOTSTRAP_SERVERS}"  -timeout 10s
}

# We need this line to make sure that this container is started
# after the one with postgres, redisuntil kafka_ready; do
                                    #  >&2 echo 'kafka is unavailable - sleeping'
                                    #done and elastic


# It is also possible to wait for other services as well: redis, elastic, mongo
>&2 echo 'kafka is up - continuing...'

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd

gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000