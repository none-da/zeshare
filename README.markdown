# ZeShare #

ZeShare is a small "code sharing" application. And can also be used as

- Ask programming puzzles and let people crack it and find the talent
- Ask for volunteering to any project/work
- Ask business related questions
- Do Code-Reviews
- Any other lateral ways to use this? [Please let me know!](mailto:madhav.bnk@gmail.com "madhav.bnk@gmail.com")

# Prerequisites #

- [Python 2.5](http://python.org/ "Python")
- [Pygments](http://pygments.org/ "Pygments")
- [Django 1.1](http://code.djangoproject.com/browser/django/tags/releases/1.1.1 "Django 1.1")
- [Postgresql](http://www.postgresql.org "Postgresql")

# Installation #

**Download [ZeShare version 1.0.1](http://github.com/madhav/zeshare/tarball/1.0.1 "ZeShare 1.0.1")**
**Create 'zeshare' db with the following commands**

    sudo su postgres -c "createuser -sP zeshare"
    sudo su postgres -c "createdb zeshare -O zeshare -W"
    
(you can always have your own db name and credentials as well. Please update 'settings.py' in zeshare folder with those corresponding values)
    

# Running ZeShare (development server) #

    cd zeshare
    python manage.py syncdb #(for creating the required tables in 'zeshare' db)
    python manage.py test quest users utils #(for testing 'zeshare' testcases)
    python manage.py runserver #(run the development server)

# Contribute #

Development of ZeShare happens at Github: http://github.com/madhav/zeshare

**You are highly encouraged to participate in the development of ZeShare**. If you don't like Github (for some reason) you're welcome to send regular patches.

    git clone git@github.com:madhav/zeshare.git zeshare

# TODOs and BUGS #

- [http://github.com/madhav/zeshare/issues](http://github.com/madhav/zeshare/issues "Issues")

# Built on #

- Python2.6, Django(1.1), Postgresql-8.3, Blueprint CSS, YUI, Eclipse(3.4), GIT(github), Pixlr, Ubuntu 9.10