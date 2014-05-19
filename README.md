{project}
==========

{project} has had a development scaffold put in place to encourage best practices; the focus being on Test-Driven Development and Continuous Integration - badly tested code that is stale tends to break. This also uses company conventions to allow for faster implementation and familiarity with other developers' work.

##Setup

To setup your development environment, please run:

    . scripts/setup.sh;
    
This will do a few things:

Client

* Check you have the required frontend dependecies installed (node.js, ruby)
* Install libraries required for main build tool (grunt) to work correctly
* Install project dependencies (package.json) and client side scripts (bower.json)

Server

* Check you have the required backend dependecies installed (python, virtualenv)
* Create a local database and populate it with an admin user (user:password admin:admin)

System

* Create git hooks that on code commit, will run before (to make sure all tests are passing) and after (to pull all changes and install/upgrade any libraries)

The setup script is just a helper, and if you want to set up your system manually you are free to do so. To get a better understanding of the automated development process, you can look through the setup.sh and related scripts to see what is going on.

##Further Info

README files for each sub-system (client/server) are automatically generated and will contain instructions to run/test/build the project.

