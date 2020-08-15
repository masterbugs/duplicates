FROM python:3.7

RUN mkdir -p /opt/aqua

COPY main.py /opt/aqua
COPY sample_dir /opt/aqua/sample_dir

WORKDIR /opt/aqua

ENTRYPOINT ["python", "main.py"]
CMD ["."]
