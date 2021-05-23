import sqlite3
import pandas as pd
from pandas import DataFrame

test_data = {
    "people": [
        {
            "last_name": "Kougang",
            "first_name": "Michael",
            "middle_initial": "R",
            "date_of_birth": "2004-06-30",
            "dose_1_product_name_manufacturer": "pfizer",
            "dose_1_lot_number": "ER8736",
            "dose_1_date": "2021-04-24",
            "dose_1_healthcare_professional_or_clinic_site": "VMS_NA",
            "dose_2_product_name_manufacturer": "pfizer",
            "dose_2_lot_number": "EW0177",
            "dose_2_date": "2021-05-15",
            "dose_2_healthcare_professional_or_clinic_site": "JK_VMS",
            "dose_3_product_name_manufacturer": "",
            "dose_3_lot_number": "",
            "dose_3_date": "",
            "dose_3_healthcare_professional_or_clinic_site": "",
            "dose_4_product_name_manufacturer": "",
            "dose_4_lot_number": "",
            "dose_4_date": "",
            "dose_4_healthcare_professional_or_clinic_site": ""
        }
    ]
}


def create_table():
    conn = sqlite3.connect("vaccinations.db")
    cur = conn.cursor()
    try:
        cur.execute("""CREATE TABLE PEOPLE
                    (person_id INTEGER PRIMARY KEY, last_name text NOT NULL, first_name text NOT NULL, middle_initial text, 
                    date_of_birth date NOT NULL, dose_1_product_name_manufacturer text, dose_1_lot_number text, 
                    dose_1_date date, dose_1_healthcare_professional_or_clinic_site text, 
                    dose_2_product_name_manufacturer text, dose_2_lot_number text, dose_2_date date, 
                    dose_2_healthcare_professional_or_clinic_site text, dose_3_product_name_manufacturer text, 
                    dose_3_lot_number text, dose_3_date date, dose_3_healthcare_professional_or_clinic_site text, 
                    dose_4_product_name_manufacturer text, dose_4_lot_number text, dose_4_date date, 
                    dose_4_healthcare_professional_or_clinic_site text)""")
    except sqlite3.OperationalError:
        pass
    conn.commit()


def insert_person():
    conn = sqlite3.connect("vaccinations.db")
    cur = conn.cursor()
    person_data = test_data["people"][0]
    cur.execute("""
            INSERT INTO PEOPLE (last_name, first_name, middle_initial, date_of_birth, dose_1_product_name_manufacturer, dose_1_lot_number, dose_1_date, dose_1_healthcare_professional_or_clinic_site, dose_2_product_name_manufacturer, dose_2_lot_number, dose_2_date, dose_2_healthcare_professional_or_clinic_site, dose_3_product_name_manufacturer, dose_3_lot_number, dose_3_date, dose_3_healthcare_professional_or_clinic_site, dose_4_product_name_manufacturer, dose_4_lot_number, dose_4_date, dose_4_healthcare_professional_or_clinic_site) 
            VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20)
        """, (person_data["last_name"], person_data["first_name"], person_data["middle_initial"],
                person_data["date_of_birth"], person_data["dose_1_product_name_manufacturer"],
                person_data["dose_1_lot_number"], person_data["dose_1_date"],
                person_data["dose_1_healthcare_professional_or_clinic_site"],
                person_data["dose_2_product_name_manufacturer"], person_data["dose_2_lot_number"],
                person_data["dose_2_date"], person_data["dose_2_healthcare_professional_or_clinic_site"],
                person_data["dose_3_product_name_manufacturer"], person_data["dose_3_lot_number"],
                person_data["dose_3_date"], person_data["dose_3_healthcare_professional_or_clinic_site"],
                person_data["dose_4_product_name_manufacturer"], person_data["dose_4_lot_number"],
                person_data["dose_4_date"], person_data["dose_4_healthcare_professional_or_clinic_site"]))
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_person()
