from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create New Database
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create New Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return '<User %r>' % self.username


# db.create_all()

# Create New Record
# admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')

# db.session.add(admin)
db.session.add(guest)
db.session.commit()


# Read All Records
# users = User.query.all()
# print(users)

# Read A Particular Record By Query
# user = User.query.filter_by(username='crisian').first()
# print(user)

# Update A Particular Record By Query
# user_to_update = User.query.filter_by(username="crisian").first()
# user_to_update.username = "crisaian"
# db.session.commit()


# Update A Record By PRIMARY KEY
# user_id = 3
# user_to_update = User.query.get(user_id)
# user_to_update.username = "admin"
# db.session.commit()

# Delete A Particular Record By PRIMARY KEY
# user_id = 4
# user_to_delete = User.query.get(user_id)
# db.session.delete(user_to_delete)
# db.session.commit()


users = User.query.all()
print(users)

