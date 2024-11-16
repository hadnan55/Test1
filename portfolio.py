# #Using universe template here:

from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# #Claude:
# Different way to 'run' Flask instead of flask --app portfolio.py run terminal command, you can do:
# if __name__ == '__main__':
#     app.run()

# IF you wanted to keep both server.py and portfolio.py flask apps activate at same time (turn one off using control+C), 
# you can run one on a different port with:

# flask --app portfolio.py run --port 5001

# or permanently a different port with:

# if __name__ == '__main__':
#     app.run(port=5001)  # different port


# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


#FIGURED THIS OUT ON OWN: <variablename> version, .html is included 

from markupsafe import escape 

@app.route('/<pagename>')
def actualpage(pagename=None):
    return render_template(pagename)

#did this originally, not required:

# @app.route('/<pagename>')
# def actualpage(pagename=None):
#     return render_template(f'{pagename}')

#Andrei used </string:pagename> to hard specify a string as the acceptable parameter
#Andrei had to remove the components link from all the pages, this is already cleaned up for us in 2024
#Andrei had to fix some headers in the aboutme and contact pages
#We updated the intro page message under the index.html 
#Underneath the index.html, searching for 002 brings up the works pages, can modify these to link to our projects 


#Now we are going to add functionality to use the "contact" form:

from flask import request 
from flask import url_for

#GET means browser us to send info to it. POST means browser wants us to save info.
#LINE 62 and 74 under contact.html have relevant sections
#GET: send data by attaching information to the URL
#Action "submit_form" will be POSTED when we click Send. (leave method as POST)
#The method .to_dict will turn the form data INTO a dictionary
#this allows up to capture information sent to us in dictionary format 

from flask import redirect
import csv

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter =',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
        except:
            return 'did not save to database' 
    #  # Method 1: Write as a simple string
    #     with open('database.txt', 'a') as file:  # 'a' means append mode
    #         file.write(f"{data}\n")  # \n adds a new line
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'
   

#Line 66, 69, 72 had to have name="email" and name="message" added so data in the form could be captured properly. 
#Andrei duplicated contact.html and renamed it thankyou.html

#thi is example resulting dictionary that was put into the output:

# {'email': 'a@a.com', 'subject': 'a', 'message': 'aaaa'}

# Claude helped setup the #Method 1 up above, the information was put into a database.txt file
#We ended up using CSV way anyway so commened out

#Andrei version to compare sets up a function:

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')

# He then called on this function inside the submit form route with:
# write_to_file(data)

# CSV files (comma separated values) is a better way to organize this incoming information. 
# CSV writer is going to write to the database.csv file. 
#THE WRITE_TO_CSV FUNCTION: was moved up in the code to BEFORE the submit form approute!!

# Delimiter is what's going to separate the values, quotechar is asking what to put around the characters, this errored and we had to give it a value. 
# CSV module has a writer.writeheader() function, but we already have headers?:

#We had to make adjustments to the newlinel = '' in the open statement 

# Front end = css, java, html
# back end = python, web servers
# databases in back end = like mongoDB
# information is stored in a database insetad of a local excel file
# DBMS = database mgmt system

# RELATIONAL Databases: like oracle db, mysql, sqlserver 
# It's relationships of columns of data with multiple rows
# Primary key and foreign keys

# http: for front-end talking to back-end
# SQL: for back end talking to database*

# NONRELATIONAL Databses: don't need predefined schema/relationship of the data
# Can define these as we go. All very different. 
# MongoDB: stores information as documents 

# Twitter example: sql ones have big sections with each independent variable data
# nonsql mongodb organizes info by username instead 

pythonanywhere.com : let's you host your .py files info online for free

#WENT INTO GITHUB SIDE SECTION*
#EXPLAINED IN GITHUB.PY*

#RETURNING TO PORTOFLIO PROJECT:

#Moved static, templates folders, and database.csv, and portfolio.py (this .py file) INTO the Test1 folder (as copy)


