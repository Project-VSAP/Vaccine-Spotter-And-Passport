from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, DateField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration

class LoginForm(FlaskForm):
    username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])

class EditProfileForm(FlaskForm):
    username = TextField('Username'     , id='username_edit'    , validators=[DataRequired()])
    email    = TextField('Email', id='email_edit', validators=[DataRequired(), Email()])
    first_name = TextField('First Name', id='first_name_edit', validators=[DataRequired()])
    last_name = TextField('Last Name', id='last_name_edit', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', id='dob_edit', validators=[DataRequired()])
    dose_1_product_name_manufacturer = TextField('Dose 1 Product Name/Manufacturer', id='dose_1_product_name_manufacturer_edit', validators=[DataRequired()])
    dose_1_lot_number = TextField('Dose 1 Lot Number', id='dose_1_lot_number_edit', validators=[DataRequired()])
    dose_1_date = DateField('Dose 1 Date', id='dose_1_date_edit', validators=[DataRequired()])
    dose_1_healthcare_professional_or_clinic_site = TextField('Dose 1 Healthcare Professional or Clinic Site', id='dose_1_healthcare_professional_or_clinic_site_edit', validators=[DataRequired()])
    dose_2_product_name_manufacturer = TextField('Dose 2 Product Name/Manufacturer',
                                                 id='dose_2_product_name_manufacturer_edit',
                                                 validators=[DataRequired()])
    dose_2_lot_number = TextField('Dose 2 Lot Number', id='dose_2_lot_number_edit', validators=[DataRequired()])
    dose_2_date = DateField('Dose 2 Date', id='dose_2_date_edit', validators=[DataRequired()])
    dose_2_healthcare_professional_or_clinic_site = TextField('Dose 2 Healthcare Professional or Clinic Site',
                                                              id='dose_2_healthcare_professional_or_clinic_site_edit',
                                                              validators=[DataRequired()])
    dose_3_product_name_manufacturer = TextField('Dose 3 Product Name/Manufacturer',
                                                 id='dose_3_product_name_manufacturer_edit',
                                                 validators=[DataRequired()])
    dose_3_lot_number = TextField('Dose 3 Lot Number', id='dose_3_lot_number_edit', validators=[DataRequired()])
    dose_3_date = DateField('Dose 3 Date', id='dose_3_date_edit', validators=[DataRequired()])
    dose_3_healthcare_professional_or_clinic_site = TextField('Dose 3 Healthcare Professional or Clinic Site',
                                                              id='dose_3_healthcare_professional_or_clinic_site_edit',
                                                              validators=[DataRequired()])
    dose_4_product_name_manufacturer = TextField('Dose 4 Product Name/Manufacturer',
                                                 id='dose_4_product_name_manufacturer_edit',
                                                 validators=[DataRequired()])
    dose_4_lot_number = TextField('Dose 4 Lot Number', id='dose_4_lot_number_edit', validators=[DataRequired()])
    dose_4_date = DateField('Dose 4 Date', id='dose_4_date_edit', validators=[DataRequired()])
    dose_4_healthcare_professional_or_clinic_site = TextField('Dose 4 Healthcare Professional or Clinic Site',
                                                              id='dose_4_healthcare_professional_or_clinic_site_edit',
                                                              validators=[DataRequired()])
