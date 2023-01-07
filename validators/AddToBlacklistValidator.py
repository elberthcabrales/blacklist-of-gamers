from flask import request
from wtforms import Form, StringField, IntegerField, validators


class AddToBlacklistValidator(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    reason = StringField('Reason', [validators.DataRequired()])
    game_id = IntegerField('Game ID', [validators.DataRequired()])
