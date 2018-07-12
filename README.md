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

# 部署

支持Docker部署
