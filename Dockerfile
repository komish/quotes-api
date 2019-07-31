FROM python:3

WORKDIR /home/quotes

COPY app/* /home/quotes/

RUN cp -a docker-entrypoint.sh /usr/local/bin
RUN pip install -r requirements.txt
RUN ln -s /usr/local/bin/docker-entrypoint.sh / # backwards compat

ENTRYPOINT ["docker-entrypoint.sh"]