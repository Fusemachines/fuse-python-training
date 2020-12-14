# Python & Flask APIs Training
This repo contains a part of codebase prepared for a internal Python + Flask training done within Fusemachines. 

## Installation
First create a virutal environment in you system. For this purpose use [pipenv](https://pypi.org/project/pipenv/) . Verify either you have installed pipenv or not. For this:

```bash
pipenv --version
```

If above command raise error then just install pipenv using following command.
```bash
pip install pipenv
```

If you are going to start new project from scratch then do following:

```bash
pipenv --python 3.7 #3.7 is the python version

pipenv install flask==1.1.1 # 1.1.1 is the latest stable version of flask
```
If you are going to use this repo then you can just run following command:

```bash
pipenv install
```

Before running the application be sure you have activated you environment. To activate you virtual environment do following:

```bash
pipenv shell # you should be in the directory where Pipfile lies
```

## Running the Application
1. Export necessary Environment Variables
```bash
export FLASK_APP=apis
export FLASK_ENV=development
```
2. Run the flask app  
`flask run`

## Code Organization
All the sessions are recorded in their respective branches. Below are the corresponding branches and their description.
- `master` - bareminimum of the flask app
- `session-6/1-mongo-setup` - Adding mongo setup and CRUD operations
- `session-6/1-mongo-setup` - Adding Schemas to the flask app
- `session-6/3-services` - Refactoring the sevices separately
- `session-7/1-basic-auth` - Add basic authentication 
- `session-7/1-token-based` - Add Token based Authentication


## Contributors / Session Facilitator
- Sushil Thapa ([www.thapasushil.com](https://thapasushil.com))
- Prem(Anuj) Subedi

## License
All Rights Reserved to Fusemachines. 

