from .database import db

class Student(db.Model):
    __tablename__ = 'student'
    s_regno=db.Column(db.Integer, primary_key=True)#, autoincrement=True)
    s_name=db.Column(db.String, nullable=False)
    s_phone=db.Column(db.Integer, nullable=False)
    s_cgpa=db.Column(db.Integer, nullable=False)
    s_email=db.Column(db.String, nullable=False)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
