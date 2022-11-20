FROM python:latest
RUN mkdir /automation
RUN apt-get update && apt-get -y install vim
COPY ./backend /automation/backend
COPY ./front /automation/front
COPY ./setup.py /automation
COPY ./conftest.py /automation
COPY ./pytest.ini /automation
WORKDIR /automation
RUN python setup.py install