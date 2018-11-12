from flask import Flask, render_template,url_for,request
from formss.InputForm import InputForm
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

app =Flask(__name__)
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

@app.route("/")
def home():
	forma = InputForm()
	return render_template('home.html',forma=forma)

@app.route("/prediction", methods=["GET","POST"])
def prediction():
	Dataframe=pd.read_csv('/home/srijan/Desktop/Youtubespam/YoutubeSpamMergedData.csv')
	X=Dataframe.iloc[:,5].values
	Y=Dataframe.iloc[:,6].values
	tem=X
	count_vectorizer=CountVectorizer()
	X=count_vectorizer.fit_transform(tem).toarray()
	from sklearn.model_selection import train_test_split
	X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=1412)
	from sklearn.naive_bayes import MultinomialNB
	classifier=MultinomialNB()
	classifier.fit(X_train,Y_train)

	if request.method == 'POST':
		comment = request.form['comment']
		val=[comment]
		vec=count_vectorizer.transform(val).toarray()
		prediction=classifier.predict(vec)
	return render_template('result.html',prediction=prediction)



if __name__ == '__main__':
	app.run(debug=True)