# Pitcher App

### External Resources: [Heroku Link](https://pitch-perfect-ip-app.herokuapp.com/) | [Figma Link](https://www.figma.com/file/R6c5bUiT6oOgf1So1WUZNO/Pitcher?node-id=0%3A1) | [Lucidchart ERD Link](https://app.lucidchart.com/invitations/accept/716c5217-7175-4ac6-914e-e824f3719bc3)
___

## Introduction
Pitcher is a social site where users can pitch ideas and others can rate them through likes. The pitches are divided into different categories. Anyone can view the pitches and vote on them, but one needs to have account to be able to add a pitch or leave a comment. When a user signs up, a welcome email is sent to the email address used to create their account.

## Technologies Used
Pitcher is built on Flask, a Python microframework. The live app is deployed on Heroku, and Postgres is used to manage the database.

## Installation (Ubuntu)
You can run the app using a local server on your computer. You will need Git to clone the app from this repo. Since Pitcher also uses Python 3 and Postresql, you will need to install them on your machine.

```bash
$ sudo apt install git python3 postgresql
```

You can now clone the repository on your computer. Navigate into the new directory after the clone is complete.

```bash
$ git clone https://github.com/VictorKMaina/pitch-app.git
$ cd pitch-app
```
As mentioned before, Pitcher runs on Flask and other Python modules. To install all the dependencies, you will need to create a virtual environment and activate it.

```bash
$ python3.6 -m venv virtual
$ source virtual/bin/activate
```

Note: Be sure to use your own preferred version of Python. You can confirm by running `$ python3 --version`.

Next, install the dependencies from the `requirements.txt` file.

```bash
$ python3.6 -m pip install -r requirements.txt
```

Pitcher makes use of a database, so you will need to create one using Postgres. You can find instrustions for creating a Postgresql user and password [here.](https://www.postgresql.org/docs/8.0/sql-createuser.html)

Enter Postgresql on your terminal using `$ psql`, then do

```postgres
username=# CREATE DATABASE pitch;
```

To be able to send emails to users, the app will access to an email address. For simplicity's sake, a dummy Google account and password have already been created. The app looks for exported environment variables to run. To enable this, create a file in the app's root directory called `start.sh`.

```bash
$ touch start.sh
$ chmod a+x start.sh
```

Add the following statements to `start.sh`.

```bash
export MAIL_USERNAME="moringacoreprojects@gmail.com"
export MAIL_PASSWORD="gwmsqndghwvumsgb"
```

The app will also need to connect to the database you created. Add this `start.sh`, and replace the `username` and `password` with your own.

```bash
...
export DATABASE_URL="postgresql+psycopg2://username:password@localhost/pitch"
```

Pitcher uses SQLAlchemy to make managing the database directly from the app easier. To update your database to work with this app's models, run the following.

```bash
python3.6 managa.py db upgrade
```

The configuration is almost complete. Edit `start.sh` so that it looks like this.

```bash
export MAIL_USERNAME="moringacoreprojects@gmail.com"
export MAIL_PASSWORD="gwmsqndghwvumsgb"
export DATABASE_URL="postgresql+psycopg2://username:password@localhost/pitch"

python3.6 manage.py server
```

Run the application.

```bash
$ ./start.sh
```
As long as the server is running, you can open it in the browser [using this link](http://127.0.0.1:5000).

## Known bugs
When viewing pitched in the categories, the app doesn't have profile pictures.

## [LICENSE](/LICENSE)