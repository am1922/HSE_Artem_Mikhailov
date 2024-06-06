import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

class ParserCBRF:
    def __init__(self):
        self.url = 'https://www.cbr.ru/currency_base/daily/'
        self.data = []

    def start(self, serialize_filename=None, deserialize_filename=None):
        if deserialize_filename:
            self.__deserialize(deserialize_filename)
        else:
            self.__fetch_data()
            self.__parse_data()
            if serialize_filename:
                self.__serialize(serialize_filename)
            else:
                self.__save_data()

    def __fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.page_content = response.content
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

    def __parse_data(self):
        soup = BeautifulSoup(self.page_content, 'html.parser')
        table = soup.find('table', {'class': 'data'})
        if not table:
            raise Exception("Failed to find data table")
        
        rows = table.find_all('tr')[1:]  # Skip header row
        date_str = soup.find('div', {'class': 'datepicker-filter'}).find('input').get('value')
        date = datetime.strptime(date_str, '%d.%m.%Y').date()
        
        for row in rows:
            cols = row.find_all('td')
            currency_info = {
                'date': date.strftime('%Y-%m-%d'),
                'num_code': cols[0].text.strip(),
                'char_code': cols[1].text.strip(),
                'unit': int(cols[2].text.strip()),
                'currency': cols[3].text.strip(),
                'rate': float(cols[4].text.strip().replace(',', '.'))
            }
            self.data.append(currency_info)

    def __save_data(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, f'cbrf_currency_{datetime.now().date()}.json')
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def __serialize(self, filename):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def __deserialize(self, filename):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

if __name__ == '__main__':
    parser = ParserCBRF()
    parser.start(serialize_filename='currency_data.json')

    # parser.start(deserialize_filename='currency_data.json')
