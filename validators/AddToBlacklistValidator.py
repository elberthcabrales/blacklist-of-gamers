from wtforms import Form, StringField, IntegerField, validators


class AddToBlacklistValidator(Form):
    email = StringField('Email',
                        [validators.DataRequired(),
                         validators.Email()])
    reason = StringField('Reason', [validators.DataRequired(),
                                    validators.AnyOf(
                                        ['foul_language',
                                         'cheating',
                                         'harassment',
                                         'other'])])
    game_id = IntegerField('Game ID', [validators.DataRequired()])
