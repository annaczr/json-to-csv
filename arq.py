import pandas as pd


try:
    df = pd.read_json(
        r'C:\Users\alunotemp\Documents\teste\json-to-csv\arq.json', orient='records')
    df.to_csv(r'C:\Users\alunotemp\Documents\teste\json-to-csv\arq.csv',
              index=False, header=True)

    print('A conversão feita com sucesso')

except:
    print('Ocorreu um erro')