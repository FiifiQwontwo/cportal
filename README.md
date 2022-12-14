
#

A django Church Portal 



## Getting Started
The mission is simple. We are building a solution to automate the church's flagship data submission and reporting processes.

Without automation, these processes in themselves have contributed to the high growth and expansion of the church all over the world.

What we are doing here today is not just another cool UD thing, it is going to impact greatly the growth of the church and the work of the ministry to carry the gospel to the ends of the world.

In the words of Bishop Kakra, "things don't just happen by osmosis." The furtherance of the Kingdom takes a lot, especially the skills, time, and resource inputs of the faithful.
## Getting Started
The mission is simple. We are building a solution to automate the church's flagship data submission and reporting processes.

Without automation, these processes in themselves have contributed to the high growth and expansion of the church all over the world.

What we are doing here today is not just another cool UD thing, it is going to impact greatly the growth of the church and the work of the ministry to carry the gospel to the ends of the world.

In the words of Bishop Kakra, "things don't just happen by osmosis." The furtherance of the Kingdom takes a lot, especially the skills, time, and resource inputs of the faithful.
## Prerequisites
```bash
python 3.9

```


# Installation

```bash
$ git clone https://github.com/FiifiQwontwo/cportal.git
```

Then 
```bash
$ cd Foldername
```
create a virtual enviroment to install dependencies

```bash
python -m venv venv
./venv/Scripts/activate
```
Then install the dependencies:
```bash
(venv) $ pip install -r requirements.txt
```
Once pip has finished downloading the dependencies: create a MySQL database and give a name and update the env file with the new database name, then makemigrations and then migrate

```bash
(venv)$ cd project
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```
and navigate to http://localhost:8000 

## Tech Stack 

    Python - Language Used
    Django - The web framework used
    MYSQL - Database used
    HTML - Used for frontend
    CSS - Used to Style the pages


## Contributing
- [@Michael Ahwireng](https://www.github.com/FiifiQwontwo)

## License

[MIT](https://choosealicense.com/licenses/mit/) This project is licensed under the MIT License - see the LICENSE.md file for details


## Acknowledgements

 - [Medium ](https://medium.com/)
 - [Simple is Better than Complex](https://simpleisbetterthancomplex.com/)
