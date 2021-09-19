# FlaskPhisher  v1.0
FlaskPhisher is a tool to generate phishing pages that target social media websites, making it much easier to phish targets of opportunity on any network. FlaskPhisher is developed using Python-Flask-Web-Framework.
![Main Image](https://github.com/Sithum-Nimlaka/FlaskPhisher/blob/Main/img/FlaskPhisher-Base.jpg)

# ⚠️DISCLAIMER⚠️
<p align="center">❗️EDUCATIONAL PURPOSES ONLY❗️<p>
❌The use of the FlaskPhisher & its phishing pages is COMPLETE RESPONSIBILITY of the END-USER. Developer assume NO liability and are NOT responsible for any misuse or damage caused by this program.❌
  
## AVAILABLE TUNNELLING OPTIONS
- Localhost
- Ngrok

## 🖥Tested Platforms🖥
- Windows 10
- Kali Linux 2021.3
- Ubuntu 20.4
- PearOS Catalina
- CentOS 7
- CentOS 8

## 📸SCREENSHOTS📸 (Tested Platforms)
<p align="center">Windows 10<p>
<img src="https://github.com/Sithum-Nimlaka/FlaskPhisher/blob/Main/img/flaskPhisher-windows.jpg"/>
<p align="center">Kali Linux 2021.3<p>
<img src="https://github.com/Sithum-Nimlaka/FlaskPhisher/blob/Main/img/flaskPhisher-kali-linux.jpg"/>
  
## PREREQUISITES

- Python 3.\*
- sudo
- pyngrok
  
# 🛠Installation🛠

### Windows
  - Download & Install python3
  - Download repository
  - Extract it<br>
  - `cd FlaskPhisher-Main`<br>
  - `pip install -r requirements.txt`<br>
  - `python FlaskPhisher.py`<br>
 
### Debian Based Distros
  - `sudo apt install git`<br>
  - `sudo apt-get -y install python3`<br>
  - `sudo apt-get -y install python3-pip`<br>
  - `git clone https://github.com/Sithum-Nimlaka/FlaskPhisher.git`<br>
  - `chmod 777 FlaskPhisher`<br>
  - `cd FlaskPhisher`<br>
  - `pip3 install -r requirements.txt`<br>
  - `python3 FlaskPhisher.py`<br>

### RedHat Based Distros
  - `sudo yum install git`<br>
  - `sudo yum install python3`<br>
  - `sudo yum install python3-pip`<br>
  - `git clone https://github.com/Sithum-Nimlaka/FlaskPhisher.git`<br>
  - `chmod 777 FlaskPhisher`<br>
  - `cd FlaskPhisher`<br>
  - `pip3 install -r requirements.txt`<br>
  - `python3 FlaskPhisher.py`<br>

# Features
### Save Data into Database.
- Flask Phisher is automatically saving phished credentials to the SQLite database.
- To access saved data,<br>
run `python3 savedCredentials.py`
