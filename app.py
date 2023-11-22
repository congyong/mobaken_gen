# app.py

import os
import tempfile
from flask import Flask, request, send_file, make_response
from MobaXterm_Keygen import GenerateLicense, VariantBase64Encode, EncryptBytes

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html', 'r').read()

@app.route('/generate_license', methods=['POST'])
def generate_license_route():
    username = request.form['username']
    version = request.form['version']

    # Call the generate_license function
    GenerateLicense(1, 1, username, *map(int, version.split('.')))

    # Read the binary content of the generated license file
    with open('Custom.mxtpro', 'rb') as file:
        license_content = file.read()

    # Remove the generated license file
    try:
        os.remove('Custom.mxtpro')
    except Exception as e:
        app.logger.error(f"Error removing temporary file: {e}")

    # Create a response with the binary content
    response = make_response(license_content)
    response.headers["Content-Disposition"] = "attachment; filename=Custom.mxtpro"

    return response

if __name__ == '__main__':
    app.run(debug=True)
