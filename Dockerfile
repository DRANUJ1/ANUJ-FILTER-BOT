FROM python:3.11-slim
RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Anuj-filter-bot
WORKDIR /Anujfilter-bot
COPY start.sh /st-art.sh
CMD ["/bin/bash", "/start.sh"]
