#!/bin/bash

# A script to test for node.js existence.

cd $PROJECT_ROOT;

command -v npm >/dev/null 2>&1;
if [ $? != 0 ]; then
    echo "${ERROR}ERROR: node.js not found. Please install specific to your OS. Check www.nodejs.org.${RESET}" >&2;
    exit 1;
fi

