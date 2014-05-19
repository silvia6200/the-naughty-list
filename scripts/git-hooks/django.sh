#!/bin/bash

cd $PROJECT;

echo "
# Django
cd ${SERVER};
. venv/bin/activate;
./manage.py test;" >> .git/hooks/pre-commit;
echo '
if [ $? != 0 ]; then
    exit 1;
fi' >> .git/hooks/pre-commit;

echo "
# Django
cd ${PROJECT};
git pull;
cd ${SERVER};
. venv/bin/activate;
pip install -r requirements.txt;
./manage.py syncdb --noinput;
./manage.py migrate;" >> .git/hooks/post-commit;
