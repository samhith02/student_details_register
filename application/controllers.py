import os
from flask import Flask
from flask import render_template
from flask import request, session
from flask import url_for,redirect
from flask_api import status
from flask import current_app as app
from application.models import *


def getlistfromdb():
    studentlist = []
    students = Student.query.all()
    if students:
        for student in students:
            studentdict = {}
            studentdict['name'] = student.s_name
            studentdict['regno'] = student.s_regno
            studentlist.append(studentdict)
            print("Student Dict = ", studentdict)
        print("StudentList = ", studentlist)
    else:
        print("No lists available!!")
    return studentlist



@app.route("/")
def index():
    return render_template('index.html', studentlist = getlistfromdb())

@app.route("/student/create", methods=['POST'])
def handle_create_student():
    name = request.form['name']
    regno = request.form['regno']
    phone = request.form['phone']
    cgpa = request.form['cgpa']
    email = request.form['email']
    
    exist = False
    
    print("name = ", name, " regno = ", regno, " phone = ", phone, "cgpa = ", cgpa, "email = ", email)
    student = Student.query.filter_by(s_regno=regno).all()
    
    if student:
        exist = True
    
    if exist:
        content = {'Invalid Input': 'Student Record already exists'}
        return content, status.HTTP_400_BAD_REQUEST
    else:
        s = Student(s_regno = regno, s_name = name, s_phone = phone, s_cgpa = cgpa, s_email = email)
        db.session.add(s)
        db.session.commit()
        return render_template('index.html', studentlist = getlistfromdb())

@app.route("/add_student", methods=['GET'])
def add_student():
    if request.method == 'GET':
            return render_template('add_student.html')


@app.route("/student/delete", methods=['POST'])
def handle_delete_student():
    regno = request.form['regno']
    exist = False

    print(" regno = ", regno)

    student = Student.query.filter_by(s_regno=regno).first()

    if student:
        exist = True

    if exist == False:
        content = {'Invalid Input': 'Student Record does not exist'}
        return content, status.HTTP_400_BAD_REQUEST
    else:
        db.session.delete(student)
        db.session.commit()
        return render_template('index.html', studentlist = getlistfromdb())




@app.route("/delete_student", methods=['GET'])
def delete_student():
    if request.method == 'GET':
            return render_template('delete_student.html')



@app.route("/student/<int:regno>/show", methods=['GET'])
def handle_show_student(regno):
    print("REGNO : ", regno)
    if request.method == 'GET':
        st = {}
        s = Student.query.filter_by(s_regno=regno).first()
        st['name'] = s.s_name
        st['regno'] = s.s_regno
        st['phone'] = s.s_phone
        st['cgpa'] = s.s_cgpa
        st['email'] = s.s_email
        print("student object to be shown : ", st)
        return render_template('student_details.html', student=st)

