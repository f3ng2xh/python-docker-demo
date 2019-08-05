# python-sshd 运行环境
支持在线服务和sshd直接登录

```
// 构建 && 运行
docker build -t demo/python-app-sshd .
docker run -d -p 2222:22 -p 5000:5000 demo/python-app-sshd

// 访问
ssh root@localhost -p 2223
curl http://localhost:5000/
```
