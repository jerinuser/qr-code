from flask import Flask, render_template, request, send_file
import pyqrcode
import os

app = Flask(__name__)

QR_DIR = '/tmp'  # Use the /tmp directory for Vercel compatibility

@app.route('/', methods=['GET', 'POST'])
def qr_code():
    if request.method == 'POST':
        link = request.form.get('link')
        
        if link:
            # Generate QR code and save it to the /tmp directory
            url = pyqrcode.create(link)
            qr_filename = 'generated_qr.png'
            qr_filepath = os.path.join(QR_DIR, qr_filename)
            url.png(qr_filepath, scale=10)
            
            # Serve the generated QR code from the custom route
            return render_template('index.html', qr_code_image=qr_filename, link=link)
    
    return render_template('index.html', qr_code_image=None)

@app.route('/qr_code_image')
def serve_qr_code():
    # Serve the generated QR code from the /tmp directory
    qr_filepath = os.path.join(QR_DIR, 'generated_qr.png')
    if os.path.exists(qr_filepath):
        return send_file(qr_filepath, mimetype='image/png')
    return "QR code not found", 404

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for deployment
