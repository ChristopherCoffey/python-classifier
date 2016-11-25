import urllib3
from model import Model

def process_data(flag):

    if flag == 1:
        f = open('Adult_Data.txt')
        data = f.read().split('\n')
    else:
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
    classSepVal = ob.getClassSepModel()

    for i in range(len(data) - 2):
        if data[i][14] == "<=50K":
            lessSalary['Age']['total-Age'] = lessSalary['Age']['total-Age'] + int(data[i][0]) # data[i][0] gives the first row
            lessSalary['Age']['total'] += 1
            if data[i][1] != '?':
                lessSalary['Workclass'][data[i][1]] += 1
                lessSalary['Workclass']['total'] += 1
            if data[i][4] != '?':
                lessSalary['Education']['total-Education'] += int(data[i][4])
                lessSalary['Education']['total'] += 1
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
                lessSalary['Capital-gain']['total-Capital-gain'] += int(data[i][10])
                lessSalary['Capital-gain']['total'] += 1
            if data[i][11] != '?':
                lessSalary['Capital-loss']['total-Capital-loss'] += int(data[i][11])
                lessSalary['Capital-loss']['total'] += 1
            if data[i][12] != '?':
                lessSalary['Hours-per-week']['total-Hours-per-week'] += int(data[i][12])
                lessSalary['Hours-per-week']['total'] += 1
        else:
            moreSalary['Age']['total-Age'] += int(data[i][0])
            moreSalary['Age']['total'] += 1
            if data[i][1] != '?':
                moreSalary['Workclass'][data[i][1]] += 1
                moreSalary['Workclass']['total'] += 1
            if data[i][4] != '?':
                moreSalary['Education']['total-Education'] += int(data[i][4])
                moreSalary['Education']['total'] += 1
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
                moreSalary['Capital-gain']['total-Capital-gain'] += int(data[i][10])
                moreSalary['Capital-gain']['total'] += 1
            if data[i][11] != '?':
                moreSalary['Capital-loss']['total-Capital-loss'] += int(data[i][11])
                moreSalary['Capital-loss']['total'] += 1
            if data[i][12] != '?':
                moreSalary['Hours-per-week']['total-Hours-per-week'] += int(data[i][12])
                moreSalary['Hours-per-week']['total'] += 1

    lessSalary = calculateAvg(lessSalary)
    moreSalary = calculateAvg(moreSalary)
    print("After average, less = ", lessSalary, '\n\n', 'more =', moreSalary)
    classSepVal = calculateClassSep(lessSalary, moreSalary, classSepVal)

    print('Class seperation value is', classSepVal)

def calculateAvg(d):
    
    for k, v in d.items():
        for k1, v1 in d[k].items():
            if k1 != 'total':
                d[k][k1] = d[k][k1] / d[k]['total']
    return d

def calculateClassSep(lSal, mSal, cls):

    for k, v in lSal.items():
        if k == 'Age' or k == 'Education' or \
                        k == 'Capital-gain' or \
                        k == 'Capital-loss' or \
                        k == 'Hours-per-week':
            cls[k][k + '-class-sep'] = (lSal[k]['total-' + k] + mSal[k]['total-' + k]) / 2.0

    return cls

process_data(1)  # 1 will fetch data locally, anything else will fetch it from the url
