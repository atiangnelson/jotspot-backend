This is the backend API for **jotspot**, a simple note-taking app built with flask. It supports user registration, login with JWT authentication, and CRUD operations on personal note.

# Features 
    - User regestration and login withJWT-based    authentination
    - Create,Read,Update,Delete operations for user notes 
    - SQLite database with SQLAlchemy ORM 
    - RESTful API with Flask-RESTful 
    - CORS enabled for frontend integration
    - Password hashing for security purpose 
    - Tags support for notes 

# Technologies used 
 - python 3.x
 - Flask 
 - Fask-RESTful 
 - Flask-JWT-Extended 
 - Flask-Migrate 
 - Falsk-CORS
 - SQLAlchemy 
 - SQLite

 # installation and setup 
 **Clone the repository**
 ** git clone <repo-url>
cd server 

**create a virtual environment**
 python3 -m venv venv

 **run database migrations**
  - flask db init 
  - flask db migrate -m "initial migration"
  - flask db upgrade 

  **seed the database**
  python seed.py 

  **start the server**
  python app.py


  # API  Endpoints 
  GET  '/notes'  --get all notes for user 
  POST '/notes'  --create a new note
  PUT  '/notes/<id>' --update an existing note 
  DELETE '/notes/<id>' --delete an existing note 


  # JWT Authentication 
After login, include the token in the 'Authorization' header for protected routes 