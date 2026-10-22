import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DHARSHINI2007@@790427@@",
        database="healthcare_db"
    )

    return connection