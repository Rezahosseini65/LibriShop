import re

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class PhoneNumberValidator(RegexValidator):
    regex = r'^09\d{9}$'
    message = 'باید حتما ۱۱ رقم باشد و با ۰۹ شروع شود'
    code = 'invalid_phone_number'


class PostalCodeValidator(RegexValidator):
    regex = r'^\d{10}$'
    message = 'کدپستی باید ۱۰ رقم باشد و فقط شامل عدد'
    code = 'invalid_postal_code'


def number_validator(password):
    regex = re.compile('[0-9]')
    if regex.search(password) is None:
        raise ValidationError(
            _("password must include number"),
            code="password_must_include_number"
        )


def letter_validator(password):
    regex = re.compile('[a-zA-Z]')
    if regex.search(password) is None:
        raise ValidationError(
            _("password must include letter"),
            code="password_must_include_letter"
        )


phone_number_validator = PhoneNumberValidator()
postal_code_validator = PostalCodeValidator()
