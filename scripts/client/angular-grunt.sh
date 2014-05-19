#!/bin/bash

# Make sure we have node installed
. $SCRIPTS/client/dependency/node.sh;

# As angular generator requires SASS/Compass check that too
. $SCRIPTS/client/dependency/sass.sh;

cd $CLIENT;

# Global dependencies
npm install -g grunt grunt-cli bower;

# Local dependencies
npm install;
bower install;
npm install karma-jasmine --save-dev;
npm install karma-chrome-launcher --save-dev;

# Add Yeoman Angular generator hooks for pre/post commit
. $SCRIPTS/git-hooks/angular-grunt.sh;