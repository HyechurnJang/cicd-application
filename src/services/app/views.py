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
#==============================================================================
import asyncio
import datetime
from drivers import Table

#===============================================================================
# Variables
#===============================================================================


#===============================================================================
# Implement
#===============================================================================
class View:
    
    def __init__(self, config):
        self.config = config
    
    async def startup(self):
        self.db = await Table.initialize(
            self.config['application']['db_writer_ip'], # hostname
            self.config['application']['db_hostport'], # hostport
            self.config['application']['db_database'], # database
            self.config['application']['db_username'], # username
            self.config['application']['db_password'], # password
            'message', # table
            [
                ('id', 'pkey-default'),
                ('text', 'char')
            ])
    
    async def shutdown(self):
        pass
    
    async def getHelloWorld(self) -> dict:
        return {
            'message': 'Hello World!'
        }
    
    async def getMessageList(self) -> list:
        async with self.db.cursor() as cursor:
            result = await cursor.getRecords()
            result.reverse()
            return result
    
    async def createMessage(self, text, **kargs) -> dict:
        async with self.db.cursor() as cursor:
            await cursor.createRecord(text=text)
            await cursor.commit()
            return {
                'result': 'ok'
            }
    
    async def updateMessage(self, id, text, **kargs) -> dict:
        async with self.db.cursor() as cursor:
            await cursor.updateRecord(id=id, text=text)
            await cursor.commit()
            return {
                'result': 'ok'
            }
    
    async def deleteMessage(self, id) -> dict:
        async with self.db.cursor() as cursor:
            await cursor.deleteRecord(id=id)
            await cursor.commit()
            return {
                'result': 'ok'
            }
    
    async def getWorkload(self, weight:int) -> dict:
        count = 0
        until = 1000 * weight
        buff = 100
        stt = datetime.datetime.now()
        while True:
            _ = (((buff * buff) + (buff * buff) % buff) * buff) / buff
            count = count + 1
            if count > until: break
            await asyncio.sleep(0)
        end = datetime.datetime.now()
        return {
            'weight': weight,
            'stt': str(stt),
            'end': str(end),
            'dur': str(end - stt)
        }
