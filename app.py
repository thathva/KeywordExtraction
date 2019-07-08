from flask import Flask,request,render_template
from keywords import Keywords

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/keywords', methods=['POST'])
def extract():
    obj=Keywords()
    description = request.form['comment']
    title=request.form['title']
    k=obj.vectorizer(description)
    keywords=obj.keyword(k,title)
    return render_template('result.html',pred=keywords)


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # important to mention debug=True
