FROM python:3-stretch
MAINTAINER Steve Bruggeman

VOLUME /src
COPY pwrstat-api.py requirements.txt PPL-*-64bit.deb  powerpanel_*_amd64.deb init.sh /src/
WORKDIR /src
RUN chmod +x /src/init.sh
RUN chmod +x /src/pwrstat-api.py
RUN pip install --trusted-host pypi.python.org -r requirements.txt
<<<<<<< HEAD
RUN dpkg -i powerpanel_*_amd64.deb
=======
RUN dpkg -i *.deb
>>>>>>> 8180675f3b3ab7aee870ce8ee32e007a9ca8a0e8
ENTRYPOINT "/src/init.sh"
