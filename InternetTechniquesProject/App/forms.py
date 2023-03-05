from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from App.models import PageUser

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    # email_address = StringField(label='Email', validators=[Email(), DataRequired()])
    email_address = StringField(label='Email', validators=[Email(allow_empty_local=True), DataRequired()])
    password = PasswordField(label='Hasło', validators=[Length(min=7), DataRequired()])
    password_confirm = PasswordField(label='Powtórz hasło', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Stwórz konto')

    def validate_username(self, username_to_check):
        user = PageUser.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Użytkownik o takiej nazwie już istnieje! Spróbuj innej!')

    def validate_email(self, email_address_to_check):
        email_address = PageUser.query.filter_by(email=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Użytkownik o takim adresie email już istnieje! Spróbuj innego adresu!')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Hasło', validators=[DataRequired()])
    submit = SubmitField(label='Zaloguj się')

class ParamForm(FlaskForm):
    speed = IntegerField(label='Szybkość kulki', validators=[NumberRange(min=1, max=10), DataRequired()])
    radius = IntegerField(label='Promień kulki', validators=[NumberRange(min=1, max=30), DataRequired()])
    submit = SubmitField(label='Zapisz')