# python-selenium

Steps to begin from scratch:

- download pycharm community
- create a project from pycharm with the python3
- install the python3 if not, please see wiki about how to install homebrew, git, gh, python3 
- pip install selenium
- brew install --cask chromedriver (install the chrome binary [link](https://gist.github.com/derhuerst/1b15ff4652a867391f03))
- run the main.py file to see it it can open the chrome browser

```
from selenium import webdriver

driver = webdriver.Chrome()

```

- git init -b main
- gh repo create project-name [link](https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line#adding-a-project-to-github-with-github-cli)

### Alert that you should not run the script a lot, in a number of times, too much because the server will automatically identify your public ip address and block you
Then, it's not nice that you have to contact the website and explain that you're not harmful to them. 









