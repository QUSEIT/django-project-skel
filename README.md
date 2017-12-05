# 环境
1. Django == 1.11
2. MySql 

# Python Module
1. MySQL-python 1.2.5


＃ 安装依赖包
pip install -r requirements.txt

#MySQL 字符集
CREATE DATABASE `djangoapp` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

# 运行
1. python manage.py makemigrations <appname> -- 初始化app
2. python manage.py migrate －－ 创建表
   import forms 报错解决：python manage.py migrate --fake models

3. python manage.py createsuperuser －－ 创建超级管理员
4. python manage.py runserver －－ 运行项目
5. python manage.py collectstatic －－静态资源自动整合

# Upgrade Django 2.0

1. pip install mysqlclient

2. ForeignKey : null=True, on_delete=models.SET_NULL

