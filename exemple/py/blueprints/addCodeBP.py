"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

# Import needed modules
from flask import Blueprint, request, render_template, redirect, flash

# Import personnal modules
from py.database.connectDatabase import connectDatabase
from py.core.generateUniqueCode import generateUniqueCode
from py.database.checkShortCode import checkShortCode

# Definition of the blueprint
addCodeBP = Blueprint("addCodeBP", __name__)

# Add page
@addCodeBP.route('/add', methods=['GET', 'POST'])
def addCodeAdd() -> str:
    if request.method == 'GET':
        query = '''SELECT url, shortCode, visitNumber FROM urls;'''
        db, cursor = connectDatabase()
        cursor.execute(query)
        data = cursor.fetchall()
        db.close()

        return render_template('add.html', data=data)
    
    elif request.method == 'POST':
        url = request.form['target_url']
        shortCode = request.form['short_code']

        if shortCode == "" or url == "":
            flash("Failed ! You must specify a url and a shortCode before submit.", "Red_flash")
            return redirect("/add")
        
        elif not checkShortCode(shortCode):
            flash("Failed ! You must enter a unique shortCode.", "Red_flash")
            return redirect("/add")

        else:
            query = '''INSERT INTO urls (url, shortCode, visitNumber) VALUES (?, ?, ?);'''
            args = (url, shortCode, 0)

            db, cursor = connectDatabase()
            cursor.execute(query, args)
            db.commit()
            db.close()

        return redirect('/add')


# Shorten page
@addCodeBP.route('/shorten', methods=['GET', 'POST'])
def addCodeShorten():
    if request.method == 'GET':
        query = '''SELECT url, shortCode, visitNumber FROM urls;'''
        db, cursor = connectDatabase()
        cursor.execute(query)
        data = cursor.fetchall()
        db.close()

        return render_template('shorten.html', data=data)
    
    elif request.method == 'POST':
        url = request.form['target_url']
        shortCode = generateUniqueCode(7)

        query = '''INSERT INTO urls (url, shortCode, visitNumber) VALUES (?, ?, ?);'''
        args = (url, shortCode, 0)

        db, cursor = connectDatabase()
        cursor.execute(query, args)
        db.commit()
        db.close()

        return redirect('/shorten')


@addCodeBP.route('/<string:route>/deleteShortCode/<string:shortCode>', methods=['GET'])
def addCodeDeleteShortCode(route: str, shortCode: str):
    if request.method == 'GET':
        query = '''DELETE FROM urls WHERE shortCode=?;'''
        arg = (shortCode, )

        db, cursor = connectDatabase()
        cursor.execute(query, arg)
        db.commit()
        db.close()

        print(route)
        return redirect(f"/{route}")