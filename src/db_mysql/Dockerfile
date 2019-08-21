FROM python:3

WORKDIR /db_mysql

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add files into working directory
COPY . .

EXPOSE 3000

ENTRYPOINT ["python", "/db_mysql/app.py"]