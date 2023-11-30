# -*- coding: utf-8 -*-
'''
   ____  _____  ______ _____             
  / __ \|  __ \|  ____|  __ \     /\     
 | |  | | |__) | |__  | |__) |   /  \    
 | |  | |  ___/|  __| |  _  /   / /\ \   
 | |__| | |    | |____| | \ \  / ____ \  
  \____/|_|    |______|_|  \_\/_/    \_\ 

@author: VMware Korea CMP TF
'''

#===============================================================================
# Import
#===============================================================================
import json
from fastapi import FastAPI, Request
from common import getConfig, Logger
from views import View

#===============================================================================
# SingleTone
#===============================================================================
config = getConfig('../deployment.ini')
Logger.register(config)
app = FastAPI(title='App Module')
view = View(config)


@app.on_event('startup')
async def runStartUp():
    await view.startup()


@app.on_event('shutdown')
async def runShutDown():
    await view.shutdown()


#===============================================================================
# Interfaces
#===============================================================================
@app.get('/helloworld')
async def getHelloWorld() -> dict:
    return await view.getHelloWorld()

@app.get('/messages')
async def getMessageList() -> list:
    return await view.getMessageList()

@app.post('/messages')
async def createMessage(request:Request) -> dict:
    data = json.loads(await request.body())
    return await view.createMessage(**data)

@app.put('/messages/{id}')
async def updateMessage(request:Request, id:str) -> dict:
    data = json.loads(await request.body())
    data['id'] = id
    return await view.updateMessage(**data)

@app.delete('/messages/{id}')
async def deleteMessage(id:str) -> dict:
    return await view.deleteMessage(id)
    
@app.get('/workload/{weight}')
async def getWorkload(weight:int) -> dict:
    return await view.getWorkload(weight)