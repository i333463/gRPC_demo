FROM python:3

FROM base as builder

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

