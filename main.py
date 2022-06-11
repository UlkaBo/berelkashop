import sqlite3

from flask import Flask, render_template, request, redirect, url_for, make_response, session, send_from_directory, send_file, abort
from werkzeug.utils import secure_filename
from pathlib import Path
from models import Item, Image
from _config import app, db, ALLOWED_EXTENSIONS, SECRET_KEY


def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    print('----', dir(session))
    print(session.modified)
    #del session['list_cart']
    items = Item.query.all() #.order_by(Item.id)
    print('begin')
    return render_template('index.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin', methods=["POST", "GET"])
def login_admin():
    if 'userLogged' in session:
        return redirect(url_for('create_item', username=session['userLogged']))

    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == '123':

            session['userLogged'] = request.form['username']
            return redirect(url_for('create_item', username=session['userLogged']))
    return render_template('login_admin.html', title='вхід адміна')


@app.route('/create_item', methods=['POST', 'GET'])
def create_item():
    if request.method == "POST":
        title = request.form['title']
        width = request.form['width']
        height = request.form['height']
        materials = request.form['materials']
        about = request.form['about']
        price = request.form['price']
        name_title = title.replace(' ', '_')
        item = Item(title=title, width=width, height=height, materials=materials, about=about,
                    price=price)
        for i in range(1, 11):

            link_im = upload_file(i, request.files, name_title)
            print('-'+str(link_im)+'-')
            if link_im:
                image = Image(link=link_im, item=item)
                try:
                    db.session.add(image)
                    print('image added')
                except:
                    return f"Error. The image {link_im} doesn't add to database"

        try:
            db.session.add(item)
            print('yes')

        except:
            return "Error. The item doesn't add to database"

        db.session.commit()
        print('commited')
        return redirect(url_for('create_item'))
    else:
        return render_template('create_item.html')


def upload_file(index, files, name_title):
    if 'file' + str(index) in files:
        image = request.files['file' + str(index)]
        if image and allowed_filename(image.filename):
            filename = secure_filename(image.filename)
            print(filename)
            path_dir = Path(app.config['UPLOAD_FOLDER'], name_title)
            if not path_dir.exists():
                path_dir.mkdir()
            path = Path(app.config['UPLOAD_FOLDER'], name_title, filename)
            image.save(path)

            send_from_directory(str(path_dir), filename)
            #return redirect(url_for('download_file', name=str(path)))
            return str(path)
    return ''
'''
@app.route('/<name>')
def download_file(name):
    return send_from_directory(name)
'''

'''
@app.route('/event/<int:id>/logo') 
def event_logo(id): 
    event = Item.query.get_or_404(id) 
    return app.response_class(event.im1, mimetype='application/octet-stream')
'''
@app.route('/item/<int:id>')
def item(id):
    data = Item.query.get(id)  # .order_by(Item.id)
    return render_template('item.html', data=data)

@app.route('/cart/<int:id>')
def cart(id):
    if 'list_cart' in session:
        list_cart = session['list_cart']
        list_cart.append(id)
    else:
        list_cart = []
        list_cart.append(id)
    session['list_cart'] = list_cart
    print(session.items())
    print(session.modified)
    #Item.query.filter_by(id)
    return render_template('cart.html', data=list_cart)

if __name__ == '__main__':

    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
