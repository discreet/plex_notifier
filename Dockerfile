FROM ubuntu:16.04
MAINTAINER discr33t <cpisano86@gmail.com>

ARG PLEX_USERNAME
ARG PLEX_PASSWORD
ARG PLEX_SERVER
ARG DAYS_PASSED=7
ARG SEND_MAIL=false
ARG EMAIL_USERNAME
ARG EMAIL_PASSWORD
ARG UNSUB_EMAILS

ENV GITHUB="https://github.com"
ENV TUSK_VER="0.3.2"
ENV NOTIFIER_VER="v0.2.0"

RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN wget ${GITHUB}/rliebz/tusk/releases/download/v${TUSK_VER}/tusk_${TUSK_VER}_linux_amd64.deb
RUN sudo dpkg -i tusk_${TUSK_VER}_linux_amd64.deb
RUN wget ${GITHUB}/co-llabs/plex_notifier/archive/${NOTIFIER_VER}.tar.gz

