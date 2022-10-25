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


def checkShortCode(shortCode: str) -> bool:
    query = '''SELECT * FROM urls WHERE shortCode=?;'''
    arg = (shortCode, )

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    result = cursor.fetchall()
    db.close()

    return (len(result) == 0)