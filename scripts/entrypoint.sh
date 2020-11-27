#!/bin/bash

while ! nc -zvw3 postgres 5432; do echo waiting for Postgres; sleep 30; done;
echo "Postgres is up"

exec guicorn wsgi:app --host 0.0.0.0 --port 5000