from django.core.validators import RegexValidator


class PhoneNumberValidator(RegexValidator):
    regex = r'^09\d{9}$'
    message = 'باید حتما ۱۱ رقم باشد و با ۰۹ شروع شود'
    code = 'invalid_phone_number'


class PostalCodeValidator(RegexValidator):
    regex = r'^\d{10}$'
    message = 'کدپستی باید ۱۰ رقم باشد و فقط شامل عدد'
    code = 'invalid_postal_code'


phone_number_validator = PhoneNumberValidator()
postal_code_validator = PostalCodeValidator()
