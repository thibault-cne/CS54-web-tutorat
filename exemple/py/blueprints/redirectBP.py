"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

# import needed modules
from flask import Blueprint, redirect

# Import personnal modules
from py.database.connectDatabase import connectDatabase

# Definition of the blueprint
redirectBP = Blueprint("redirectBP", __name__)


@redirectBP.route('/r/<string:shortCode>')
def redirectR(shortCode: str):
    query = '''SELECT url, visitNumber FROM urls WHERE shortCode=?;'''
    arg = (shortCode, )

    db, cursor = connectDatabase()

    cursor.execute(query, arg)
    data = cursor.fetchall()[0]
    
    updateQuery = '''UPDATE urls SET visitNumber=? WHERE shortCode=?;'''
    args = (data[1]+1, shortCode)

    cursor.execute(updateQuery, args)
    db.commit()
    db.close()

    return redirect(data[0])