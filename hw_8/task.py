"""
Опишите любую абстракцию (желательно юридическую, но вы можете выбрать любую другую)
с помощью инструментов ООП (например, Истец-Ответчик, Право- Обязательство, 
Срок, Судья и др.).
Придумайте атрибуты и методы для абстракции. Если ничего не приходит на ум,
просто дополните абстракцию (класс) из домашнего задания No 7 любыми атрибутами 
и методами на ваше усмотрение.
"""
import datetime

class LegalContract:
    def __init__(self, parties, date_signed, duration, terms):
        self.parties = parties
        self.date_signed = date_signed
        self.duration = duration
        self.terms = terms

    def is_valid(self, current_date):
        return current_date >= self.date_signed and current_date <= self.date_signed + self.duration

    def get_contract_parties(self):
        return self.parties

    def get_contract_terms(self):
        return self.terms

    def update_contract_terms(self, new_terms):
        self.terms = new_terms

    def extend_contract_duration(self, extension):
        self.duration += extension

# Использования
parties = ["Компания А", "Компания Б"]
date_signed = datetime.date(2024, 4, 10)
duration = datetime.timedelta(days=365)
terms = {"payment": "1000$", "deliverables": "10 units"}

contract = LegalContract(parties, date_signed, duration, terms)

print(contract.is_valid(datetime.date(2025, 4, 10)))  # Проверяем, действителен ли договор на 2025-04-10
print(contract.get_contract_parties())  # Получаем список сторон договора
print(contract.get_contract_terms())  # Получаем условия договора

new_terms = {"payment": "1200$", "deliverables": "15 units"}
contract.update_contract_terms(new_terms)  # Обновляем условия договора
print(contract.get_contract_terms())

contract.extend_contract_duration(datetime.timedelta(days=30))  # Продляем договор на 30 дней
print(contract.duration.days)
