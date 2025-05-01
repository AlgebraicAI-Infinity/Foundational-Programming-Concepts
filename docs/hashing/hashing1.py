import hashlib
import json
import os

# What is hashing ?
# Hashing is the way by which we scramble some original data to get some new value . This process is called hashing
# The function which performs this process is called hash function and the output is called hash value or Digest


# What is SHA-256 Algorithm ?
# It is a part of SHA2 family of algorithms . SHA stands for Secure Hash Algorithm
# you can learn more about here : https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm


DATABASE_PATH:str = 'data.json'
database: dict[str, str] = {}

if os.path.exists(DATABASE_PATH):
    with open(DATABASE_PATH,'r') as f:
        database = json.load(f)
else:
    database={}

def save_db() -> None :
    with open(DATABASE_PATH,'w') as f:
        json.dump(database,f)

# This hash function takes password as input
# It returns fixed size string of characters which appears random and mixed
# This prevents us to directly store the password in the database
def hash(password:str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# This function takes username and password as parameters
def insert_user(username:str,password:str) -> None :
    if username in database:
        print(f'{username} already exists in the database! ')
    else:
        database[username] = hash(password)
        save_db()
        print(f'{username} added successfully!')

# This function verifies the password 
def verify_user(username:str,password:str) -> None :
    if username in database:
        if database[username]==hash(password):
            print('User exists')
        else:
            print('Invalid password')
    else :
        print(f'{username} not found ')


if __name__=="__main__":
    insert_user('sharma','12@vivek')
    verify_user('sharma','1234')