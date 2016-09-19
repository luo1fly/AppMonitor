#!/usr/bin/env python
# Name: index.py.py
# Time:9/19/16 9:08 AM
# Author:luo1fly

import json
from multiprocessing import Pool
from core.main import call
# import custom modules above


if __name__ == '__main__':
    with open('conf/api.json') as f:
        apps = json.load(f)
    pool = Pool(processes=4)
    for app_name, args_body in apps.items():
        pool.apply_async(call, (app_name, args_body))
    pool.close()
    pool.join()
