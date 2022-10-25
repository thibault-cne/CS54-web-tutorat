"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

# Import needed modules
import string
import random

# Import personnal modules
from py.database.connectDatabase import connectDatabase
from py.database.checkShortCode import checkShortCode


def generateUniqueCode(codeLength: int) -> str:
    alphabet = string.ascii_letters + string.digits 
    shortCode =''.join(random.choice(alphabet)for i in range(codeLength))

    query = '''SELECT * FROM urls WHERE shortCode=?;'''
    arg = (shortCode, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    result = cursor.fetchall()
    db.close()

    if checkShortCode(shortCode):
        return shortCode
    else:
        return generateUniqueCode(codeLength)
