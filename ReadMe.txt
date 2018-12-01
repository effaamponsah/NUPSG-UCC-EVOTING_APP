Organization of the project


Documentation of the Voting App
Dennis Effa Amponsah


This system was implemented using the flask python microframework.
Click here to read about flask microframework.
The database used is sqlite. Click here to read the documentation of sqlite.
Sql alchemy is also used to 
Added is a picture of the database schema diagram.
Sqlite database was used bacuase it is easy to carry around and doesnt need a local
server to view the app.




Most of the data is fetched from the database. With the exception
of the data that is rendered in the html templates.
The data is faked to be coming from a server(jsonfified).
Data was not fetched directly from the database due to code optimization



Users are approached with the first screen which is the login screen.
Which is based there is a query into the database to see whether there is 
an index number such as that. The user is authenticated based when there is 
an index numbr in it or is bounced when there is no instance of the User
Sessions are used for the authentication. The sessions are based on the 
index numbers. Session is set to true when there is an existing user in the 
database.
The session is set to false when the user clicks the logout which sets the 
session to false and redirects to the index function which checks 
the session



Cookies are used to check whether the user is already voted or hasnt.
Take a look at cookies if you are new to it.
The cookies are set based on the users index number provided.
If there is a cookie set for that index number, the user is redirected to 
the error page else the user is redirected to the voting page.



The admin route enables users to register.


On sign in, some data is fetched such as the wing name, hall of affiliation
and the current residence as global variables and are in future routes.


Login is handled by