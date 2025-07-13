from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/info')
def app_info():
    return jsonify({
        'app_name': 'DevOps Demo App',
        'version': '1.0.0',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'build_number': os.getenv('BUILD_NUMBER', 'local')
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)