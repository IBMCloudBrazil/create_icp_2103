FROM ubuntu:16.04
RUN apt-get update
RUN apt-get -y install locales
RUN rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y install ansible python
RUN apt-get -y install python-pip vim
RUN pip install softlayer

RUN mkdir -p /workdir
RUN mkdir -p /workdir/playbook
#RUN mkdir -p /workdir/config
RUN mkdir -p /etc/ansible/modules

WORKDIR /workdir

COPY ./config/ansible.cfg /etc/ansible/ansible.cfg
COPY ./config/sl_vm.py /etc/ansible/modules/sl_vm.py
COPY ./playbook/. /workdir/playbook
#COPY ./config/ /workdir/config
COPY . /workdir
