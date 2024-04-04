from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///kitchen.db"
db=SQLAlchemy(app)

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
    
    class buyer(db.Model):
        user_id=db.Column(db.VARCHAR(20), primary_key=True)
        password=db.Column(db.String(100),nullable=False)
        name=db.Column(db.String(100), nullable=False)
        phone_num=db.Column(db.Integer(),  nullable=False)
        email=db.Column(db.String(50), nullable=True)
        address=db.Column(db.VARCHAR(100), nullable=False)
        image=db.Column(db.String(20), nullable=False, default='default.jpg')
    
@app.route('/', methods=['GET','POST'])
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

@app.route('/show')
def Sellers():
    allsellers=seller.query.all()
    print(allsellers)
    return 'this is Sellers page'

@app.route('/update/<string:user_id>')
def update(user_id):
    seller1=seller.query.filter_by(user_id=user_id).first()
    return render_template('update.html',seller1=seller1)

@app.route('/delete/<string:user_id>')
def delete(user_id):
    seller1=seller.query.filter_by(user_id=user_id).first()
    db.session.delete(seller1)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
