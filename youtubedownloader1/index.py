from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
	filename1 = request.args.get('filename1')
	filename2 = request.args.get('filename2')
	return render_template('index.html', filename1=filename1,filename2=filename2)

@app.route('/submit', methods=['POST'])
def post_submit():
	yt = YouTube()
	url = request.form.get('url1')
	yt.url = url
	video = yt.get('mp4','360p')
	video.download('./')
	filename1 = yt.filename

	url = request.form.get('url2')
	yt.url = url
	video = yt.get('mp4','360p')
	video.download('./')
	filename2 = yt.filename

	print(filename1)
	print(filename2)

	return redirect(url_for('index',filename1=filename1,filename2=filename2))

if __name__ == '__main__':
	app.run(debug=True)