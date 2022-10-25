"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

def buildDeleteUrl(completeUrl: str) -> str:
    newUrl = completeUrl.replace("http://localhost:5454/", "")

    return newUrl + "/deleteShortCode"