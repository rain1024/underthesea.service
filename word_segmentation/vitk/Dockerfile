FROM sequenceiq/spark:1.6.0

RUN yum install -y wget

RUN cd /opt; wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo; sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo

RUN yum install -y apache-maven

RUN yum -y update

RUN yum install -y python-pip python-dev build-essential

RUN pip install cherrypy