# wine_inventory

Special thanks to Miguel Grinberg for putting together excellent tutorials on flask/flask_restful:
https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful

This is a simple app for keep track of your wine inventory, with the ability to add notes and searchable tags.

There are essentially 3 parts:

## Backend (python 3.X)

    GET /wine_list/api/v1.0/winelist (get all wines)
    GET /wine_list/api/v1.0/winelist/{id} (get info on specific wine)
    POST /wine_list/api/v1.0/winelist (add new wine info)
    PUT /v1.0/wine/{id} (update wine info) (not implemented yet)
    PATCH /wine_list/api/v1.0/winelist/{id} (update wine info)
    DELETE /wine_list/api/v1.0/winelist/{id} (delete specific wine)

Use 

`pip3 install -r backend/requirements.txt`

to install all the backend required python modules

    
## Frontend (web/react)

A no-SQL DB.

    No SQL was choosen so that adding fields is easy(er).
    
    