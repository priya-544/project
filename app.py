from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///kitchen.db"
db = SQLAlchemy(app)  

class seller(db.Model):
    user_id=db.Column(db.VARCHAR(20), primary_key=True)
    password=db.Column(db.String(100),nullable=False)
    name=db.Column(db.String(100), nullable=False)
    phone_num=db.Column(db.Integer(),  nullable=False)
    email=db.Column(db.String(50), nullable=True)
    address=db.Column(db.VARCHAR(100), nullable=False)
    image=db.Column(db.String(20), nullable=True, default='default.jpg')
    status=db.Column(db.String(10), nullable=False)
    description=db.Column(db.String(200),nullable=False)
    type=db.Column(db.String(10),nullable=False)

    def __repr__(self) -> str:
        return f"kitchen('{self.user_id}','{self.name}','{self.phone_num}','{self.email}','{self.address}','{self.image}','{self.status}','{self.description}''{self.type}')"
    
@app.route('/')
def home():
        return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        user_id = request.form['user_id']
        password = request.form['password']
        name = request.form['name']
        phone_num = request.form['phone_num']
        email = request.form['email']
        address = request.form['address']
        image = request.form['image']
        description = request.form['description']
        status=request.form['status']
        type=request.form['type']
        seller1=seller(user_id=user_id,password=password, name=name, phone_num=phone_num, address=address,status=status, description=description,type=type )
        db.session.add(seller1)
        db.session.commit()
    allsellers=seller.query.all()
    print(allsellers)
    return render_template('index.html',allsellers=allsellers)

class buyer(db.Model):
        user_id=db.Column(db.VARCHAR(20), primary_key=True)
        password=db.Column(db.String(100),nullable=False)
        name=db.Column(db.String(100), nullable=False)
        phone_num=db.Column(db.Integer(),  nullable=False)
        email=db.Column(db.String(50), nullable=True )
        address=db.Column(db.VARCHAR(100), nullable=False)
        image=db.Column(db.String(20), nullable=False, default='default.jpg')   

@app.route('/regst', methods=['GET','POST'])
def stu_reg():
    if request.method=='POST':
        user_id = request.form['user_id']
        password = request.form['password']
        name = request.form['name']
        phone_num = request.form['phone_num']
        email = request.form['email']
        address = request.form['address']
        image = request.form['image']
        buyer1=buyer(user_id=user_id,password=password, name=name, phone_num=phone_num, address=address,image=image )
        db.session.add(buyer1)
        db.session.commit()
    allbuyers=buyer.query.all()
    print(allbuyers)
    return render_template('register_st.html',allbuyers=allbuyers)

@app.route('/allsellers')
def allseller():
        allsellers=seller.query.all()
        return render_template('all_sellers.html')

class menu(db.Model):
    day=db.Column(db.String(20), nullable=False, primary_key=True)
    lunch=db.Column(db.String(100), nullable=False)
    dinner=db.Column(db.String(100), nullable=False)
    specials=db.Column(db.String(100), nullable=True)
    price=db.Column(db.Integer, nullable=True)

@app.route('/menu', methods=['GET','POST'])
def menu():
    if request.method=='POST':
        day = request.form['day']
        lunch = request.form['lunch']
        dinner = request.form['dinner']
        specials = request.form['specials']
        price = request.form['price']
        menu1=menu(day=day,lunch=lunch,dinner=dinner,specials=specials,price=price)
        db.session.add(menu1)
        db.session.commit()
    allmenu=menu.query.all()
    print(allmenu)
    return render_template('menu.html',allmenu=allmenu)

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/about')
def about():
    return render_template('home.html')

@app.route('/show')
def Sellers():
    allsellers=seller.query.all()
    print(allsellers)
    return 'this is Sellers page'

# @app.route('/menu', methods=['GET','POST'])
# def menu():
#     if request.method=='POST':
#         day = request.form['day']
#         lunch = request.form['lunch']
#         dinner = request.form['dinner']
#         specials = request.form['specials']
#         price = request.form['price']
#         menu1=menu(day=day,lunch=lunch,dinner=dinner,specials=specials,price=price)
#         db.session.add(menu1)
#         db.session.commit()
#     allmenu=seller.query.all()
#     print(allmenu)
#     return render_template('menu.html',allmenu=allmenu)

@app.route('/update/<string:user_id>')
def update(user_id):
    seller1=seller.query.filter_by(user_id=user_id).first()
    return render_template('update.html',seller1=seller1)

@app.route('/delete/<string:user_id>')
def delete(user_id):
    seller1=seller.query.filter_by(user_id=user_id).first()
    db.session.delete(seller1)
    db.session.commit()
    return redirect("/register")

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/prosellers')
def proseller():
        return render_template('profile_seller.html')

@app.route('/order')
def order():
        return render_template('order_item.html')

@app.route('/ordersuccess')
def ordersuccess():
        return render_template('order.html')

@app.route('/studentprofile')
def stuprofile():
        
            return render_template('stu_profile.html')

@app.route('/prost')
def prost():
        
            return render_template('prost_seller.html')

if __name__ == "__main__":
    app.run(debug=True)
