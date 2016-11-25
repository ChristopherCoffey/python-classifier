class Model:

    def getModel(self):

        model = {
            'Age': {
                'total-Age': 0,
                'total': 0
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
                'total-Education': 0,
                'total': 0
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
               'total-Capital-gain': 0,
               'total': 0
            },
            'Capital-loss': {
                'total-Capital-loss': 0,
                'total': 0
            },
            'Hours-per-week': {
                'total-Hours-per-week':  0,
                'total': 0
            }
        }
        return model

    def getClassSepModel(self):

        model = {
            'Age': {
                'Age-class-sep': 0
            },
            'Workclass': {
                'Private': None,
                'Self-emp-not-inc': None,
                'Self-emp-inc': None,
                'Federal-gov': None,
                'Local-gov': None,
                'State-gov': None,
                'Without-pay': None,
                'Never-worked': None
            },
            'Education': {
                'Education-class-sep': 0
            },
            'Marital-status': {
                'Married-civ-spouse': None,
                'Divorced': None,
                'Never-married': None,
                'Separated': None,
                'Widowed': None,
                'Married-spouse-absent': None,
                'Married-AF-spouse': None
            },
            'Occupation': {
                'Tech-support': None,
                'Craft-repair': None,
                'Other-service': None,
                'Sales': None,
                'Exec-managerial': None,
                'Prof-specialty': None,
                'Handlers-cleaners': None,
                'Machine-op-inspct': None,
                'Adm-clerical': None,
                'Farming-fishing': None,
                'Transport-moving': None,
                'Priv-house-serv': None,
                'Protective-serv': None,
                'Armed-Forces': None
            },
            'Relationship': {
                'Wife': None,
                'Own-child': None,
                'Husband': None,
                'Not-in-family': None,
                'Other-relative': None,
                'Unmarried': None
            },
            'Race': {
                'White': None,
                'Asian-Pac-Islander': None,
                'Amer-Indian-Eskimo': None,
                'Other': None,
                'Black': None
            },
            'Sex': {
                'Female': None,
                'Male': None
            },
            'Capital-gain': {
                'Capital-gain-class-sep': 0
            },
            'Capital-loss': {
                'Capital-loss-class-sep': 0
            },
            'Hours-per-week': {
                'Hours-per-week-class-sep': 0
            }
        }
        return model