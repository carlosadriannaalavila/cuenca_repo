#Developer Carlos Adrian Naal Avila
#Date: 20/Oct/2019

import sys
import sqlalchemy as db
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

R = 0
S = 8
k = 1
rows = []
Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = None
#connection = engine.connect()


class Register_Solutions(Base):
    __tablename__ = "NQSolutions"
    global db
    id = db.Column(db.Integer, primary_key=True)
    solutions = db.Column(db.String)


def notUnderAttack(nxnboard, row, col):

    for i in range(col):
        if (nxnboard[row][i]):
            return False

    i = row
    j = col
    while i >=0 and j >= 0 :
        if (nxnboard[i][j]):
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while j >= 0 and i < N:
        if (nxnboard[i][j]):
            return False
        i = i + 1
        j = j - 1

    return True

def printBoard(nxnboard):
    global k
    global engine
    global connection
    global DBSession
    solution = ""
    current = k
    k = k + 1
    for i in range(N):
        for j in range (N):
            solution = solution + str(nxnboard[i][j])
        solution = solution + "\n"
    solution = solution + "\n"
    
    register_solution = Register_Solutions()
    register_solution.id = current
    register_solution.solutions = solution
    DBSession.add(register_solution)
    if k % 20000 == 0:
        DBSession.flush()
        DBSession.commit()


def solveProblem(nxnboard, col):
    if (col == N):
        printBoard(nxnboard)
        return True
        
    res = False
    for i in range(N):
        if (notUnderAttack(nxnboard, i , col)):
            nxnboard[i][col] = 1
            res = solveProblem(nxnboard,col+1) or res
            nxnboard[i][col] = 0
    return res

def reset_variables(nQueen):
    global R
    global S
    global k
    R = 0
    S = int(nQueen)
    k = 1

def init_alchemy():
    global engine
    global DBSession
    global Base
    dbname='postgresql+psycopg2://cuenca:mycu3nc4Us3r@localhost:5433/mydb'
    engine = db.create_engine(dbname, echo=False)
    DBSession.remove()
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def compute(nQueen):
#Step 1: Defining n values
    start = time.time()
    reset_variables(nQueen)
    global N
    global engine
    N = int(nQueen)
    init_alchemy()
    nxnboard = [
        [0 for j in range (N)]
        for i in range(N)]
    if(solveProblem(nxnboard, 0) == False):
        return
    global DBSession
    DBSession.flush()
    DBSession.commit()
    end = time.time()
    print("Numero de Reinas: %s. Tiempo Transcurrido para %f"% (nQueen,end - start))
    return k-1

#Start
#if __name__ == 'main':

compute(12)