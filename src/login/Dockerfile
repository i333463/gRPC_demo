FROM python:3

# get packages
WORKDIR /register
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

# set listen port
ENV PORT "50052"
EXPOSE 50052

ENTRYPOINT ["python", "/login/login_server.py"]