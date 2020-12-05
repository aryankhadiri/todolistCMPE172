# TuduList Project
### <b>UniversityName-SJSU</b>
### <b>Course:EnterpriseSoftware-CMPE172Fall2020</b>
### <b>TeamMembers</b>
- Aryan Khadiri
- Anish Patel
## <b>Project Introduction</b>
Out TuduList project is a web application which allows users to create and store their to-do tasks. Furthermore, the users can create their own accounts and are required to login to view or edit their tasks. The main problem which our application is trying to solve, is to create a space for everyone where they can store their tasks and get them off their mind. Once any of the tasks are done, they can edit them and mark them as finished. The main objective of this project was to connect different enterprise software components such as Docker, dynamodb and etc. 
## <b>Sample Demo Screenshots </b>
Login Page
![Alt text](imagesgithub/demo1.png?raw=true "System Diagram")
Registration Page
![Alt text](imagesgithub/demo2.png?raw=true "System Diagram")
HomePage-adding a new task
![Alt text](imagesgithub/demo3.png?raw=true "System Diagram")
Homepage-updated with new task
![Alt text](imagesgithub/demo4.png?raw=true "System Diagram")

## <b>How to Run Application Locally</b>
- You need to first have Python3 and Django any version of 3 installed. If you don't, take the steps below:
- ``` pip3 install django=3 ```
- You also need to install boto3 to connect to AWS
- ```pip3 install boto3 ```
- You need to have DynamoDB account and a table named Tasks
- Create Your DynamoDB account and configure your AWS within the Terminal by typing:
- ``` aws configure ```
- If you don't have aws cli installed, you need to first do install that in order to run the command above
-   Navigate to the home directory of the application where you see the file 'manage.py'
- Run the command: 
``` python3 manage.py runserver 8000 ```
- Note: if port 8000 is used, simply change that to some other port number
- Copy the link provided by Django after you run the command above and paste it in your browser. You should be able to view the homescreen. 
## <b>SystemDiagram</b>
![Alt text](imagesgithub/shot1.png?raw=true "System Diagram")
Database Tables
![Alt text](imagesgithub/shot2.png?raw=true "Database Diagram")
