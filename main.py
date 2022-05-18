import sqlite3
from flask import Flask, render_template, request, redirect, url_for, make_response, session
from models import Item
from _config import app, db


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin', methods=["POST", "GET"])
def login_admin():
    if 'userLogged' in session:
        print(1)
        return redirect(url_for('create_item', username=session['userLogged']))
    print(vars(session))
    if request.method == "POST":
        print(vars(session))

        if request.form['username'] == 'admin' and request.form['password'] == '123':

            session['userLogged'] = request.form['username']
            print('---',vars(session))
            return redirect(url_for('create_item', username=session['userLogged']))
    return render_template('login_admin.html', title='вхід адміна')


@app.route('/create_item', methods=['POST', 'GET'])
def create_item():
    if request.method == "POST":
        title = request.form['title']
        size = request.form['size']
        price = request.form['price']
        im1 = request.files['file1'].read()

        '''im2 = request.files['file2'].read()
        im3 = request.files['file3'].read()
        im4 = request.files['file4'].read()
        im5 = request.files['file5'].read()
        im6 = request.files['file6'].read()
        im7 = request.files['file7'].read()
        im8 = request.files['file8'].read()
        im9 = request.files['file9'].read()
        im10 = request.files['file10'].read()'''

        binary1 = sqlite3.Binary(im1)
        item = Item(title=title, size=size, price=price, im1=binary1)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('create_item'))
        except:
            return "Error. The item doesn't add to database"

    else:
        return render_template('create_item.html')
'''
@app.route('/event/<int:id>/logo') 
def event_logo(id): 
    event = Item.query.get_or_404(id) 
    return app.response_class(event.im1, mimetype='application/octet-stream')
'''

@app.route('/im/<int:id>')
def im(id):
    item = Item.query.get(id)
    b_image = item.im1
    image = make_response(b_image)
    image.headers['Content-Type'] = 'image/png'
    return image

if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
