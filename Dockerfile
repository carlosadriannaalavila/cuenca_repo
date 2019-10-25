FROM python:3
ADD n_queen_cn.py /
ADD n_queen_test.py /
RUN pip3 install SQLAlchemy
RUN pip3 install -U pytest
RUN pip3 install psycopg2-binary
CMD ['"docker pull postgres"]
CMD ["sudo docker-compose up -d"]
CMD ["psql -h localhost -p 54320 -U cuenca -d mydb"]
CMD ["pytest", "./n_queen_test.py"]
