# 是否开启windows身份认证，默认关闭
is_auth_enable = False

# 数据库信息，下面包含了必须修改的参数
host = "xxx.xxx.xxx.xxx"
user = "xx"
password = "xxxx"
database = "xxxx"
timeout = 0
login_timeout = 60
charset = "UTF-8"
as_dict = True
port = "1433"
autocommit = True


# excel信息
file_ext = "xlsx"
file_name = "excel"
sheet_name = "test"
# 文件夹
sub_dir = "sub_dir"

# SQL与参数
query_statement = 'SELECT x,y FROM table_a JOIN table_b ON table_a.z = table_b.z WHERE table_a.x>=%s AND table_a.y LIKE %s'
query_parameter = ('2023-6-1', '%test%data')
# 是否启用查询参数
is_param_use = True

# 终端输出消息
success_info = "Generated Successfully"
fail_info = "Generated failed"