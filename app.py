from flask import Flask, render_template, request
import pyqrcode
import os

app = Flask(__name__)

QR_DIR = 'static'

@app.route('/', methods=['GET', 'POST'])
def qr_code():
    if request.method == 'POST':
        link = request.form.get('link')
        
        if link:
            url = pyqrcode.create(link)
            qr_filename = 'generated_qr.png'
            qr_filepath = os.path.join(QR_DIR, qr_filename)
            url.png(qr_filepath, scale=10)
            
            return render_template('index.html', qr_code_image=qr_filename, link=link)
    
    return render_template('index.html', qr_code_image=None)

if __name__ == '__main__':
    app.run(debug=True)
