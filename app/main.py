from pyexpat import model
from fastapi import Depends, FastAPI, HTTPException,Response
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Call(BaseModel):
    user_name : str
    call_duration : int
    call_count : int
    block_count : int

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'Vin', user = 'postgres',
                    password = 'postgres',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successfull")
        break
    except Exception as error:
        print("Connection failed")
        print("Erorr" ,error)
        time.sleep(2)


@app.get("/")
def root():
    return {"Hello to my project"}



@app.get("/mobile")
def get_all():
    cursor.execute(""" SELECT * FROM test""")
    result =cursor.fetchall()
    return {"data ": result}


@app.post("/moblie",status_code=201)
def creat_call(call : Call, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO test (user_name,call_duration,call_count,block_count) VALUES (%s,%s,%s,%s) RETURNING * """,
    #         (call.user_name, call.call_duration, call.call_count, call.block_count))
    # call_person = cursor.fetchone()
    # conn.commit()

    new_call = models.Call(user_name = call.user_name, call_duration=call.call_duration,call_count=call.call_count, block_count=call.block_count)
    db.add(new_call)
    db.commit()
    db.refresh(new_call)
    return {"new_call is": new_call}


@app.get("/moblie/{user_name}")
def get_call(user_name : str, db : Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM test WHERE user_name = %s """,(str(user_name)))
    # test_call = cursor.fetchone()
    # print(test_call)
    new_call = db.query(models.Call).filter(models.Call.user_name == user_name).all()
    if new_call == None :
        raise HTTPException(status_code=404,detail=f"call with {user_name} was not found")
    return {"call_detail" : new_call}

@app.put("/moblie/{user_name}/call")
def update_duration(user_name : str,call : Call , db :Session= Depends(get_db)):
    update_call = db.query(models.Call).filter(models.Call.user_name == user_name)

    if update_call.first() == None :
        raise HTTPException(status_code=404, detail=f"call with user_name {user_name} does exist")
    
    update_call.update(call_duration =+ call.call_duration,synchronize_session=False)
    db.commit()
    
    temp = 0
    if call.call_duration>0 and call.call_duration %30 != 0 :
        temp = call.call_duration / 30 + 1
    if call.call_duration>0 and call.call_duration %30 == 0 :
        temp = call.call_duration / 30
    update_call.update(block_count=+temp,call_count =+1 ,synchronize_session=False)
    db.commit()
    return {"call_duration": update_call}

@app.get("/moblie/{user_name}/billing")
def get_billing(user_name : str, db : Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM test WHERE user_name = %s """,(str(user_name)))
    # test_call = cursor.fetchone()
    # print(test_call)
    billing = db.query(models.Call.call_count,models.Call.block_count).filter(models.Call.user_name == user_name).all()
    if billing == None :
        raise HTTPException(status_code=404,detail=f"call with {user_name} was not found")
    return {"billing" : billing}
