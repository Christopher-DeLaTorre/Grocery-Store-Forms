from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, GroceryItem, ItemCategory

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    title = StringField('Grocery Title', validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Submit')
    # - title - StringField
    # - address - StringField
    # - submit button
    pass

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    name = StringField('Item Name', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Item Price', validators=[DataRequired()])
    category = SelectField('Item Category',  choices=ItemCategory.choices())
    photo_url = StringField('Item Photo', validators=[DataRequired(), Length(min=3, max=150)])
    store = QuerySelectField('Stores', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
