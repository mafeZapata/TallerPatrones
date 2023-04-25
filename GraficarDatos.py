
import datetime
import CovidDataService
import matplotlib.pyplot as plt

class GraficarDatos(CovidDataService):
    
    def __init__(self, file_path):
        super().__init__(file_path)
        
    def plot_cases_by_country(self, country):
        cases = self.get_cases_by_country(country)
        dates = [datetime.strptime(case['date'], '%m/%d/%y') for case in cases]
        case_counts = [int(case['cases']) for case in cases]
        
        plt.plot(dates, case_counts)
        plt.title(f"Casos confirmados de COVID-19 en {country}")
        plt.xlabel("Fecha")
        plt.ylabel("Número de casos")
        plt.show()
