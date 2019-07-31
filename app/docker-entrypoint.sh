#!/usr/bin/env bash

set -e

test ! -z "${LISTEN_ADDRESS}" \
  && HOST_ARGS="--host ${LISTEN_ADDRESS}"

test ! -z "${LISTEN_PORT}" \
  && PORT_ARGS="--port ${LISTEN_PORT}"

uvicorn app:app ${HOST_ARGS} ${PORT_ARGS}