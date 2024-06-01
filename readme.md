# Project Install Instructions

## install

1. clone
2. pip install -r requirements.txt

git clone https://github.com/d-yerovi/myproject.git

cd myproject

source venv/bin/activate

pip3 install -r requirements.txt

pytest --pylint --cov

## Git commnad examples

  git status

  git branch

  git checkout -b pylintrcUpdate

  mvim .pylintrc

  git status

  git commit -am "update .pylintrc file"

  git push origin pylintrcUpdate

  git fetch

  git checkout master

  cat .pylintrc

  git pull origin master

  cat .pylintrc

## Start Env
1. virtualenv venv <- Makes a virtual environment in the venv directory (you can make this any directory but you will have to remember it to activate it correctlty)

or 

virtualenv -p python3 <desired-path> <- Creation of virtualenv

2. source ./venv/bin/activate <- you should see (venv) in the terminal command line to indicate that the venv environment of your project is activated
3. deactivate <- Deactivate the virtualenv

## Testing

1. pytest <-runs the tests without pylint or coverage
2. pytest --pylint <- Runs tests with pylint static code analysis
3. pytest --pylint --cov <-Runs tests, pylint, and coverage to check if you have all your code tested.

