import mod
import read_csv
import charts




def run():
    data = read_csv.read_csv('./data.csv')
    country = input('type country => ')
    result = mod.population_by_country(data, country)

    if len(result) > 0:
        country =result[0]
        labels , values = mod.get_population(country)
        charts.generate_bar_chart(country, labels, values)


    #print(mod.a) #se pueden llamar variables tambien

    
    
    #print(result)

if __name__=='__main__': #esto se llama entry point
    run()