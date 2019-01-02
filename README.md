# 环境
1. Python3 + Django 2
2. PostgreSQL 

＃ 安装依赖包
pip install -r requirements.txt

# 开发模式
1. 编辑run.sh，替换真实的环境变量
2. bash run.sh

# 其他问题
1. python manage.py makemigrations <appname> -- 初始化app
2. python manage.py migrate －－ 创建表
   import forms 报错解决：python manage.py migrate --fake models

3. python manage.py createsuperuser －－ 创建超级管理员
4. python manage.py runserver －－ 运行项目
5. python manage.py collectstatic －－静态资源自动整合

# Docker启动
1. 编辑application/.env, 配置项目及数据库字段
2. 如数据库未初始化, 使用`make migrate` 进行初始化表
3. 使用`make up`启动docker compose
4. 如改动后未重新生成镜像, 可使用`make build`重新生成镜像容器

# Makefile 命令
- default 
- up 
    启动服务
- build 
    若修改了Dockerfile, 可通过该命令重建镜像
- stop 
    停止服务
- restart 
    重启服务
- down 
    删除已停止的容器
- migrate 
    将django数据表migrate至数据库
- log 
    查看容器日志输出
- enter_db
    进入数据库

# 项目详情:
项目模板结构为:

```
root
├── .docker
│   └── docker-compose.yml
├── .env
├── Makefile
├── README.md
└── application(Django项目根目录)
```

该例中使用docker-compose构建, 使用远程数据库, 数据库相关配置写在.env中, docker-compose.yml内容修改为如下

```
version: '3'

services:
  db:
    image: postgres
  backend:
    build: ../application
    env_file: ../.env
    command: gunicorn --reload apps.wsgi --timeout=30 --bind 0.0.0.0:$PORT --access-logfile -
    ports:
      - "$PORT:$PORT"
    depends_on:
      - db
```

其中services/backend/build字段为django项目路径, 如果填写的是本地路径则在该项目中存在Dockerfile文件, 除填写本地路径外还可填写远端Docker仓库的镜像名称.
