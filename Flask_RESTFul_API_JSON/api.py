from flask import Flask, request, jsonify, make_response
from flask.wrappers import Request

from flask_sqlalchemy import SQLAlchemy
import uuid
import json
from sqlalchemy.sql.elements import True_
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import logging
from functools import wraps
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/db'


logHandler= logging.FileHandler('./logs/app.log')
logHandler.setLevel(logging.INFO)
app.logger.addHandler(logHandler)
app.logger.setLevel(logging.INFO)



db = SQLAlchemy(app)


class User(db.Model):
    id= int
    public_id=str
    name=str
    pasword=str
    admin=bool

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(90))
    admin = db.Column(db.Boolean)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            return jsonify({'message' : 'Token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user= User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid'})

        return f(current_user,*args,**kargs)

    return decorated


@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform function!'})

    data = User.query.all()
    
    users= []

    for user in data:
        print( user.public_id, user.name, user.password)
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        users.append(user_data)

    return  jsonify({'users' : users})

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user,public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform function!'})
    
    data = User.query.filter_by(public_id=public_id).first()
    if not data:
        return jsonify({'message' : 'No user Found'})

    user= {}
    user['public_id'] = data.public_id
    user['name'] = data.name
    user['admin'] = data.admin
    user['password'] = data.password

    return jsonify({'user' : user} )

@app.route('/user', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform function!'})

    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    print('the number is:', len(hashed_password))
    new_user = User(public_id=str(uuid.uuid4()),name =data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'Message': 'New User Created!'})

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user,public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform function!'})

    data = User.query.filter_by(public_id=public_id).first()
    if not data:
        return jsonify({'message' : 'No user Found'})
    
    data.admin = True
    db.session.commit()

    return jsonify({'Message':'The user has been promoted!'})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user,public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform function!'})

    data = User.query.filter_by(public_id=public_id).first()
    if not data:
        return jsonify({'message' : 'No user Found'})

    db.session.delete(data)
    db.session.commit()

    return jsonify({'message' : 'The user has been deleted!'})

@app.route('/login')
def login():
    auth = request.authorization
    # Under devolpment
    time= str(datetime.datetime.utcnow())
    test = (time , request.method, request.headers)
    app.logger.info(test)

    if not auth or not auth.username or not auth.password:
        response = make_response('Could not verify', 401, {'WWW-Authenticate':'Basic realm="Login required"'})
        responselog = (time,response.response,  response.status_code,(response.headers))
        app.logger.info(responselog)
        return response
    user = User.query.filter_by(name=auth.username).first()
    if not user:
        
        return make_response('Could not verify', 401, {'WWW-Authenticate':'Basic realm="Login required"'})
    
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30) }, app.config['SECRET_KEY'])
        
        
        return jsonify({'token': token})
    




@app.route('/todo',methods=['GET'])
@token_required
def get_all_todo(current_user):
    todos= Todo.query.filter_by(user_id=current_user.id).all()

    output = []

    for todo in todos:
        todo_data ={}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['complete'] = todo.complete
        output.append(todo_data)
    return jsonify({'todos': output})

@app.route('/todo/<todo_id>', methods=['GET'])
@token_required
def get_one_todo(current_user,todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return  jsonify({'message' : 'No todo found!'})

    todo_data ={}
    todo_data['id'] = todo.id
    todo_data['text'] = todo.text
    todo_data['complete'] = todo.complete

    return jsonify(todo_data)
@app.route('/todo', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()

    new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()


    return jsonify({'message':"Todo created!"})

@app.route('/todo/<todo_id>', methods=['PUT'])
@token_required
def complete_todo(current_user,todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return  jsonify({'message' : 'No todo found!'})

    todo.complete = True
    db.session.commit()    
    return jsonify({'message' :'Todo item has been complete'})
@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user,todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return  jsonify({'message' : 'No todo found!'})

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message':'Todo Deleted!'})

    return make_response('Could not verify', 401, {'WWW-Authenticate':'Basic realm="Login required"'})


