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

import uvicorn
from common import getConfig


def handler(module):
    config = getConfig('../deployment.conf')
    
    uvicorn.run(
        'routes:app',
        host='0.0.0.0',
        port=int(config['application']['hostport']),
        reload=True,
        reload_dirs=[f'services/{module}']
    )
