"""
    Author : Chenevière Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

# Import personnal modules
from py.database.connectDatabase import connectDatabase


def createDB():
    """
        Function to create the database with 2 first exemples

        Arguments :
            - None
        
        Returns :
            - None
    """

    query = '''
    DROP TABLE IF EXISTS urls;
    
    CREATE TABLE urls 
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        shortCode TEXT UNIQUE,
        visitNumber INTEGER
    );
    
    INSERT INTO urls (url, shortCode, visitNumber) VALUES ('https://telecomnancy.univ-lorraine.fr/','tn', 42);
    INSERT INTO urls (url, shortCode, visitNumber) VALUES ('https://gitlab.telecomnancy.univ-lorraine.fr/','gitlab', 666);'''

    db, cursor = connectDatabase()

    cursor.executescript(query)
    db.commit()
    db.close()


if __name__ == "__main__":
    createDB()