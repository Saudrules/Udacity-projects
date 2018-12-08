# Introduction 

In this project I am analyzing logs to create a log analysis document using python code, logs are taken from a newspaper database called called "news".
This database is an SQL based database (Postgresql in particular) and it has 3 tables: Articles, Authors and Log.
I was asked to write 3 queries to do the following:
1. Retrieve the 3 most popular articles in the database.
2. Retrieve the 3 most popular authors in the database.
3. Retrieve the days which have more than 1% of requests leading to errors. 

(_Popularity is based on number of visits_). 


# Installation 

Here are all the things you will need to install before you run this program:

* You will need to install Python3 which you can download [here](https://www.python.org/ftp/python/3.7.1/python-3.7.1-macosx10.9.pkg).
* You will need to install VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
* You will need to install Vagrant from [here](https://www.vagrantup.com/downloads.html).
* To download the Virtual Machine you can download and unzip [this file](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip), which will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.
* Alternatively, you can use Github to fork and clone [this repository](https://github.com/udacity/fullstack-nanodegree-vm).


# Execution 

After downloading the required files and tools above, follow these steps to run the program:

1. Change to the directory having the VM files (The zip folder) in your terminal using the `cd` command followed by the name of the file you to change into. You will find another directory called vagrant. `cd` into the vagrant directory. 
2. Start you Virtual Machine using `vagrant up` and when it is finished running, run the `vagrant ssh` command to login to your VM.
3. Now we need to connect to the database, we will use the `psql` command to connect to our _news_ database. Use `psql -d news`.
4. Now you can display the tables of the database using `\dt`.
5. Now we just have to run the python program, to do that just open another terminal window and make sure you are in the directory which contains the python file, just run `python "Filename.py"`. 
6. Now the program should be running.


# Code Design 

When writing the python code I followed a coding style that was required by Udacity using a command line tool, the tool is pycodestyle. 
To install this tool I used the `pip3 install pycodestyle` command. 
I have seperated the three queries into 3 seperate functions: 
the first query in `FirstQuery()`, 
the second query in `SecondQuery()`, 
the third query in `ThirdQuery()`.


# Notes 

When writing the third query which can be found in the `ThirdQuery()` method, I broke the query into a few steps:

1. I have created a view which has the total number of requests per day called _reqs_per_day_ as in: 
``` 
CREATE VIEW reqs_per_day AS SELECT CAST(time AS date), COUNT(*) AS Requests FROM log GROUP BY CAST(time AS date);
``` 
* The CAST method is used to convert a data type of a certain expression or a table column into a target data type that you want to convert to as in : 
` CAST ( expression AS type ); `. 
2. I have created another view which has the number of **failed** requests per day and called it error_reqs as in: 
``` 
CREATE VIEW error_reqs AS SELECT CAST(time AS date) AS day, COUNT(*) AS requests FROM log WHERE status = '404 NOT FOUND' GROUP BY CAST(time AS date);
```
3. I have joined the _reqs_per_day_ view and _error_reqs_ view to get the final result as in: 
```
SELECT error_reqs.requests/(reqs_per_day.requests*0.01) Percentage, reqs_per_day.day FROM reqs_per_day JOIN error_reqs ON error_reqs.day = reqs_per_day.day WHERE error_reqs.requests > reqs_per_day.requests * 0.01;
```


# References 

* I have used [this](https://stackoverflow.com/questions/23276344/like-operator-in-inner-join-in-sql) feed from **StackOverFlow** to help me with the first query.


