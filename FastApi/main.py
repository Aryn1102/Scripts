from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello world"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/students/{student_id}")
def get_student(student_id:int):
    return {"student id": student_id}

@app.get("/students")
def get_students(branch: str):
    return {"branch": branch}


"""
Interview Questions

Answer these without looking back.

Q1.
What is an API?
Api stands for appllication programming interface which acts as the medium of communication between two different softwares.

Q2. ⭐
What is the difference between an API and an endpoint?
endpoint is th final location the api points to and api is the medium of communication between different softwares
An endpoint is a specific API operation exposed at a particular path and HTTP method.

Q3.
What is HTTP?
it is a protocol to transfer data between two seperate entities namely client and server

Q4.
What are GET and POST generally used for?
get retrives data from server to client while post accepts data from client and sends to server

Q5. ⭐
Why would an ML prediction endpoint commonly use POST rather than GET?
to give input to the model we use POST

Q6.
What is an HTTP status code?
A status code is a numeric code in the HTTP response that indicates the result/status of the request.
Q7.
What does 200 OK generally mean?
200 OK means the request was successfully processed.

Q8.
What is a path parameter?
Given:
/students/22
what is 22?
path parameter is the data given to reach the endpoint and send the response

Q9.
What is a query parameter?
Given:
/students?branch=IT
what is branch=IT?
query paraneter is a filter given to filter out the required data and send the response

Q10. ⭐⭐⭐
Explain this code line by line:
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
    return {"status": "healthy"}
Your explanation should include:
FastAPI()
app
@app.get()
/health
health()
response
the first line imports the  fastapi application
second line is creating a instance of the application fastapi named app
@app.get("/health") is a route decorator that registers the health() function as the handler for GET /health.
It's not itself the endpoint function.
fourth & fivth line is the function that will be returned
"""

"""
Create:
GET /
that returns:
{
    "message": "Welcome to my ML API"
}
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def message():
    return {
    "message": "Welcome to my ML API"
}
"""

""" 
Create:
GET /health
that returns:
{
    "status": "healthy"
}

from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
    return {
    "status": "healthy"
}
"""

""" 
Create:
GET /model-info
Return:
{
    "model": "logistic_regression",
    "version": "1.0"
}
from fastapi import FastAPI
app = FastAPI()
@app.get("/model-info")
def model_info():
    return {
    "model": "logistic_regression",
    "version": "1.0"
}
"""

""" 
Your eventual project will expose:
POST /predict
The client will send:
{
    "cgpa": 7.5,
    "experience": 2,
    "branch": "IT"
}
Explain without implementing it yet what should happen between the request arriving and the prediction being returned.
Think in terms of:
request
→ validation
→ preprocessing
→ model
→ prediction
→ response
client will send the request POST with data to the endpoint
the data will be validated whether it is Json format and required data
after validation the data will reach the endpoint /predict
the function below will be called and the input data will be passed as parameter
the function will preprocess the data clean, transform, 
give the preprocessed data to model
model makes the prediction and returns the response back to api

"""