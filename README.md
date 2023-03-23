This Project is my end of year holberton project. <br>

The idea of the project is to make a chatting application which is user <br>
friendly and connects people together. 

<strong>tic</strong> is hosted in two repositories, this repository is based on the backend api implementation <br>
of the application. 
<br>
<h1>How to Use This repo </h1>
fork the repo and run <br>

<code>pip install -r requirements.txt </code> <br> 

To install the necessary dependencies <br>
then go ahead and run  django development server with the command below<br>

<code>python3 manage.py runserver </code> <br>

This API allows users to create, view, and update user accounts.

<h1>Endpoints</h1> <br>
Create User <br>
Endpoint: 
/api/create_user/

<strong>Method: <strong> 
POST

Request body:
<br>
{ <br>
    "first_name": "John", <br>
    "last_name": "Doe", <br>
    "email": "johndoe@example.com",<br>
    "password": "password"<br>
}<br>

<br>
Response body:
 <br>
{ <br>
    "id": 1, <br>
    "first_name": "John", <br>
    "last_name": "Doe", <br>
    "email": "johndoe@example.com" <br>
}<br>
<br>
  
  
 <h1>List Users </h1>
Endpoint: 
/api/list_users/

 <strong>Method: </strong> 
GET

Response body:
<br>
[<br>
    {<br>
        "id": 1,<br>
        "first_name": "John",<br>
        "last_name": "Doe",<br>
        "email": "johndoe@example.com"<br>
    },<br>
    {<br>
        "id": 2,<br>
        "first_name": "Jane",<br>
        "last_name": "Doe",<br>
        "email": "janedoe@example.com"<br>
    }<br>
]<br>
  <br>
 <h1>Authenticate User</h1> <br>
Endpoint:  <br>
/api/authenticate_user/
<br>
  <strong>Method:</strong> 
POST

Request body:<br>
<br>
{<br>
    "email": "johndoe@example.com",<br>
    "password": "password"<br>
}<br>
  
  <br>
Response body:

{<br>
    "name": "John Doe",<br>
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6ImpvaG5kb2VAdGVzdC5jb20iLCJleHAiOjE1NzUyMzI3MzJ9.0H1_Q-NgYjB5q3xIjnX9S5E5XyG-f8Kj-L4h4t4pfZ8"<br>
}<br>
  
<br>
Retrieve Update User
Endpoint: 
/api/retrieve_update_user/

Method: 
PUT, GET

Request body:<br>

{<br>
    "first_name": "John",<br>
    "last_name": "Doe",<br>
    "email": "johndoe@example.com",<br>
    "password": "password"<br>
}
  
  <br>
Response body:
    
{<br>
    "id": 1,<br>
    "first_name": "John",<br>
    "last_name": "Doe",<br>
    "email": "johndoe@example.com"<br>
}<br>
