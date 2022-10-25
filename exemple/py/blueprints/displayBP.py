"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

# Import needed modules
from flask import Blueprint, request, render_template

# Import personnal modules
from py.database.connectDatabase import connectDatabase

# Definition of the blueprint
displayBP = Blueprint("displayBP", __name__)


# Display page
@displayBP.route('/display', methods=['GET', 'POST'])
def displayDisplay() -> str:
    if request.method == 'GET':
        query = '''SELECT url, shortCode, visitNumber FROM urls;'''
        db, cursor = connectDatabase()
        cursor.execute(query)
        data = cursor.fetchall()
        db.close()

        return render_template('display.html', data=data)