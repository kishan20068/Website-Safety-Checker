from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy function to check URL safety (to be improved later)
def check_url_safety(url):
    # Simple logic: mark as 'Safe' if 'https', 'Danger' if 'phishing' in url, else 'Spam'
    if 'phishing' in url:
        return 'Danger'
    elif url.startswith('https'):
        return 'Safe'
    else:
        return 'Spam'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')
        result = check_url_safety(url)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) 