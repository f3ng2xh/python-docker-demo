# python-docker-demo
通过三个示例演示 python docker 使用

## crontab
演示如何创建一个离线脚本镜像

## service
演示如何创建一个在线服务镜像

## base_image
演示如何构建一个自定义依赖包镜像

## 有用的命令
```
// 构建镜像
docker build -t demo/python-xxx-demo:v2019-07-31 .

// 执行
docker run -p 5000:5000 demo/python-xxx-demo:v2019-07-31

// 自定义执行文件
docker run -it --rm -v `pwd`:/app demo/python-base-demo:v2019-07-31 python3 /app/main.py --start_time 1000

// bash 进入容器内部
docker run --rm -it demo/python-xxx-demo:v2019-07-31 /bin/bash
```
