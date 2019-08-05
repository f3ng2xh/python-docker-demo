FROM ubuntu:16.04
RUN apt-get update \
 && apt-get install -y --no-install-recommends openssh-server sudo python3 python3-pip supervisor \
 && apt-get clean

RUN mkdir /var/run/sshd \
 && sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
 && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN echo 'root:root' | chpasswd \
 && useradd -m work \
 && usermod -a -G sudo work \
 && echo 'work:work' | chpasswd

ADD app.conf /etc/supervisor/conf.d/services.conf

RUN mkdir -p /app
WORKDIR /app
ADD requirements.txt app.py ./
RUN python3 -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["/usr/bin/supervisord", "-n"]
