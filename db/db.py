import pymssql
import logging
from config import *


def auth_connection():
    return pymssql.connect(server=host, database=database)


def password_connection():
    return pymssql.connect(server=host,
                           user=user,
                           password=password,
                           database=database,
                           timeout=timeout,
                           charset=charset,
                           as_dict=as_dict,
                           port=port,
                           autocommit=autocommit
                           )


# 获取数据库连接
def get_connection():
    if is_auth_enable:
        return auth_connection()
    else:
        return password_connection()


# 查询数据，比如直接 cursor.execute('select * from usrTBTS')
def query_data() -> list[dict]:
    connection = get_connection()
    cursor = connection.cursor()
    if len(query_statement) == 0 or query_parameter is None:
        logging.error('查询语句为空！')
        return []
    if not is_param_use:
        cursor.execute(query_statement)
    else:
        if query_statement is None or len(query_parameter) == 0:
            logging.error('参数形式错误')
        else:
            cursor.execute(query_statement, query_parameter)
    data = []
    row = cursor.fetchone()
    while row:
        data.append(row)
        row = cursor.fetchone()
    connection.close()
    return data
