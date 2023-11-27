#!/bin/bash

pip install --no-cache-dir fastapi uvicorn aiohttp asyncio requests psycopg psycopg-binary

if [ ! -f "/lib/systemd/system/fapi.service" ]; then
	sudo -i cp /opt/cicd/src/files/fapi.service /lib/systemd/system/fapi.service
	sudo -i systemctl enable fapi.service
fi

sudo -i systemctl restart fapi.service
