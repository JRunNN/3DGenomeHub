#!/bin/bash
# 从第一行到最后一行分别表示：
# 1. 等待MySQL服务启动后再进行数据迁移。nc即netcat缩写
# 2. 收集静态文件到根目录static文件夹，
# 3. 生成数据库可执行文件，
# 4. 根据数据库可执行文件来修改数据库
# 5. 用 uwsgi启动 django 服务
# 6. tail空命令防止web容器执行脚本后退出
# while ! nc -z db 3306 ; do
#     echo "Waiting for the MySQL Server"
#     sleep 3
# done

python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
# uwsgi --ini /var/www/html/myproject/uwsgi.ini&&
if [ "$CONTAINER_ROLE" = "django" ]; then
    # Start the Django UWSGI server if in production, otherwise use the development server
    if [ "$DJANGO_ENV" = 'production' ]; then
        uwsgi --ini /var/www/html/myproject/uwsgi.ini
    else
        python manage.py runserver 0.0.0.0:8000
    fi
elif [ "$CONTAINER_ROLE" = "celery" ]; then
    # Start the Celery worker using the app's settings module
    celery -A myproject worker --loglevel=info
else
    echo "No or incorrect CONTAINER_ROLE set. Exiting."
    exit 1
fi
tail -f /dev/null

exec "$@"