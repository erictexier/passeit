pip3 install virtualenv
virtualenv /Users/eric/42_folder/passeit/django -p /usr/bin/python3

cd /Users/eric/42_folder/passeit/django/D04/ex00

source bin/activate
pip3 install Django
# pip3 install mysql-client
pip freeze > requirements.txt

python bin/django-admin.py startproject d04
cd d04
python manage.py runserver

pip install psycopg2-binary
conda install -c conda-forge django-crispy-forms


# for data base from source
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
brew update && brew install openssl
homebrew/bin/brew install postgresql 
# update
brew postgresql-upgrade-database
# only on demand:
# not that for now pg_ctl -D /usr/local/var/postgres start

initdb d05.db
pg_ctl -D d05.db -l logfile start


# fix in case:
mkdir /usr/local/var/postgres/pg_tblspc\nmkdir /usr/local/var/postgres/pg_twophase\nmkdir /usr/local/var/postgres/pg_stat\nmkdir /usr/local/var/postgres/pg_stat_tmp\nmkdir /usr/local/var/postgres/pg_replslot\nmkdir /usr/local/var/postgres/pg_commit_ts
 1169  pg_ctl -D /usr/local/var/postgres start
# start database
brew services start postgresql
==> Successfully started `postgresql` (label: homebrew.mxcl.postgresql)
# https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

initdb formationdjango
createdb formationdjango
# https://www.a2hosting.com/kb/developer-corner/postgresql/managing-postgresql-databases-and-users-from-the-command-line
 pg_ctl -D formationdjango -l logfile start
 createuser --interactive --pwprompt



 psql postgres
