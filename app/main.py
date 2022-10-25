#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:50:27 2022

@author: andrerodrigues
"""

from fastapi import FastAPI, status, HTTPException, Request
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
import secrets

 
# replace it with your 32 bit secret key
SECRET_KEY = "a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf"
 
# encryption algorithm
ALGORITHM = "HS512"

# Pydantic Model that will be used in the
# token endpoint for the response
class Token(BaseModel):
    access_token: str
    token_type: str
 
 
# Initialise the app
# app = FastAPI(root_path="/api/v1")
app = FastAPI()

# app = FastAPI(
#     servers=[
#         {"url": "http://stag.example.com", "description": "Staging environment"},
#         {"url": "http://prod.example.com", "description": "Production environment"},
#     ],
#     root_path="/api/v1",
#     # root_path_in_servers=False,
# )


# this function will create the token
# for particular data
def create_access_token(data: dict):
    to_encode = data.copy()
     
    # expire time of the token
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({
        "exp": expire,
        'iat' : datetime.utcnow(),
        'jti' : secrets.token_urlsafe()
        })
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
     
    # return the generated token
    return encoded_jwt
 

# the endpoint to get the token
# @app.get("/get_token")
# async def get_token():
   
#     # data to be signed using token
#     data = {
#         'user': 'username',
#         'date': 'todays date'
#     }
#     token = create_access_token(data=data)
#     return {'token': token}

@app.get("/get_token")
async def get_token(request: Request):
   
    # data to be signed using token
    data = {
        'user': 'username',
        'date': 'todays date'
    }
    token = create_access_token(data=data)
    return {'token': token,
            # "root_path": request.scope.get("root_path")
            }


# the endpoint to verify the token
@app.post("/verify_token")
async def verify_token(token: str):
    try:
        # try to decode the token, it will
        # raise error if the token is not correct
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
