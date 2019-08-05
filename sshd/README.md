# sshd 
docker 虚拟linux主机
```
// 启动 ubuntu 主机
docker run -d -p 2222:22 demo/ubuntu-sshd

// 登录 
// 默认密码 root:root work:work
ssh root@localhost -p 2222

```
