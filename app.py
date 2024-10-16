from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("patterns.html")

@app.route('/findMatch', methods=['POST'])
def findMatch():
    pattern = str(request.form["pattern"])
    text = str(request.form["textValue"])

    try:
        patt = re.compile(pattern)
        matches = re.finditer(patt, text)
        match_list = [match.group() for match in matches]
        Notfound = len(match_list) == 0
    except re.error:
        match_list = []
        Notfound = True  # Indicate that no matches were found due to invalid regex

    return render_template("patterns.html", match_list=match_list, Notfound=Notfound)

@app.route('/checkMail')
def checkMail():
    return render_template("mail.html")

@app.route('/validate', methods=['POST'])
def validate():
    mail_pattern = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    mail_ID = str(request.form["mail"])
    valid = re.match(mail_pattern, mail_ID)

    result = f"{mail_ID} is a valid Email ID" if valid else f"{mail_ID} is not a valid Email ID"
    return render_template('mail.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
