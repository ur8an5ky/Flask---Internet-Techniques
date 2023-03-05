from App import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return PageUser.query.get(int(id))

class PageUser(db.Model, UserMixin):
    __table_args__ = {"schema":"ti"}
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    def __repr__(self):
        return f'User {self.username}: {self.email}'

    def get_username(self):
        return self.username

    # @property
    # def password(self):
    #     return self.password

    # @password.setter
    # def password(self, plain_text_password):
    #     self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    # def check_password_correction(self, attempted_password):
    #     return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Parameters(db.Model):
    __table_args__ = {"schema":"ti"}
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(length=20), nullable=False)
    speed = db.Column(db.Integer(), nullable=False)
    radius = db.Column(db.Integer(), nullable=False)

    # def __repr__(self):
    #     return f'Solve alg'

def check_if_parameters_are_unique(usr, spe, rad, parameters):
    for p in parameters:
        if p.user == usr and p.speed == spe and p.radius == rad:
            return False
    return True


def solve_int(solver):
    if solver == 'dijkstra':
        return 0
    elif solver == 'astar':
        return 1
    elif solver == 'bidirectional':
        return 2