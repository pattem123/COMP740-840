### DigitRecognizer Web API:

  Stages to develop and deploy API :
  -Train model
  -Save model using pickling and use to create Web API in local machine
  using Flask
  -create an app
  -Deploy the app externally using Heroku delpoying tool.
  -



  ## Developed a Web API implementing Convolution Neural Network model for predicting the numeric digits drew by the user.
  and deploy it into web server using web frameworks.
  ## initially I have trained my model and tried to save it into my disk with pickling function
     but couldn't do that as I got error like "Can't pickle lock_object and Can't pickle local_object".
     So, I have tried doing saving it by other method which by "joblib" which also gave me same error .
  ## After trying the different methods I wanted to create my app using different framework which Django
     rather than using Flask which is easy to implement than Django , but had to try that as well because I wasn't able to
     create app in former way.
  ## Created an app using Django REST web API Framework called main and the project as digitrecognizer using Django packages
     while I ran my app locally I got error in giving path to my json file for the communication between the front end and
     the backend . While trying to clear the outputs and re-running my jupyter notebook I started getting error which I mentioned
     below in the Errors section .


### Backend : - Django API named main.
### Frontend : - html and json
### Language : -Python pogramming



### Errors :

1.I got error in pickling when I wanted to use flask to develop App using different mnist dataset source.

  ## Can't pickle lock_objects and wasn't able to clear the error and had to go for other framework using Django.

2. Json file path error in utils.py file

3.I somehow started getting this error when running jupyter notebook.

##handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
ValueError: signal only works in main thread

How I resolved :
>> upgraded python kernel using following command :

    pip install --upgrade ipykernel
