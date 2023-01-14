# module
#from logging import debug
from deta import Deta
from flask import *

# deta Base
deta = Deta("c08p64s1_M2NsZiEzbdCh4fCCK7SqBv4XAKWr3dZ3")
db = deta.Base("term")
drive = deta.Drive("term")
# flask 
app = Flask(__name__)

app.config['SECRET_KEY'] = 'madewgn'
# add to database
def add(title,url,desk):
    key = title.replace(" ","-")
    data = {'title': title,'link': url,'desk': desk}
    return db.put(data, key)

def getpost(key):
    x = db.get(key)
    return x
# def cloud(file):
#     f = open('rec/'+file, 'r')
#     x = drive.put(file,f)
#     f.close()
#     return x

@app.route("/")
def index():
    res = db.fetch()
    all_items = res.items
#    data = all_items['key']
    return render_template("index.html",post=all_items)


@app.route("/<key>")
def post(key):
    data = getpost(key)
    if data is None:
        abort(404)
    link = data["link"] + ".cast"
    title = data["title"]
    desk = data['desk']
    return render_template("post.html", title=title,link=link,desk=desk)

#    return link

# ...

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['url']
        desk = request.form['desk']

        if not title:
            flash('Title is required!')
        elif not link:
            flash('url is required!')
        elif not desk:
            flash('desk is required!')
        else:
            flash('berhasil!')
            add(title,link,desk)

            # messages.append({'title': title, 'content': content})
            # return redirect(url_for('index'))

    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
