__author__ = 'xiangcy123a'

import asyncio, logging

import aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),

    )