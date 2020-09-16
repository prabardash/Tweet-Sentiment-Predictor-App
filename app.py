from flask import Flask, request, url_for, render_template, render_template_string
from flask_bootstrap import Bootstrap
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

import numpy as np
import pickle

from tweet_access import TwitterClient
import TweetCleaner


app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

category=[]
with open('Tokenizer/tokenizer.pickle', 'rb') as handle:
    tok = pickle.load(handle)
with open('Tokenizer/label_tokenizer.pickle', 'rb') as handle:
    label_tok = pickle.load(handle)
tc = TwitterClient()
api = tc.get_twitter_client_api()
tcl = TweetCleaner.TweetCleaner()
label_dict = {1:'neutral', 2:'positive', 3: 'negative'}
model = load_model('models/LSTM_emb-v1.0_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_keyword',methods=['POST','GET'])
def process_keyword():
    #val = request.form.get("val")
    val = request.form["keyword"]
    tweets = tc.get_searched_tweets(query= val, num_tweets= 10, api = api)

    for idx, val in enumerate(tweets):
        #print(val)
        text = tcl.inference_clean(str(val))
        #print(text)
        token_sequence = tok.texts_to_sequences([text])
        pad_seq = np.array(pad_sequences(token_sequence, maxlen=34, padding='post'))
        p=np.argmax(model.predict(pad_seq))
        #print(p)

        for key, val in label_tok.word_index.items():
            if p == val:
                category.append(key)

    return render_template('predictions.html', tweets = tweets, predictions = category, length = len(tweets))



if __name__ == "__main__":
    app.run(debug=True)
