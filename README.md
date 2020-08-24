# changedip
Python script for automated response when public IP address changes of device running it, with encrypted email using gnupg

### NOTE: email and password are stored plaintext in two separate files: email.txt and password.txt, use it with servers you trust.

#### Dependencies:

##### Python2: if you are running raspberry pi with Raspbian you need python2 and requireing modules, you install them with these commands:

`sudo apt install python-pip` 

`sudo pip install requests python-gnupg` 

##### Python3:

`sudo apt install python3-pip`

`sudo pip3 install python-gnupg`

#### Usage:

You begin with entering your credentials for email account you want to use to send email, and you must have public key in your gnupg keyring for encryption of mail to recipient you want to send to.

Just edit line  __13__ and lines __49__ and __50__, you will see explanation for them in code.

Script recognises some servers with smtp protocol and will automatically set correct one (if its listed) when sending email.

Usable with cron.

Any suggestions appreciated.

