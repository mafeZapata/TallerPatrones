import csv
from datetime import datetime

class CovidData:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append(row)
                
    
    def get_country_data(self, country):
        cases = []
        for row in self.data:
            if row['Country'] == country:
                cases.append({
                    'date': row['Start_date'],
                    'cases': row['#Cases']
                })
        return cases
    
    def get_countries_historic_data(self, country, start_date, end_date):
        cases = []
        for row in self.data:
            if row['Country'] == country:
                row_date = datetime.strptime(row['Start_date'], '%m/%d/%y')
                if start_date <= row_date <= end_date:
                    cases.append(int(row['#Cases']))
        return sum(cases)
    
