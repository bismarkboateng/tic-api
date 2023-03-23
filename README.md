This Project is my end of year holberton project. <br>

The idea of the project is to make a chatting application which is user <br>
friendly and connects people together. 

<strong>tic</strong> is hosted in two repositories, this repository is based on the backend api implementation <br>
of the application. 


This API allows users to create, view, and update user accounts.

<h1>Endpoints</h1> <br>
Create User <br>
Endpoint: 
/api/create_user/

<strong>Method: <strong> 
POST

Request body:

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "password": "password"
}

<br>
Response body:

{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com"
}
<br>
  
  
 <h1>List Users </h1>
Endpoint: 
/api/list_users/

 <strong>Method: </strong> 
GET

Response body:

[
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com"
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "janedoe@example.com"
    }
]
  <br>
 <h1>Authenticate User</h1> <br>
Endpoint:  <br>
/api/authenticate_user/
<br>
  <strong>Method:</strong> 
POST

Request body:

{
    "email": "johndoe@example.com",
    "password": "password"
}
  
  <br>
Response body:

{
    "name": "John Doe",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6ImpvaG5kb2VAdGVzdC5jb20iLCJleHAiOjE1NzUyMzI3MzJ9.0H1_Q-NgYjB5q3xIjnX9S5E5XyG-f8Kj-L4h4t4pfZ8"
}
  
<br>
Retrieve Update User
Endpoint: 
/api/retrieve_update_user/

Method: 
PUT, GET

Request body:

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "password": "password"
}
  
  <br>
Response body:
    
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com"
}
