# TodoApp


A simple example of app which uses DRF for backend and 
NodeJS for frontend
---
### How to run it:
#### clone repo
```
git clone https://github.com/Farrukhraz/TodoApp.git
cd TodoApp
```
#### install nodejs for frontend
```
sudo apt update
sudo apt install nodejs
sudo apt search build-essential
```
#### check that npm is installed correctly (nodejs tool)
```
npm --version
```
#### create a venv for backend
```
python -m venv venv
source venv/bin/activate
```
#### backend
server will run on localhost:8000
```
cd backend
python -m pip install -r requirements.txt
python manage.py runserver
```
#### frontend
server will run on localhost:3000
```
cd ../frontend
npm start 
```
