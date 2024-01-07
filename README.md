<h1 align="center" >Hello 👋, I'm Ryo</h1>
<h3 align="center" >An independent backend developer</h3>

<h1 align="center" >Welcome To InstaHarvest🍁</h1>

> This program is a program that can be used to retrieve data from Instagram and download their content

## Feature

- Using requests instead of webdriver makes it lighter and faster
- use of cookies and check expiration so you don't need to always log in
- can download all content uploaded by users
- search for the target user ID automatically so that the user only needs to enter the target username
- providing an update_component file to make it easier for those who have difficulty using the flag command
- The download quality does not decrease and the quality will remain the same as the original quality of the post

## Tech

- [python-dotenv](https://pypi.org/project/python-dotenv/) is a convenient Python library that simplifies the management of environment variables in your projects. It allows you to load variables from a .env file into your environment, making it easy to configure and control settings for your applications.
- [icecream](https://github.com/gruns/icecream) is a Python library that provides a simple and informative way to log code, helping with monitoring program execution flows.
- [requests](https://requests.readthedocs.io/) is an easy-to-use Python library for interacting with APIs and making HTTP requests.
- [tqdm](https://tqdm.github.io/) is a Python library that provides an aesthetic progress bar to monitor the execution process in iterations.

## Requirement

- [Python](https://www.python.org/) v3.11.6+
- [icecream](https://github.com/gruns/icecream) v2.1.3+
- [python-dotenv](https://pypi.org/project/python-dotenv/) v1.0.0+
- [requests](https://requests.readthedocs.io/) v2.31.0+
- [tqdm](https://tqdm.github.io/) v4.66.1+

## Installation

> To run this program you need to install some libraries with the command

```sh
pip install -r requirements.txt
```

## How To Run ?🤔

```bash
# Clone this repositories
git clone https://github.com/ryosoraa/InstaHarvest.git

# go into the directory
cd InstaHarvest

```

To run the program the first time you have to include several flags

```bash
python main.py --username target_username --cookies '<YOUR_COOKIES>' --igclaim '<YOUR-X-Ig-Www-Claim>'
```

or if you don't understand you can run the update_component.py file
and insert COOKIES and X-Ig-Www-Claim there

```bash
python update_component.py
```

![](https://raw.githubusercontent.com/ryosoraa/ryosoraa/main/images/Screenshot%202024-01-07%20173442.png)

## How To Get COOKIES And X-Ig-Www-Claim ?🍪

⚠️I suggest not using your main account because we do not guarantee that your account will not be blocked⚠️

1. Log in to the Instagram account you want to use to retrieve data
2. If you are already logged in then continue by opening the target account profile
3. Open developer Tool Using Option + ⌘ + J (on macOS), or Shift + CTRL + J (on Windows/Linux)
4. Open the network menu and run the shortcut CTRL + R to reload the page

   <br>
   <div style="text-align: center;">
     <img src="https://raw.githubusercontent.com/ryosoraa/ryosoraa/main/images/Screenshot%202024-01-07%20175904.png", width="600" height="315 "> 
   </div>
   <br>

5. look for the name that has: <b>username/?count=12<b>

   <br>
   <div style="text-align: center;">
     <img src="https://raw.githubusercontent.com/ryosoraa/ryosoraa/main/images/Screenshot%202024-01-07%20180050.png"> 
   </div>
   <br>

6. Click and scroll down until you find Cookies and X-Ig-Www-Claim

   <br>
   <div style="text-align: center;">
     <img src="https://github.com/ryosoraa/ryosoraa/blob/main/images/Screenshot%202024-01-07%20180200.png?raw=true"> 
   </div>
   <br>

7. Copy Cookies and X-Ig-Www-Claim to insert into the code above

## Flags

|    Flag    | Alias |          Descriptions          |         Example         |
| :--------: | :---: | :----------------------------: | :---------------------: |
| --username |  -u   | Insert username account target | --username freya.jkt48  |
| --cookies  |  -c   |      Insert your cookies       | --cookies 'sxdfcgvbhnj' |
| --igclaim  |  -ic  |   Insert your X-Ig-Www-Claim   | --igclaim 'dcfvgbhjnmk' |

## 🚀Structure

```
│   .env
│   .gitignore
│   LICENSE
│   main.py
│   README.md
│   requirements.txt
│   update_component.py
│
├───data
└───src
    │   __init__.py
    │
    ├───exceptions
    │       ExpiredExceptions.py
    │
    ├───service
    │       instagram.py
    │
    └───utils
            Arguments.py
            file.py
```

## Author

👤 **Rio Dwi Saputra**

- Twitter: [@ryosora12](https://twitter.com/ryosora12)
- Github: [@ryosoraa](https://github.com/ryosoraa)
- LinkedIn: [@rio-dwi-saputra-23560b287](https://www.linkedin.com/in/rio-dwi-saputra-23560b287/)
- Instagram: [@ryosoraa](https://www.instagram.com/ryosoraaa/)

<a href="https://www.linkedin.com/in/ryosora/">
  <img align="left" alt="Ryo's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://www.instagram.com/ryosoraaa/">
  <img align="left" alt="Ryo's Instagram" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" /> 
</a>
