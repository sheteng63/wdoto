pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
uwsgi3 -x wdoto.xml