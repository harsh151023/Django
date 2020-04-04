# cc_jec
// Go to cc_jec/cc_jec directory. It is project directory

// create virtual environment.
$ conda create --name virEnv django

// to activate virtual env-
$ source activate virEnv



// to make migrations of DB
$ python manage.py migrate
$ python manage.py makemigrations c_app
$ python manage.py migrate

// To run the django development server
$ python manage.py runserver

// copy the server address(e.g - http://127.0.0.1:8000/) and paste it to browser.

