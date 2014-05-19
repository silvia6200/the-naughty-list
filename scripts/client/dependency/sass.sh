#!/bin/bash

# Make sure we have ruby installed
. $SCRIPTS/client/dependency/ruby.sh

echo 'Installing Compass (if required)...'

command -v compass >/dev/null 2>&1;
if [ $? != 0 ]; then
    echo "${WARN}WARN: compass not found. Attempting to install without sudo.${RESET}" >&2;
    gem install compass;
    if [ $? != 0 ]; then
        echo "${WARN}WARN: compass gem not installable as current user, attempting sudo.${RESET}" >&2;
        sudo gem install compass;
        if [ $? != 0 ]; then
            echo "${ERROR}ERROR: compass not installed. Please try a different method.${RESET}" >&2;
            exit 1;
        fi
    fi
fi