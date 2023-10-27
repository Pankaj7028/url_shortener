from flask import Flask, request, render_template, jsonify, redirect
import shortuuid

app = Flask(__name__)
url_data = {}

def generate_short_url():
    return shortuuid.uuid()[:6]  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('long_url')
    title = request.form.get('title')  
    short_url = generate_short_url()

    url_data[short_url] = {
        'long_url': long_url,
        'title': title,
        'hit_count': 0
    }
    return f"Short URL: {short_url}"

@app.route('/search', methods=['GET'])
def search_urls():
    term = request.args.get('term')
    results = []

    for short_url, data in url_data.items():
        if term in data['title']:
            results.append({
                'title': data['title'],
                'url': data['long_url'],
                'short_url': short_url
            })
    return jsonify(results)

@app.route('/<short_url>', methods=['GET'])
def get_url(short_url):
    if short_url in url_data:
        url_data[short_url]['hit_count'] += 1
        return redirect(url_data[short_url]['long_url'])
    else:
        return "URL not found"

if __name__ == '__main__':
    app.run(debug=True)