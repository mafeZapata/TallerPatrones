from GraficarDatos import CovidDataPlotter, GraficarDatos


class Graficar(GraficarDatos):
    
    def __init__(self, file_path):
        super().__init__(file_path)
        
    def graficar(self, country):
        self.plot_cases_by_country(country)
