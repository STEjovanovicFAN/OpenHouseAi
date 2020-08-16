# Open House AI API Test 

Open House coding test 

## Installation

Download python, can be done [here](https://www.python.org/downloads/).

Next use pip to install flask with this command:
```bash
pip install flask 
```

## To Run
In the project work directory run on the cmd:
```bash
python api.py 
```

Navigate to default page [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## API End Points

### GET 

First one is [http://127.0.0.1:5000/api/v1/resources/user/all](http://127.0.0.1:5000/api/v1/resources/user/all)

This endpoint retrieves all the user entities of the database. It takes no additional params and is primarily for sanity testing the POST request to input user entities into the database.

Second one is [http://127.0.0.1:5000/api/v1/resources/action/all](http://127.0.0.1:5000/api/v1/resources/action/all)

This endpoint retrieves all the action entities of the database. It takes no additional params and is primarily for sanity testing the POST request to input action entities into the database.


**Third one is** [http://127.0.0.1:5000/api/v1/resources/logdump](http://127.0.0.1:5000/api/v1/resources/logdump)

This endpoint is the solution to the whole coding test you guys gave out. It serves to extract logs based on specified param(s) and outputted in the desired format. It takes in four optional params can be of any combination:

- userId : specify a userId you want to retrieve logs of
- logType : specify the log type you want to retrieve logs of
- lowerTimeRange : specify the lower time range of log time stamps that are equal to or greater than the specified time (note time format is of YYYY-MM-DD HH:MM:SS , example: "2020-08-15 21:56:54")
- upperTimeRange : specify the upper time range of log time stamps that are strictly lower than the specified time (note time format is of YYYY-MM-DD HH:MM:SS , example: "2020-08-15 21:56:54")

### POST

First one is [http://127.0.0.1:5000/api/v1/resources/user](http://127.0.0.1:5000/api/v1/resources/user)

This endpoint is designed for the front end to dump the user id and sessionId into the database. It takes in two mandatory params:
- id - Mandatory. This is the user id 
- sessionId - Mandatory. This is the session id

Second one is [http://127.0.0.1:5000/api/v1/resources/action](http://127.0.0.1:5000/api/v1/resources/action)

This endpoint is designed for the front end to dump the action logs into the database. It takes in five params but only one is mandatory (user_sessionId):
- user_sessionId : Mandatory. This is the session id for the action and is used to relate back to the user entity when doing queries
- type : this is the type of log 
- locationX : this is the location of the mouse cursor at point x 
- locationY : this is the location of the mouse cursor at point y
- viewedId : this is the viewed id 

## Example

This example will go over how to generate the output of the sample log provided for this coding project from zero. 

**Note** the database you guys will have when you pull down the gitrepo will have this example already done for you. If you would like to follow along just delete the "sqlite.db" file in the database folder and you should be able to recreate this example.

First we will create the user entity using this post request with these id and sessionId params:
[http://127.0.0.1:5000/api/v1/resources/user?id=ABC123XYZ&sessionId=XYZ456ABC](http://127.0.0.1:5000/api/v1/resources/user?id=ABC123XYZ&sessionId=XYZ456ABC)

You can use this get request to verify [http://127.0.0.1:5000/api/v1/resources/user/all](http://127.0.0.1:5000/api/v1/resources/user/all)

Next we will start adding the action entities using this post request with the specified params:
 - [http://127.0.0.1:5000/api/v1/resources/action?user_sessionId=XYZ456ABC&type=CLICK&locationX=52&locationY=11](http://127.0.0.1:5000/api/v1/resources/action?user_sessionId=XYZ456ABC&type=CLICK&locationX=52&locationY=11)
- [http://127.0.0.1:5000/api/v1/resources/action?user_sessionId=XYZ456ABC&type=VIEW&viewedId=FDJKLHSLD](http://127.0.0.1:5000/api/v1/resources/action?user_sessionId=XYZ456ABC&type=VIEW&viewedId=FDJKLHSLD)
- [http://127.0.0.1:5000/api/v1/resources/action?user_sessionId=XYZ456ABC&type=NAVIGATE&pageFrom=communities&pageTo=inventory](http://127.0.0.1:5000/api/v1/resources/action?user_sessionId=XYZ456ABC&type=NAVIGATE&pageFrom=communities&pageTo=inventory)

You can use this get request to verify [http://127.0.0.1:5000/api/v1/resources/action/all](http://127.0.0.1:5000/api/v1/resources/action/all)

Lastly we can use this get request to retrieve all log files from the user id "ABC123XYZ": 
[http://127.0.0.1:5000/api/v1/resources/logdump?userId=ABC123XYZ](http://127.0.0.1:5000/api/v1/resources/logdump?userId=ABC123XYZ)

This will return us the JSON formatted as the sample log you gave for this coding test. I've also **included a screenshot of the final output for this last get request** labeled "Solution.PNG" that can be found in the gitrepo. 