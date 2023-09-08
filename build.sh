set -o errexit

python -m venv venv
pip install -- upgrade pip
pip install -r requirements.txt
python -m pip install flask
