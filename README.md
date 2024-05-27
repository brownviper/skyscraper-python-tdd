# skyscraper-python-tdd
tdd-ing skyscraper solution in python

[![pipeline status](https://gitlab.com/brownviper/flask-tdd-docker/badges/master/pipeline.svg)](https://github.com/brownviper/skyscraper-python-tdd/commits/main)

# Steps to run the project:

## pyenv install:
follow instruction from: https://k0nze.dev/posts/install-pyenv-venv-vscode/#using-pyenv

## running via docker compose
```bash
docker compose up -d --build
````
## to show logs to check the result
```bash
docker compose logs
````

## running locally
### python setup
```bash
 pyenv local 3.12.2
 python -m venv .venv
```
### activate env
```bash
.\.venv\Scripts\activate
pip install -r .\requirements.txt
```
### running the test
```bash
python -m pytest "src/tests"
```
### to deactivate the venv
```bash
deactivate
```