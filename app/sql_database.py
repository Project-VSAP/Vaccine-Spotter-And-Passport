import psycopg2
from configparser import ConfigParser


def insert_user_data(_conn, person_data):
    with _conn.cursor() as cursor:
        cursor.execute("""INSERT INTO people(id, last_name, first_name, middle_initial, date_of_birth, dose_1_product_name_manufacturer, dose_1_lot_number, dose_1_date, dose_1_healthcare_professional_or_clinic_site, dose_2_product_name_manufacturer, dose_2_lot_number, dose_2_date, dose_2_healthcare_professional_or_clinic_site)
        VALUES ()""")


if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database="people",
        user="postgres",
        password="@2Maroua")
    conn.autocommit = False
    insert_user_data(conn)
