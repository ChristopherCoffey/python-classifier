class Model:

    def getModel(self):

        model = {
            'Age': {
                'totalAge': 0,
                'count': 0
            },
            'Workclass': {
                'Private': 0,
                'Self-emp-not-inc': 0,
                'Self-emp-inc': 0,
                'Federal-gov': 0,
                'Local-gov': 0,
                'State-gov': 0,
                'Without-pay': 0,
                'Never-worked': 0,
                'total': 0
            },
            'Education': {
                'education-number': 0,
                'count': 0
            },
            'Marital-status': {
                'Married-civ-spouse': 0,
                'Divorced': 0,
                'Never-married': 0,
                'Separated': 0,
                'Widowed': 0,
                'Married-spouse-absent': 0,
                'Married-AF-spouse': 0,
                'total': 0
            },
            'Occupation': {
               'Tech-support': 0,
               'Craft-repair': 0,
               'Other-service': 0,
               'Sales': 0,
               'Exec-managerial': 0,
               'Prof-specialty': 0,
               'Handlers-cleaners': 0,
               'Machine-op-inspct': 0,
               'Adm-clerical': 0,
               'Farming-fishing': 0,
               'Transport-moving': 0,
               'Priv-house-serv': 0,
               'Protective-serv': 0,
               'Armed-Forces': 0,
               'total': 0
            },
            'Relationship': {
                'Wife': 0,
                'Own-child': 0,
                'Husband': 0,
                'Not-in-family': 0,
                'Other-relative': 0,
                'Unmarried': 0,
                'total': 0
            },
            'Race': {
                'White': 0,
                'Asian-Pac-Islander': 0,
                'Amer-Indian-Eskimo': 0,
                'Other': 0,
                'Black': 0,
                'total': 0
            },
            'Sex': {
                'Female': 0,
                 'Male': 0,
                 'total': 0
            },
            'Capital-gain': {
               'total-capital-gain': 0,
               'count': 0
            },
            'Capital-loss': {
                'total-capital-loss': 0,
                'count': 0
            },
            'Hours-per-week': {
                'total-hours-per-week':  0,
                'count': 0
            }
        }
        return model