import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

from Graficar import Graficar

class CSVPlotter(Graficar):
    #el parametro file_path hace referencia a el cvs que se le va a ingresar, mas en especifico la ruta del mismo
    def graph_cases_by_country(self, file_path):
        df = pd.read_csv(file_path)
        
        country = input("Ingrese el país que desea graficar: ")
        start_date = input("Ingrese la fecha de inicio (MM/DD/YY): ")
        end_date = input("Ingrese la fecha de fin (MM/DD/YY): ")
        
        cases = self.get_cases_by_country_in_range_from_df(df, country, start_date, end_date)
        dates = [datetime.strptime(case['date'], '%m/%d/%y') for case in cases]
        case_counts = [int(case['cases']) for case in cases]
        
        plt.plot(dates, case_counts)
        plt.title(f"Casos confirmados de COVID-19 en {country}")
        plt.xlabel("Fecha")
        plt.ylabel("Número de casos")
        plt.show()
