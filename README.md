<center>

  <h1>PlanITarium</h1>
  <p>Looking at time differently</p>
  <h3>by <a href="https://github.com/kimmykokonut">Kim Robinson</a></h3>
  <p>
        <a href="https://github.com/kimmykokonut/planitarium/stargazers">
            <img src="https://img.shields.io/github/stars/kimmykokonut/Capstone?color=yellow&style=plastic">
        </a>
        ¨
        <a href="https://github.com/kimmykokonut/planitarium/issues">
            <img src="https://img.shields.io/github/issues/kimmykokonut/planitarium?style=plastic">
        </a>
        ¨
        <a href="https://github.com/kimmykokonut/planitarium/blob/main/LICENSE">
            <img src="https://img.shields.io/github/license/kimmykokonut/planitarium?color=orange&style=plastic">
        </a>
        ¨
        <a href="https://www.linkedin.com/in/robinson-kim/">
            <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=plastic&logo=linkedin&colorB=2867B2">
        </a>
    </p>    
</p>
<!--   <a href="https://myco.onrender.com/" alt="hosted site">See it live on Render (sign in required)</a>     ||     <a href="https://www.linkedin.com/feed/update/urn:li:activity:7203485384104693762/" alt="linked in reference">Learn more here via LinkedIn</a> 
  
  <p>Initiated October 21, 2024</p> -->
  
  </center>

### Jump around!

* <a href="#about-the-project">About the Project</a>
  * <a href="#description">Description</a>
  * <a href="#built-with">Built With</a>
  * <a href="#known-bugs">Known Bugs</a>
* <a href="#getting-started">Getting Started</a>
  * <a href="#prerequisites">Prerequisites</a>
  * <a href="#setup">Setup</a>
* <a href="#miscellaneous">Miscellaneous</a>
  * <a href="#contact-and-support">Contact and Support</a>
  * <a href="#license">License</a>
  * <a href="#acknowledgements">Acknowledgements</a>
  * <a href="#stretch-goals-and-thoughts">Stretch Goals and Thoughts</a>
---------------------------
## About the Project

### Description

  What is the problem with To-do Lists?
  --more content here--
  
## Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Known Bugs 

None at this time

## Getting Started

  ## Prerequisites

### Code Editor
  To view or edit the code, you will need a code editor or text editor. The open-source code editor I used is VisualStudio Code.

  1) Code Editor Download: [VisualStudio Code](https://www.npmjs.com/)
  2) Click the download most applicable to your OS and system.
  3) Wait for download to complete, then install -- Windows will run the setup exe and macOS will drag and drop into applications.

### Install RestClient Extension for Visual Studio Code
(Optional) Download and install VS Code [RestClient extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

### Install Postman
(Optional) Download and install [Postman] to test API calls(https://www.postman.com/downloads/).

### Install Homebrew (macOS)
_I highly recommend you download this package manager to install software._

In terminal:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

### Install Python via homebrew
In terminal: 
`$ brew install python@3`
(Note: pip is included with Python-it is the standard package manager for Python)

## Setup

### Clone repository

1. Navigate to the [repository](https://github.com/kimmykokonut/planitarium).
2. Click the `Fork` button and you will be taken to a new page where you can give your repository a new name and description. Choose "create fork".
3. Click the `Code` button and copy the url for HTTPS.
4. On your local computer, create a working directory of your choice.
5. In this new directory, via the terminal, type `$ git clone https://github.com/kimmykokonut/planitarium`.
6. Run the command `cd planitarium` to enter into the project directory.
7. View or Edit: On your terminal, type `$ code .` to open the project in VS Code.

### Install dependencies - Backend/WebAPI
1. In VSCode Terminal: navigate to `planitarium` directory.
2. Make sure the .gitignore in the root directory has .venv in it.
3. Create a virtual environment `$ python3 -m venv .venv`
4. Enter the virtual environment `$ . .venv/bin/activate`
5. Install packages and dependencies `$ pip install -r requirements.txt`
<!-- 5.5. Maybe install Django if not in step 5. `$ pip install django` -->
6. Run server (http://127.0.0.1:8000) `$ python manage.py runserver`
- To exit virtual environment: `$ . deactivate`

### API .env
1. Make sure the .gitignore has .env in it and is committed before step 2.
2. Create .env file in the root directory for the backend api.
3. Add in the following fields with your own personal information: (note host and port may differ depending on what service you are using)
```
SECRET_KEY = '{YOUR-KEY}'
DB_USER='{YOUR-USER-NAME}'
DB_PASSWORD='{YOUR-DATABASE-PASSWORD}'

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='{YOUR-SENDER-EMAIL}'
EMAIL_HOST_PASSWORD='{YOUR-SENDER-PASSWORD}'
```

### Database
Django has built in migrations that make it easy to update database changes.
1. This project uses Sqlite3 database which is built into the project as a single file
2. Make sure you are in the directory that contains manage.py
3. Make migrations to update database schema `$ python3 manage.py makemigrations`
4. Apply migrations to update database `$ python3 manage.py migrate`

Now you should have your database schema all set!

## Miscellaneous
...coming

## Contact and Support

If you have any feedback or concerns, 
[Report Bug](https://github.com/kimmykokonut/planitarium/issues)
[Request Feature](https://github.com/kimmykokonut/planitarium/issues)

## License

GNU General Public License v3.0, See license.md for more information

## Acknowledgements

## Stretch Goals and Thoughts

