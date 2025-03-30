FROM python:3-stretch
MAINTAINER Steve Bruggeman

VOLUME /src
COPY pwrstat-api.py download-helper.py requirements.txt init.sh /src/
WORKDIR /src
RUN chmod +x /src/init.sh
RUN chmod +x /src/pwrstat-api.py
RUN chmod +x /src/download-helper.py

# Implemented
ARG PORT=5002
# Not yet implemented, only Debian base, no Alpine or Red Hat.
ARG DISTRO=deb
ARG ARCHITECTURE=64

ENV PORT=${PORT} \
    DISTRO=${DISTRO} \
    ARCHITECTURE=${ARCHITECTURE}

# This gets the latest version of CyberPower PowerPanel
RUN python3 /src/download-helper.py

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN dpkg -i *.${DISTRO}
ENTRYPOINT "/src/init.sh"