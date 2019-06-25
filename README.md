# mp3-video_converter

git clone https://github.com/AIDARXAN/mp3-video_converter

virtualenv mp3_env -p python3
source mp3_env/bin/activate
pip install -r requirements.txt

in folder with settings.py create file secrets.py
and put SECRET_KEY="your_key"

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
