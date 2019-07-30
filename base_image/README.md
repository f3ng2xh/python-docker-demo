# base_image
构建自定义 python 依赖

```
// 构建基础镜像
docker build -t demo/python-base-demo:v2019-07-31 .
// 进入容器内部检验是否正确
docker run -it --rm demo/python-base-demo:v2019-07-31 /bin/bash
```
