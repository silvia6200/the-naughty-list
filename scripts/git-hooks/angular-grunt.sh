#!/bin/bash

cd $PROJECT;

echo "
# Yeoman Angular Grunt
cd ${CLIENT};
grunt test;" >> .git/hooks/pre-commit;
echo '
if [ $? != 0 ]; then
    exit 1;
fi' >> .git/hooks/pre-commit;

echo "
# Yeoman Angular Grunt
cd ${PROJECT};
git pull;
cd ${CLIENT};
npm install;
bower install;" >> .git/hooks/post-commit;
chmod +x .git/hooks/post-commit;
