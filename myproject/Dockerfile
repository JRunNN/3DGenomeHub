# 建立 python 3.9环境
FROM python:3.11


# change source
RUN echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib\n" \
         "deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib\n" \
         "deb http://mirrors.aliyun.com/debian-security buster/updates main\n" \
         "deb-src http://mirrors.aliyun.com/debian-security buster/updates main\n" \
         "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib\n" \
         "deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib\n" \
         "deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib\n" \
         "deb https://mirrors.aliyun.com/debian-security bookworm-security main contrib non-free non-free-firmware" \
         "deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" > /etc/apt/sources.list
# RUN echo > /etc/apt/sources.list
# RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

# 安装netcat
# RUN apt-get update
# RUN apt install -y netcat-traditional
# RUN apt-get install bedtools
# RUN apt-get install tabix -y

# 设置 python 环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 可选：设置镜像源为国内
COPY pip.conf /root/.pip/pip.conf

# 容器内创建 myproject 文件夹
ENV APP_HOME=/var/www/html/myproject
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# 将当前目录加入到工作目录中（. 表示当前目录）
ADD . $APP_HOME

# 更新pip版本
RUN /usr/local/bin/python -m pip install --upgrade pip

# 安装项目依赖
RUN pip install -r requirements.txt

# ENV DJANGO_ENV development

# 移除\r in windows
RUN sed -i 's/\r//' ./start.sh

# 给start.sh可执行权限
RUN chmod +x ./start.sh

# 数据迁移，并使用uwsgi启动服务
ENTRYPOINT /bin/bash ./start.sh