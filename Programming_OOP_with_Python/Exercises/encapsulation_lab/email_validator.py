import re


class EmailValidator:
    REGEX = r'[.@]'

    def __init__(self, min_length, mails, domains):
        self.domains = domains
        self.mails = mails
        self.min_length = min_length

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        name, mail, domain = re.split(EmailValidator.REGEX, email)
        return self.__is_mail_valid(mail) and self.__is_domain_valid(domain) and self.__is_name_valid(name)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
