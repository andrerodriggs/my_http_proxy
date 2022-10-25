## Instructions to activate the HTTP Proxy with JWT token delivery

*1) Clone this repo*

*2) Run docker-compose up -d --build* 

*3) Access the http://fastapi.localhost:8008/docs*

*4) In this URL click on GET and then click on "Try it out" buttom in the left"*

*5) Click in the Excecute blue buttom*

*6) Copy the token string without the "" signs*

*7) In the POST area paste the token string in the token field and click "Execute"*

*8) Check the Server response area*

*9) You can test via cURL as well: curl -H Host:fastapi.localhost http://0.0.0.0:8008/docs*

*10) To access the dashboard, go to http://fastapi.localhost:8081/*
