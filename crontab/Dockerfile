FROM python:3.7.4-stretch

RUN mkdir -p /app
WORKDIR /app

ADD . ./

ENV PIPENV_VENV_IN_PROJECT true
ENV PIPENV_SKIP_LOCK true
RUN pip install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple && pipenv install -i https://pypi.tuna.tsinghua.edu.cn/simple 

CMD ["/app/.venv/bin/python", "main.py"] 

