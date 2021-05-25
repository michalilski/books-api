# Books REST API using Django

## Overview
This project provides RESR API for searching books using Django. API lets user to find books with opinions about them making simple HTTP GET request.

## Data insertion
To add Book models use command:  
python3 manage.py insert_books <filename\>  
where filename is path to your CSV file. To learn more about e.g. data
format type:  
python3 manage.py insert_books --help  
  
To add Opinion models use command:  
python3 manage.py insert_opinions <filename\>  
where filename is path to your CSV file. To learn more about e.g. data
format type:  
python3 manage.py insert_opinions --help  
Important - you can't add opinion to book not existing in database, so remember to add books first.

## API
To get book by title make GET request as  
<host\>:<port\>/book/?title=<title\>  
e.g.  http://127.0.0.1:8000/book/?title=Ryzyko%20gangstera  
where title is your book title passed as query parameter. You may also pass just beginning of book title so response will return all results starting with passed prefix. This feature may be used e.g. in searching bar serving hints after each typed character.  
Important - passing empty <title\> will return empty result.

## Run locally
1. Install required dependencies using command:  
pip install -r requirements.txt  
2. Run server using command:  
python3 manage.py runserver  
3. Or using gunicorn:  
gunicorn --pythonpath booksapi booksapi.wsgi
