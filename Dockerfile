FROM python:3.9.6-alpine
RUN /bin/sh
RUN mkdir -p /path/to/workdir
WORKDIR /path/to/workdir
RUN python -m venv .
WORKDIR /path/to/workdir
RUN source bin/activate
RUN echo 'Copy the pip requirement to the workdir.'
COPY pip_requirement.install ./
RUN echo 'Build python env success.'
RUN pip3 install -r pip_requirement.install
RUN mkdir -p workspace
RUN echo 'Move the source files to the workdir.'
COPY ./workspace/* ./workspace/
ENV REMOTE_CHROME_DRIVER=http://192.168.6.150:4444/wd/hub
WORKDIR /path/to/workdir
CMD python workspace/trick_slideshow.py
RUN echo 'Run trick script success.'
