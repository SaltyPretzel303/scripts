FROM ubuntu:20.04

RUN apt update; \
	apt install openssh-server openssh-client -y

RUN useradd -r -s /bin/bash -g root -G sudo ssh_user

RUN echo 'ssh_user:ssh_password' | chpasswd

RUN service ssh start

ENTRYPOINT ['/bin/bash']
