The Naughty List
================

##About

The Naughty List at it's simplest level is about raising awareness of companies' exploitation and to provide a platform where action can be taken.

Some observations about the problem:

* Whether it's animal cruelty, child labour, deforestation or climate change; something, somewhere is exploited so to make a profit from it.
* Many charities and NGO's want to highlight these issues i.e. PETA with topshop over angora fur. 
* These bodies are getting way more coverage these days thanks to the internet... But, their reach on an issue and consumer's anger tends to be short lived.
* Social media helps raise awareness of wrongful acts, but as they happen so often, people will go "RA RA RA that's terrible!" and then move on to the next media frenzy. The rage is temporary, and when it's so short, it's difficult to really build momentum for change.
* As all these NGO's are trying to get your attention to their cause, there is no real combined effort to punish those responsible. It's a lot of small attacks on a giant fortress.

The insight

* Companies/countries are the main cause of exploitation across the globe. One human cannot cause any damage, but a machine built up of many can.
* Companies need your support, or they die.
* December and the run up to Christmas is a very important month for almost every company.

The idea

* By thinking of the larger problem at hand, and not just separate causes; that is, that multinationals and countries are responsible for many different faults it becomes a much more easier to plan a course of action.
* Create a means where every person can express their anger at a particular company/country, and for what reason, every day across any medium (twitter, facebook, thenaughtylist.com etc...)
* Track the opinions of those companies throughout the year, with the worst companies being visible on the website.
* Come December, compile the list of the most badly behaved companies to form the Naughty List.
* Have a mass boycott of those companies on The Naughty List during the entire month of December, applying not just pressure in shear numbers, but also a long duration of action. 
* In the same way as santa doesn't give misbehaving children presents, neither do the consumers reward little shits.

On a side note, this will probably also become a #nicelist too, so that companies can right their wrongs, and because being negative all the time gets you nowhere.

##Setup

This project has had a development scaffold put in place to encourage best practices; the focus being on Test-Driven Development and Continuous Integration - badly tested code that is stale tends to break. This also uses company conventions to allow for faster implementation and familiarity with other developers' work.

To set up your development environment, simply run:

    . scripts/setup.sh;
    
This will do a few things:

Client

* Check you have the required frontend dependecies installed (node.js, ruby)
* Install libraries required for main build tool (grunt) to work correctly
* Install project dependencies through package.json (e.g. bower) and client side scripts through bower (e.g. angular)

Server

* Check you have the required backend dependecies installed (python, virtualenv)
* Create a local database and populate it with an admin user (user:password admin:admin)

System

* Create git hooks that on code commit, will run before (to make sure all tests are passing) and after (to pull all changes and install/upgrade any libraries)

The setup script is just a helper, and if you want to set up your system manually you are free to do so. To get a better understanding of the automated development process, you can look through the setup.sh and related scripts to see what is going on.

##Further Info

README files for each sub-system (client/server) are automatically generated and will contain instructions to run/test/build the project.

