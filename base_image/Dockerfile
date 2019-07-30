FROM python:3.7.4-stretch

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt ./

RUN python3 -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

