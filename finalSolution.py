import urllib3
from model import Model

def process_data():
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    print("Reading data from url, this might take a while, please be patient....")
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    data = response.data.decode('utf-8').split('\n')
    response.release_conn()
    print("Data fetched from url!")
    for i in range(len(data)):
        data[i] = data[i].strip().split(', ')

    train_classifier(data)

def train_classifier(data):

    ob = Model()
    lessSalary = ob.getModel()
    moreSalary = ob.getModel()
    classSepVal = ob.getModel()

    for i in range(len(data) - 2):
        if data[i][14] == "<=50K":
            lessSalary['Age' ]['totalAge'] = lessSalary['Age']['totalAge'] + int(data[i][0]) # data[i][0] gives the first row
            lessSalary['Age']['count'] += 1
            if data[i][1] != '?':
                lessSalary['Workclass'][data[i][1]] += 1
                lessSalary['Workclass']['total'] += 1
            if data[i][4] != '?':
                lessSalary['Education']['education-number'] += int(data[i][4])
                lessSalary['Education']['count'] += 1
            if data[i][5] != '?':
                lessSalary['Marital-status'][data[i][5]] += 1
                lessSalary['Marital-status']['total'] += 1
            if data[i][6] != '?':
                lessSalary['Occupation'][data[i][6]] += 1
                lessSalary['Occupation']['total'] += 1
            if data[i][7] != '?':
                lessSalary['Relationship'][data[i][7]] += 1
                lessSalary['Relationship']['total'] += 1
            if data[i][8] != '?':
                lessSalary['Race'][data[i][8]] += 1
                lessSalary['Race']['total'] += 1
            if data[i][9] != '?':
                lessSalary['Sex'][data[i][9]] += 1
                lessSalary['Sex']['total'] += 1
            if data[i][10] != '?':
                lessSalary['Capital-gain']['total-capital-gain'] += int(data[i][10])
                lessSalary['Capital-gain']['count'] += 1
            if data[i][11] != '?':
                lessSalary['Capital-loss']['total-capital-loss'] += int(data[i][11])
                lessSalary['Capital-loss']['count'] += 1
            if data[i][12] != '?':
                lessSalary['Hours-per-week']['total-hours-per-week'] += int(data[i][12])
                lessSalary['Hours-per-week']['count'] += 1
        else:
            moreSalary['Age']['totalAge'] += int(data[i][0])
            moreSalary['Age']['count'] += 1
            if data[i][1] != '?':
                moreSalary['Workclass'][data[i][1]] += 1
                moreSalary['Workclass']['total'] += 1
            if data[i][4] != '?':
                moreSalary['Education']['education-number'] += int(data[i][4])
                moreSalary['Education']['count'] += 1
            if data[i][5] != '?':
                moreSalary['Marital-status'][data[i][5]] += 1
                moreSalary['Marital-status']['total'] += 1
            if data[i][6] != '?':
                moreSalary['Occupation'][data[i][6]] += 1
                moreSalary['Occupation']['total'] += 1
            if data[i][7] != '?':
                moreSalary['Relationship'][data[i][7]] += 1
                moreSalary['Relationship']['total'] += 1
            if data[i][8] != '?':
                moreSalary['Race'][data[i][8]] += 1
                moreSalary['Race']['total'] += 1
            if data[i][9] != '?':
                moreSalary['Sex'][data[i][9]] += 1
                moreSalary['Sex']['total'] += 1
            if data[i][10] != '?':
                moreSalary['Capital-gain']['total-capital-gain'] += int(data[i][10])
                moreSalary['Capital-gain']['count'] += 1
            if data[i][11] != '?':
                moreSalary['Capital-loss']['total-capital-loss'] += int(data[i][11])
                moreSalary['Capital-loss']['count'] += 1
            if data[i][12] != '?':
                moreSalary['Hours-per-week']['total-hours-per-week'] += int(data[i][12])
                moreSalary['Hours-per-week']['count'] += 1



                    # for k, v in lessSalary['Workclass'].items():
        #     if (k != 'total'):
        #         lessSalary['Workclass'][k] /= lessSalary['Workclass']['total']


    print("Average age of the guy that earns more than 50k", moreSalary['Age']['totalAge']/moreSalary['Age']['count'])
    print("Average age of the guy that earns less than 50k", lessSalary['Age']['totalAge']/lessSalary['Age']['count'])
    print("Workclass fraction for people earning less than 50k", lessSalary['Workclass'])
    print("Workclass fraction for people earning more than 50k", moreSalary['Workclass'])
    print('less Salary = ', lessSalary)
    print('more Salary = ', lessSalary)

process_data()
