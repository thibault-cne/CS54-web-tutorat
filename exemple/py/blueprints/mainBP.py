"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

# import needed modules
from flask import Blueprint, request

# Definition of the blueprint
mainBP = Blueprint("mainBP", __name__)


# Status page
@mainBP.route('/status', methods=['GET', 'POST'])
def mainStatus() -> str:
    if request.method == 'GET':
        return "Up and Running!"
