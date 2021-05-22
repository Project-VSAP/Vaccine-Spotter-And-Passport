import psycopg2
from config import config


def insert_person(last_name, first_name, middle_initial, date_of_birth, dose_1_product_name_manufacturer,
                  dose_1_lot_number, dose_1_date, dose_1_healthcare_professional_or_clinic_site,
                  dose_2_product_name_manufacturer, dose_2_lot_number, dose_2_date,
                  dose_2_healthcare_professional_or_clinic_site, dose_3_product_name_manufacturer,
                  dose_3_lot_number, dose_3_date, dose_3_healthcare_professional_or_clinic_site,
                  dose_4_product_name_manufacturer, dose_4_lot_number, dose_4_date,
                  dose_4_healthcare_professional_or_clinic_site):
    """ insert a new person into the people table """
    sql = """INSERT INTO people(last_name, first_name, middle_initial, date_of_birth, dose_1_product_name_manufacturer,
                  dose_1_lot_number, dose_1_date, dose_1_healthcare_professional_or_clinic_site, 
                  dose_2_product_name_manufacturer, dose_2_lot_number, dose_2_date, 
                  dose_2_healthcare_professional_or_clinic_site, dose_3_product_name_manufacturer,
                  dose_3_lot_number, dose_3_date, dose_3_healthcare_professional_or_clinic_site, 
                  dose_4_product_name_manufacturer, dose_4_lot_number, dose_4_date, 
                  dose_4_healthcare_professional_or_clinic_site)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;"""
    conn = None
    person_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (last_name, first_name, middle_initial, date_of_birth, dose_1_product_name_manufacturer,
                          dose_1_lot_number, dose_1_date, dose_1_healthcare_professional_or_clinic_site,
                          dose_2_product_name_manufacturer, dose_2_lot_number, dose_2_date,
                          dose_2_healthcare_professional_or_clinic_site, dose_3_product_name_manufacturer,
                          dose_3_lot_number, dose_3_date, dose_3_healthcare_professional_or_clinic_site,
                          dose_4_product_name_manufacturer, dose_4_lot_number, dose_4_date,
                          dose_4_healthcare_professional_or_clinic_site,))
        # get the generated id back
        person_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
    finally:
        if conn is not None:
            conn.close()

    return person_id


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


if __name__ == "__main__":
    person_data = test_data["people"][0]
    insert_person(person_data["last_name"], person_data["first_name"], person_data["middle_initial"],
                  person_data["date_of_birth"], person_data["dose_1_product_name_manufacturer"],
                  person_data["dose_1_lot_number"], person_data["dose_1_date"],
                  person_data["dose_1_healthcare_professional_or_clinic_site"],
                  person_data["dose_2_product_name_manufacturer"], person_data["dose_2_lot_number"],
                  person_data["dose_2_date"], person_data["dose_2_healthcare_professional_or_clinic_site"],
                  person_data["dose_3_product_name_manufacturer"], person_data["dose_3_lot_number"],
                  person_data["dose_3_date"], person_data["dose_3_healthcare_professional_or_clinic_site"],
                  person_data["dose_4_product_name_manufacturer"], person_data["dose_4_lot_number"],
                  person_data["dose_4_date"], person_data["dose_4_healthcare_professional_or_clinic_site"])
