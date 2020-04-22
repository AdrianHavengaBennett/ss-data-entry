# [SS Data Entry Tool](http://ss-data-entry.herokuapp.com/)

## User stories

### I was asked by my current employer to help with some simple data entry. These were the individual steps taken:
- copy a job number from a spreadsheet
- paste it into a search field in FSL (Salesforce, which we currently use)
- retrieve a job number (copy it and paste back into the spreadsheet)
- if the job is not found, make a note in the spreadsheet
- copy a commission amout from the spreadsheet
- paste commission amount in FSL
- check whether an invoice number exists for the job, if so, copy and paste into spreadsheet
- check if payments from spreadsheet match those in FSL
- repeat the above

These tasks might not have been too drawn, had the list on the spreadsheet been small. But we do a month's worth at a time, so it's rather extensive.

I noticed a pattern of what we're asking of our own program's database, and so developed this software to assist.

### The task list is now as simple as 
- inputting the job number, commission amount, and expected payment into the data entry form
- clicking a button
- repeat

The software takes care of the rest and retrieves all the information we were seeking and saves it to a table, which updates below the data entry form with each input.

There's also an option to download the report when complete or clear the form and start over.

## Features

### - Existing features
User has the ability to do the following:
- create a report
- download the report
- clear the report
- access the github repository

### - Features left to implement

A feature soon be to added, should my company decide to use this software in the future, is authentication. The ability to log in and out of your account. This is to protect our real database.

## Technologies Used

Technologies used in this project:

## HTML5:
- https://en.wikipedia.org/wiki/HTML

## CSS3:
- https://en.wikipedia.org/wiki/Cascading_Style_Sheets

## Bootstrap:
- https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)

## Python
- https://en.wikipedia.org/wiki/Python_(programming_language)

## Django
- https://en.wikipedia.org/wiki/Django_(web_framework)

## And many more packages, which can be found in the requirements.txt file

## Deployment
For this project, I have used Heroku to deploy and host the application.

Below are the steps I have taken to achieve this:

- $heroku login (logging in on the terminal means you don't have to $git remote add the application, once you've created it in the step following)
- create new heroku app in terminal - $heroku create your-app-name --region eu(or us)
- add app (your-app-name.herokuapp.com) to ALLOWED_HOSTS list in Django settings.py
- switch Django debug to True to see errors in heroku app
- make sure you have postgres installed on your local machine
- pip install django-heroku then import it in settings.py and add django_heroku.settings(locals()) to the very bottom of the settings file
- make sure there's a requirements.txt file
- make sure there's a Procfile
- make sure heroku config vars has SECRET_KEY
- if using bootstrap css (not CDN, but actual file), add DISABLE_COLLECTSTATIC=1 to heroku config vars (I was getting an error about a file not being found - this step fixed that)
- $heroku run python manage.py migrate (or open the bash - $heroku run bash, then run things without "heroku run". See next step
- create new database superuser (from within heroku bash): $python manage.py createsuperuser
- if site is now running on heroku with no errors, switch django debug to False for

### Deployment Link
- http://ss-data-entry.herokuapp.com/

## Version Control
For this project, I have used Github for static version control:
- https://github.com/AdrianHavengaBennett/ss-data-entry

For this project, I drew inspiration from my love of finding ways to automate mundane tasks.

Copyright 2020 - Adrian Havenga-Bennett