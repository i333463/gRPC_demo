FROM python:3

# download the grpc health probe
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.0 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

# get packages
WORKDIR /register
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

# set listen port
ENV PORT "50051"
EXPOSE 50051

ENTRYPOINT ["python", "/register/register_server.py"]

