This newsletter application is made with Flask and SQLAlchemy.
- Newsletter list, login, create post, edit post and post detail pages are available.
- A single user (admin) will be logged in. Therefore, the registration page was not created.
- In order to enter a news content, you must enter the title and content of the news. The created_time variable is also automatically created for the news.
- You can edit the content of a news or delete the news.
- PostgreSQL database is used.
- Packaged using Docker. (docker-compose up)
- Flask-WTForms is used for user forms and news forms.
- Flask-Login is used for authentication & authorization.
- Psycopg2 is used for PostgreSQL connection. 
