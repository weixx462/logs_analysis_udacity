# logs_analysis_udacity


# Project description 

Internal reporting tool that uses information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, the code will answer questions about the site's user activity.
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


# Prerequisites & Set up

You'll need database software (provided by a Linux virtual machine) and the data to analyze.

The virtual machine

This project makes use of the same Linux-based virtual machine (VM) as the preceding lessons in Udacity Full Stack Nanodegree.

If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.

Download the data

Next, download the data here(https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)

To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

    psql — the PostgreSQL command line program
    -d news — connect to the database named news which has been set up for you
    -f newsdata.sql — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. 


# Usage

The repo contains 2 files: logs.py and output.txt. Running logs.py will produce contents output.txt for logs analysis. 

To run logs.py: in vagrant VM, run command python logs.py.
