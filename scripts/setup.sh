#!/bin/bash

# Environmental variables to highlight the status of our code.
BOLD=$(tput bold);
ERROR=${BOLD}$(tput setaf 1);
WARNING=${BOLD}$(tput setaf 3);
INFO=${BOLD}$(tput setaf 2);
RESET=$(tput sgr0);

# Directory Variables for use with dependent scripts.
SCRIPTS="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
PROJECT="$SCRIPTS/..";
SERVER="$PROJECT/server";
CLIENT="$PROJECT/client";

if [ "$1" == "create" ]; then
    # Project Creation
    . $SCRIPTS/client/angular-grunt-project.sh;
    . $SCRIPTS/server/django-project.sh
else
    # Run custom setup commands
    . $SCRIPTS/client/angular-grunt.sh;
    . $SCRIPTS/server/django.sh;
    . $SCRIPTS/git-hooks/django-angular-grunt.sh;
fi

# Finally make sure all pulls and pushes go to master
cd $PROJECT;
git branch --set-upstream-to=origin/master master;
