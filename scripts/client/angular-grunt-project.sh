#!/bin/bash

# Make sure we have node installed
. $SCRIPTS/client/dependency/node.sh;

# As angular generator requires SASS/Compass check that too
. $SCRIPTS/client/dependency/sass.sh;

mkdir -p $CLIENT;
cd $CLIENT;

npm install -g yo generator-angular;
yo angular;

echo "Client Commands
===============

The client side on this project makes use of [grunt](http://gruntjs.com/) task runner to automate work.

To run the server:

    grunt serve

To test your code:

    grunt test

To build the project (including minification and compilation) to a distributable folder:

    grunt build

See Gruntfile.js for more tasks that are available.
" > README.md