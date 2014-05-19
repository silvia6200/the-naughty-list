#!/bin/bash

# A script to test for Ruby existence.
cd $PROJECT;

echo 'Checking Ruby installed...'

command -v ruby >/dev/null 2>&1;
if [ $? != 0 ]; then
    echo "${ERROR}ERROR: Ruby not found. Please install specific to your OS. Check www.ruby-lang.org.${RESET}" >&2;
    exit 1;
fi

