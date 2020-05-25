# Connect

### Developed By
[Carine I. SEMWAGA](https://github.com/Krasivaya)

## Description
This is an idea sharing platform, which help users to express their thoughts through creation of articles and sharing the articles with their networks. An author can create a post, and then, other users can react to the posts.

## BDD
|   Description   |   Method   |   Endpoint  |
|   :-------:   |   :---:   |   :---:   |
|   A user can view all article posts  |   GET    |   api  |
|   A user can view a single article post  |   GET |   api/article/:artId   |
|   A user can comment on an article post  |   POST  |   api/article |
|   A user can liken an article post  |  POST |   api  |
|   A user can share on an article post  | POST    |   api/article/shared  |
|   A user can view recent posts   |   GET    |   api    |
|   A user can get an email alert once a new article post is made  |   POST   |   api |
|   An author can sign up  |   POST  |   api/auth/signup   |
|   An author can login  | POST    |   api/auth/signin    |
|   An author can create a post    |   POST    |   api/article    |
|   An author can delete comments  |   DELETE   |   api/article/:cmId |
|   An author can delete a post  |   DELETE    |   api/article/:artId    |
|   An author can update a post  |   UPDATE    |   api/article/:artId    |


## Technologies Used

1. Python3.6
2. Virtualenv
3. Django 
4. Postgresql
5. HTML5 
6. Bootsrap & CSS
7. Git Version Control 

## Setup/Installation Requirements

* Open your terminal
* initialize github, git clone ` https://github.com/Krasivaya/Connect.git `
* cd Connect
* open folder in prefered IDE Eg. ` code . `
* open terminal
* Activate virtual envirnoment `source virtual/bin/activate`
* Install the latest version of pip `curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all requirements `pip install -r requirements.txt`
* Run in terminal `chmod a+x start.sh`
* Run in terminal `./start.sh`
* Run the application in your localhost provided

## Known Bugs
No bug known. If you found any, please contact!

## Contacts Details
Email: semwagacarine@gmail.com

## Live Demo
[Connect(Not available Now)]()

## License
This project is under the [MIT](https://github.com/Krasivaya/github/blob/master/LICENSE) license.

##### Copyright © 2020 Carine I. SEMWAGA.