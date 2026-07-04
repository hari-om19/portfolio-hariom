from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ==================== 1. STATIC SCRAPING ROUTES ====================
@app.route('/static-scraping')
def static_scraping():
    return render_template('static_scraping.html')

@app.route('/static-scraping/goodreads')
def goodreads(): 
    return render_template('goodreads.html')

@app.route('/static-scraping/sandbox')
def sandbox(): 
    return render_template('sandbox.html')

@app.route('/static-scraping/amazon')
def amazon(): 
    return render_template('amazon.html')

@app.route('/static-scraping/flipkart')
def flipkart(): 
    return render_template('flipkart.html')

@app.route('/static-scraping/news')
def news(): 
    return render_template('news.html')


# ==================== 2. DYNAMIC SCRAPING ROUTES ====================
@app.route('/dynamic-scraping')
def dynamic_scraping():
    return render_template('dynamic_scraping.html')

@app.route('/dynamic-scraping/imdb')
def dynamic_imdb():
    return render_template('dyn_imdb.html')

@app.route('/dynamic-scraping/youtube')
def dynamic_youtube():
    return render_template('dyn_youtube.html')

@app.route('/dynamic-scraping/twitter')
def dynamic_twitter():
    return render_template('dyn_twitter.html')

@app.route('/dynamic-scraping/linkedin')
def dynamic_linkedin():
    return render_template('dyn_linkedin.html')

@app.route('/dynamic-scraping/stocks')
def dynamic_stocks():
    return render_template('dyn_stocks.html')


# ==================== 3. API INTEGRATION ROUTES ====================
@app.route('/api-integration')
def api_integration():
    return render_template('api_integration.html')

@app.route('/api-integration/weather')
def api_weather():
    return render_template('api_weather.html')


if __name__ == '__main__':
    app.run(debug=True)