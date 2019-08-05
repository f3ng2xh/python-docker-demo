FROM ubuntu:16.04
RUN apt-get update \
 && apt-get install -y --no-install-recommends openssh-server sudo python3 python3-pip \
 && apt-get clean

RUN mkdir /var/run/sshd \
 && sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
 && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN echo 'root:root' | chpasswd \
 && useradd -m work \
 && usermod -a -G sudo work \
 && echo 'work:work' | chpasswd
CMD ["/usr/sbin/sshd", "-D"]
