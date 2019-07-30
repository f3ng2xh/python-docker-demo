# service
在线服务示例项目，项目依赖 flask 启动，注意主文件下 port 的设置。

```
docker build -t demo/python-service-demo .
docker run --rm -p 5000:5000 demo/python-service-demo
```
