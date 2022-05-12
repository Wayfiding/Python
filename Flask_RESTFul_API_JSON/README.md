<h1 align="center">Welcome to Flask_RESTFul_API_JSON 👋</h1>

![home](./images/cover.jpg)

<p>
  <img alt="Version" src="https://img.shields.io/badge/version-Adding Readme -blue.svg?cacheSeconds=2592000" />
  <a href="On Test" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="<img alt=&#34;GitHub&#34; src=&#34;https://img.shields.io/github/license/wayfiding/ROCKETSEAT?color=MIT&logo=MIT&logoColor=MIT&#34;>" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

</div>

<div>
Languages:

[Portuguese :brazil:](README-ptbr.md)

</div>
</div>

# About
> This a Restful API project for Flask, developed by [Pretty Printed](https://prettyprinted.com/), you can see the entire video [there](https://www.youtube.com/watch?v=WxGBoY5iNXY&ab_channel=PrettyPrinted). On this project were made a restful api for authenticating with JSON web token and routes for CRUD on  ToDo task.


### **Prerequisites**
To be able to use the techonolgies provided there, you need to have a editor and a computer with Linux,Windows or Mac SO. 


## How to Use
If you want download this folder from this repository just follow this steps below:


1. Copy the url from your browser;
2. Replace the 'tree/main' or 'tree/master' with trunk;

Example: 
> https://github.com/User/somerepo/tree/main/folderyouwant
 
> https://github.com/User/somerepo/trunk/folderyouwant 

3.Go to the command Line and just grab the folder with SVN

```sh
    svn checkout https://github.com/User/somerepo/trunk/folderyouwant 
```

## How to Run

 - For Windows User will be flagged what to do in each steps.
 - Windows User need to install at least the Python 3.8 Version, this can be done accesing the [Python](https://www.python.org/) website.
 - Most Command for Windows User is for PowerShell.
1. Install > virtualenv : (Linux)


```sh
$ sudo apt-get install python3-venv
$ sudo yum install python3-venv
$ sudo zypper install python3-venv
```

2. Open a terminal in the project root directory and run:

```sh
$ python3 -m venv venv
```
For (Windows User):
```sh
python -m venv venv
```
3. Then run the command:

```sh
$ source venv/bin/activate
```
For (Windows User):
```sh
.\venv\bin\activate
```

4. Then install the dependencies:

```sh
$ (env) pip install -r requirements.txt
```
5. Populate the DB: 
```sh
python
from api import db
db.create_all()
```

6. Finally start the back-end server:
   
```sh
(env) export FLASK_APP=api.py
(env) flask run
```
For (Windows User):
```sh
$env:FLASK_APP='api.py'
flask run
```

---- Windows User ----

If the Python Flask aren't working because of Windows Policy, you should allow this using the following command on PowerShell: 
```ps1
Set-ExecutionPolicy RemoteSigned
```
or

```ps1
Set-ExecutionPolicy Unrestricted
```
And to check the Execution Policy 

```ps1
Get-ExecutionPolicy
```

More details you can find on [Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2) website.
## 🚀 Technologies
This Project was developed using the following technologies:



- Python 3.8
- Flask
- Insomnia / Postman




## Author

👤 **Alberto Junior**

* Github: [Alberto Júnior](https://github.com/wayfiding)
* LinkedIn: [Alberto Souza](https://linkedin.com/in/alberto-souza)
  
## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](Teste). 

## 📝 License
Copyright © 2021 [Alberto Júnior](https://github.com/Wayfiding).<br />

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](../LICENSE) para mais detalhes.

***
This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator) and Alberto
