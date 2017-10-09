FROM hivesolutions/python:latest

LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8080

VOLUME /repos

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV MONGOHQ_URL mongodb://localhost
ENV REPOS_PATH /repos
ENV GITHUB_USERNAME GITHUB_USERNAME
ENV GITHUB_PASSWORD GITHUB_PASSWORD
ENV GA ""
ENV PYTHONPATH /src

ADD requirements.txt /
ADD extra.txt /
ADD src /src

RUN pip3 install -r /requirements.txt && pip3 install -r /extra.txt && pip3 install --upgrade netius

CMD ["/usr/bin/python3", "/src/proyectos/main.py"]
