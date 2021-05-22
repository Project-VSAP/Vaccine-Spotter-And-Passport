from flask import Flask, request, render_template, url_for, redirect
import segno
import json
from urllib.parse import urlencode, parse_qs
import ast
import sql_database

app = Flask(__name__)

vaccination_data = {
    "people": [
        {
            "last_name": "Kougang",
            "first_name": "Michael",
            "middle_initial": "R",
            "date_of_birth": "06-30-2004",
            "dose_1": {
                "product_name-manufacturer": "pfizer",
                "lot_number": "ER8736",
                "date": "04-24-21",
                "healthcare_professional_or_clinic_site": "VMS_NA"
            },
            "dose_2": {
                "product_name-manufacturer": "pfizer",
                "lot_number": "EW0177",
                "date": "05-15-21",
                "healthcare_professional_or_clinic_site": "JK_VMS"
            }
        }
    ]
}


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/qr_code')
def qr_code():
    create_qr()
    return render_template("qr_code.html")


# create qr code
def create_qr():
    person_data = vaccination_data["people"][0]
    url = "http://localhost:5000/vaccination_data/" + urlencode(person_data)
    qr = segno.make_qr(url)
    qr.save("static/qr.png", scale=5)


@app.route('/vaccination_data/<person_data>')
def show_qr_data(person_data):
    vaccination_data_qr = dict(parse_qs(person_data))
    vaccination_data_qr_dose_1 = ast.literal_eval(vaccination_data_qr["dose_1"][0])
    vaccination_data_qr_dose_2 = ast.literal_eval(vaccination_data_qr["dose_2"][0])
    return render_template("vaccination_data.html",
                           last_name=vaccination_data_qr["last_name"][0],
                           first_name=vaccination_data_qr["first_name"][0],
                           middle_initial=vaccination_data_qr["middle_initial"][0],
                           date_of_birth=vaccination_data_qr["date_of_birth"][0],
                           dose_1_product_name_manufacturer=vaccination_data_qr_dose_1["product_name-manufacturer"],
                           dose_1_lot_number=vaccination_data_qr_dose_1["lot_number"],
                           dose_1_date=vaccination_data_qr_dose_1["date"],
                           dose_1_healthcare_professional_or_clinic_site=vaccination_data_qr_dose_1["healthcare_professional_or_clinic_site"],
                           dose_2_product_name_manufacturer=vaccination_data_qr_dose_2["product_name-manufacturer"],
                           dose_2_lot_number=vaccination_data_qr_dose_2["lot_number"],
                           dose_2_date=vaccination_data_qr_dose_2["date"],
                           dose_2_healthcare_professional_or_clinic_site=vaccination_data_qr_dose_2["healthcare_professional_or_clinic_site"])


if __name__ == '__main__':
    app.run(debug=True)
