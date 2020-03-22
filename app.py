import flask
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import tweepy
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC

app = flask.Flask(__name__, template_folder='templates')

classifier = pickle.load(open('model/svm_classifier.pkl','rb'))
tfidf = pickle.load(open('model/tfidf_variable.pkl', 'rb'))

def fetch(tweet_id):
	
	#Consumer Key (API Key), Consumer Secret (API Secret)
	auth = tweepy.OAuthHandler('Tq1Es6PFDkXhjzcAHdC2YCGKa', 
	                           'fcowbhzP67soVqeFWpHfKn2L5ytPfTnJfflDZbyEMCSFy2npG6')
	# Access Token, Access Token Secret
	auth.set_access_token('1216656616310730752-CVHCA320WI9heRVI7LkVMlrRWcbxq8', 
	                      'e2hXM57Zfp8PBwah1QOFLRDbaqiqIgcnsfn1Pw2iu0SjZ')
	api = tweepy.API(auth, wait_on_rate_limit=True)

	tweet = api.get_status(tweet_id)

	retweet_count_unseen = tweet.retweet_count
	user_id_unseen = tweet.user.id
	user_unseen = api.get_user(user_id_unseen)
	follower_count_unseen = user_unseen.followers_count
	friends_count_unseen = user_unseen.friends_count
	text_unseen = tweet.text.lower()
	df_testset = pd.DataFrame([[text_unseen, retweet_count_unseen, friends_count_unseen, follower_count_unseen]], columns=['text', 'retweet', 'friends', 'followers'],dtype=float)
	df_testset = df_testset.replace(np.nan, '', regex=True)

	df_unseen_vect = pd.DataFrame(tfidf.transform(df_testset['text']).toarray())
	retweet_unseen_test = df_testset[['retweet']]
	follower_unseen_test = df_testset[['followers']]
	friends_unseen_test = df_testset[['friends']]

	retweet_unseen_test.reset_index(drop=True, inplace=True)
	follower_unseen_test.reset_index(drop=True, inplace=True)
	friends_unseen_test.reset_index(drop=True, inplace=True)

	c = [retweet_unseen_test, follower_unseen_test, friends_unseen_test, df_unseen_vect]
	X_test_unseen_features = pd.concat(c, axis=1)

	y_predict_svc = classifier.predict(X_test_unseen_features)

	return y_predict_svc[0]


@app.route('/', methods=['GET', 'POST'])
def main():
  if flask.request.method == 'GET':
    return(flask.render_template('main.html'))
  if flask.request.method == 'POST':
    tweet_id = flask.request.form['tweet_id']

    prediction = fetch(tweet_id)

    if prediction==1:
    	result="Oops!!! Rumor Tweet Found"
    else:
    	result = "Hurray! Non-rumor Tweet Found"
    return flask.render_template('main.html',original_input={'Tweet ID':tweet_id},result = result)

if __name__ == '__main__':
  app.run(debug=True)