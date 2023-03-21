import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter =',')
        header =next(reader)
        print = header
        data = []
        for row in reader:
            iterable = zip(header, row) #va a unir los dos
           # print(list(iterable)) # da formato de tuplas
            country_dict = {key : value for key, value in iterable} # esto lo muestra como un diccionario
            data.append(country_dict)
        return data


if __name__=='__main__':
   data =  read_csv('./data.csv')

#print(data[0])
