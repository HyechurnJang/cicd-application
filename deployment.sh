#!/bin/bash
source .cicd/files/ini_parser.sh
process_ini_file "deployment.ini" > /dev/null

# Load Variables from INI ###################################################
workspace=$default_workspace

# Deployment Script Here ####################################################
pip install --no-cache-dir fastapi uvicorn aiohttp asyncio requests psycopg psycopg-binary 2>&1 > /dev/null

if [ ! -f "/lib/systemd/system/fapi.service" ]; then
	sudo -i cp $workspace/src/files/fapi.service /lib/systemd/system/fapi.service
	sudo -i systemctl enable fapi.service
fi

sudo -i systemctl restart fapi.service
