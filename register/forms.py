# -*- coding: UTF-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from register.models import User
from mainApp.models import SiteSetting


class UserForm(forms.ModelForm):

    site_settings = SiteSetting.objects.all().first()

    if site_settings.one_day_registration > 0:
        fee_choices = [('full_price_registration', "I wish to register for the conference at the normal price of £" +
                        str(site_settings.full_price_registration)),

                       ('student_price_registration', "I wish to register for the conference at the reduced price of "
                                                      "£" + str(site_settings.student_price_registration) +
                        "(bona fide students only)"),

                       ('one_day_registration', "I wish to register for a one day pass to the conference for £" +
                        str(site_settings.one_day_registration)),

                       ('discounted_registration', "I wish to register for a discounted price and have a discount code")]

    else:
        fee_choices = [('full_price_registration', "I wish to register for the conference at the normal price of £" +
                        str(site_settings.full_price_registration)),

                       ('student_price_registration', "I wish to register for the conference at the reduced price of "
                                                      "£" + str(site_settings.student_price_registration) +
                        "(bona fide students only)"),

                       ('discounted_registration', "I wish to register for a discounted price and have a discount code")]

    salutation = forms.ChoiceField(choices=(("Mr.", "Mr."), ("Mrs.", "Mrs."), ("Ms.", "Ms."), ("Dr.", "Dr."),
                                            ("Prof.", "Prof."), ("Sir", "Sir"), ("Lady", "Lady"), ("Lord", "Lord")),
                                   required=True)
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)
    organisation = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=40, required=True)
    postcode = forms.CharField(max_length=10, required=True)
    country = forms.CharField(max_length=60, required=True)
    telephone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=60, required=True)
    registration_fee = forms.ChoiceField(choices=fee_choices, widget=forms.RadioSelect)
    discount_code_if_applicable = forms.CharField(max_length=10, required=False)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('/register/', 'Submit Registration', css_class='btn-primary'))

    class Meta:
        model = User
        fields = ('salutation', 'first_name', 'last_name', 'organisation', 'address', 'city', 'postcode', 'country',
                  'telephone', 'email', 'registration_fee', 'discount_code_if_applicable')
