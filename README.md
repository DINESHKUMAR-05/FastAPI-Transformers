Create the required files in following schema :
 with :
      - requirement.txt
      - Dockerfile
      -app
        - main.py
        - __init__.py
Install required libaries locally if you want to run the code on local machine . (fastapi,transformers,typing_extensions,torch,uvicorn,pydantic,python-multipart)
If runnning in local machine direct the powershell to location of main.py file run the following command "uvicorn main:app" This will direct you the the loaclhost port there enter in URL has /docs followed by the localhost and port . click on try it out and enter the question and context in it and execute to get the answer
Build a docker image (ensure network connectivity for smooth building). Push the image to the dockerhub for future use and transfer and run the docker image in command prompt using the command "docker run <image_name>"
