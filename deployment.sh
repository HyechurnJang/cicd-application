#!/bin/bash

pip install --no-cache-dir fastapi uvicorn aiohttp asyncio requests psycopg psycopg-binary

cd /opt/cicd/src; python