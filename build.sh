pip install -r requirements.txt

python3.9 manage.py migrate

python3.9 manage.py tailwind install
python3.9 manage.py tailwind build

python3.9 manage.py collectstatic  --noinput