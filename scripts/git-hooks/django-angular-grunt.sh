#!/bin/bash

cd $PROJECT;

echo "#!/bin/bash" > .git/hooks/pre-commit;
echo "#!/bin/bash" > .git/hooks/post-commit;

. $SCRIPTS/git-hooks/django.sh;
. $SCRIPTS/git-hooks/angular-grunt.sh;

chmod +x .git/hooks/pre-commit .git/hooks/post-commit;