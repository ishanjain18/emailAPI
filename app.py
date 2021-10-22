from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        file = request.files["filename"]
        content = request.form['content']

        if file:
            # Contains list of email addresses
            addresses = [i.decode('utf-8').replace("\r\n", "") for i in file.readlines()]

            for i in range(len(addresses)): 
                try:
                    senderEmail = "Add sender email here"
                    receiverEmail = addresses[i]
                    # Password has to be generated using app password if using gmail.
                    senderPass = "Add sender password here"
                except:
                    return render_template("index.html")

                message = MIMEMultipart()
                message['From'] = senderEmail
                message['To'] =  receiverEmail
                message['Subject'] =  'Mail sent using python'
                
                mail_content = content
                message.attach(MIMEText(mail_content, 'plain'))

                s = smtplib.SMTP('smtp.gmail.com', 587) 
                s.starttls() 
                s.login(senderEmail, senderPass) 
                text = message.as_string()
                s.sendmail(senderEmail, receiverEmail, text) 
                s.quit() 

                print('Mail Sent')

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)