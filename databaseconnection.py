import mysql.connector as db
from credentials import *


def connect_to_database():
    connection = db.connect(host=host,
                        database=database,
                        user=user,
                        password=password)
    return connection


def get_table(name):
    query = "select * from " + name
    return get_query(query)


def get_query(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def delete_row(table, id_name, id):
    connection = connect_to_database()
    query = "DELETE FROM " + table + " WHERE " + id_name + "='" + id + "'"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def send_query(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def search(first_name, last_name):
    connection = connect_to_database()
    query = "SELECT FirstName, LastName, Type, BuildingName, Price \
            FROM Tenants INNER JOIN RentedUnits\
            ON Tenants.TenantID = RentedUnits.TenantID \
            INNER JOIN Units \
            ON RentedUnits.UnitID = Units.UnitID \
            INNER JOIN Buildings \
            ON Units.BuildingID = Buildings.BuildingID \
            INNER JOIN UnitTypes \
            ON Units.UnitTypeID = UnitTypes.UnitTypeID \
            WHERE FirstName='" + first_name + "' AND LastName='" + last_name + "';"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def building_keys():
    connection = connect_to_database()
    query = "SELECT BuildingID, BuildingName FROM Buildings"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def types_keys():
    connection = connect_to_database()
    query = "SELECT UnitTypeID, Type FROM UnitTypes"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def tenants_keys():
    connection = connect_to_database()
    query = "SELECT TenantID, FirstName, LastName FROM Tenants"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def units_keys():
    connection = connect_to_database()
    query = "SELECT UnitID, BuildingName, AptNum FROM Units \
            INNER JOIN Buildings on Units.BuildingID=Buildings.BuildingId"
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


