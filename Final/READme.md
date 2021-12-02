This project uses the flask app to generate a mad libs story for the user. It builds off Lab 11, but makes it a bit more interactive.
It takes input from the user with a form, and then it ouputs it in the format of a mad lib story. 


For my final project to work, you need to download everything within the "Final" folder (routes.py, web.py, and the templates folder)
Do not remove anything from the templates folder, they need to remain in that folder for it to work. 

#BEFORE RUNNING

You will need to install flask if you already haven't from our previous lab:

In the command prompt enter:

py -3 -m venv venv

venv\Scripts\activate.ps1

pip install flask

python web.py

Before running the command "python web.py" you will need to cd to into the directory that you downloaded it to.

#AFTER FLASK INSTALL

Make sure that your VENV is activated and that you are in the right directory.

Once you run the command "python web.py", you can navigate to localhost:5000 in the browser and it will ask you to input information. 

After that, click submit and the mad libs story will appear with the answers you gave. 
