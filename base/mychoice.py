# choices for gender
gen_choice = (
        ('M', 'M'),
        ('FM', 'FM')
    )


# choices for department
dep_choice = (
        ('Accounting/Finance', 'Accounting/Finance'),
        ('Administration', 'Administration'),
        ('Agriculture', 'Agriculture'),
        ('Art / Media', 'Art / Media'),
        ('Automotive service', 'Automotive service'),
        ('Aviation/Airport', 'Aviation/Airport'),
        ('Banking', 'Banking'),
        ('Engineering', 'Engineering'),
        ('Hotels, restaurants, service', 'Hotels, restaurants, service'),
        ('Information technology', 'Information technology'),
        ('Insurance', 'Insurance'),
        ('Marketing, Advertising, PR', 'Marketing, Advertising, PR'),
        ('Medical', 'Medical'),
        ('Quality control, environment, safety', 'Quality control, environment, safety'),
        ('Security', 'Security'),
        ('Tourism/entertainment industry', 'Tourism/entertainment industry'),
        ('Training courses/Educational programmes', 'Training courses/Educational programmes'),
        ('Beauty/Aesthetic Medicine', 'Beauty/Aesthetic Medicine'),
        ('Top management', 'Top management')
    )


# choices for description
desc_choices = [
        ('Shift', (
            ('First', 'First'),
            ('Second', 'Second'),
            ('Third', 'Third'),
            ('Fixed', 'Fixed'),
            ('Rotating', 'Rotating'),
            ('Split', 'Split'),
            ('On-call', 'On-call'),
        )
         ),
        # ('Job level', (
        #     ('Intern', 'Intern'),
        #     ('Junior', 'Junior'),
        #     ('Middle', 'Middle'),
        #     ('Senior', 'Senior'),
        #     ('Lead', 'Lead'),
        # )
        #  ),
        ('Employment form', (
            ("Full-time", "Full-time"),
            ("Part-time", "Part-time"),

        )
         ),
        ('Experience', (
            ("Without experience", "Without experience"),
            ("Less than 1 year", "Less than 1 year"),
            ("1 - 2 years", "1 - 2 years"),
            ("2 - 3 years", "2 - 3 years"),
            ("3 - 5 years", "3 - 5 years"),
            ("5 - 7 years", "5 - 7 years"),
            ("7 - 10 years", "7 - 10 years"),
            ("10+ years", "10+ years"),
         )
        ),
        ('English language level', (
            ("Intermediate/B1", "Intermediate/B1"),
            ("Upper Intermediate/B2", "Upper Intermediate/B2"),
            ("Pre-advanced/C1", "Pre-advanced/C1"),
            ("Advanced/C2", "Advanced/C2"),
        )
        )

    ]