class DVD:
    def __init__(self, name, id_, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id_
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id_, name, date, age_restriction):
        month, year = cls.return_format_date(date)
        return cls(name, id_, year, month, age_restriction)

    @staticmethod
    def return_format_date(date):
        mapper = {
            '01': 'January',
            '02': 'February',
            '03': 'March',
            '04': 'April',
            '05': 'May',
            '06': 'June',
            '07': 'July',
            '08': 'August',
            '09': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December',
        }
        new_date = date.split('.')
        month, year = new_date[1:]
        month = mapper[month]
        year = int(year)
        return month, year
