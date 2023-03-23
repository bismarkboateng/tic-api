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

<br>
<h1> Endpoints </h1>
<table>
    <tr>
       <th> Method </th>
       <th> Endpoint </th>
       <th> Description </th>
    </tr>
    <tr>
       <td>POST</td>
       <td>/api/create_user/</td>
       <td>Endpoint to create a user</td>
    </tr>
    <tr>
       <td>GET</td>
       <td>/api/list_users/</td>
       <td>List all available users</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/api/authenticate_user/</td>
        <td>authenticating users</td
    </tr>
    <tr>
        <td>GET n PUT</td>
        <td>/api/retrieve_update_user/</td>
        <td>For retrieving a user and updating a user</td>
    </tr>
</table>
