from flask import Flask, request, render_template,jsonify
app = Flask(__name__)
def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine
@app.route('/')
def home():
    return render_template('twitter.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text = request.form['hashtag']
   while True:
    
    tweets = api.search_recent_tweets('#ipl2020').data
    i=1
    for tweet in tweets:
        original_tweet = tweet.text
        clean_tweet = preprocess(original_tweet)
        sentiment = get_sentiment(clean_tweet)
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
