FROM python:3
ADD n_queen_cn.py /
ADD n_queen_test.py /
RUN pip3 install SQLAlchemy
RUN pip3 install -U pytest
RUN pip3 install psycopg2-binary
RUN pip3 install docker-compose