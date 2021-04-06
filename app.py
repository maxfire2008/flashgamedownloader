from flask import Flask
from flask import send_file
import os
import requests
import cookieheaders

if "RUNFLASHGAMEDOWNLOADER" in os.environ and os.environ["RUNFLASHGAMEDOWNLOADER"] == "iu":
    app = Flask(__name__)

    @app.route('/')
    @app.route('/<path:dummy>')
    def fallback(dummy=''):
        try:
            open("downloadtmp\\"+dummy.replace("/","\\"),"rb")
        except:
            downloadurl = open("downloadurl.txt","rb").read().decode()
            filename="downloadtmp\\"+dummy.replace("/","\\")
            url = downloadurl+dummy
            r = requests.get(url, allow_redirects=True,
                             cookies=cookieheaders.cookies,
                             headers=cookieheaders.headers)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            open(filename, 'wb+').write(r.content)
        return send_file("downloadtmp\\"+dummy.replace("/","\\"), cache_timeout=0)
##        return dummy
##        return "downloadtmp\\"+dummy.replace("/","\\")
else:
    print("""--------
WARNING!!!
This app opens a web server that given the
right address can open all of your files.
Secure this web server very well!

If you understand the risks set the
enviroment variable "RUNFLASHGAMEDOWNLOADER"
to the text "iu"
--------""")
