from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    options = request.form.getlist('options')  # Get selected options as a list
    nmap_command = ['nmap'] + options + [target]
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    scan_output = result.stdout
    return render_template('scan_result.html', scan_output=scan_output)

if __name__ == '__main__':
    app.run(port=5000)
