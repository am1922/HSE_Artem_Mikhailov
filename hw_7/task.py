"""
Реализуйте класс CourtCase.
При вызове метода конструктора экземпляра (__init__) должны создаваться следующие
атрибуты экземпляра:
case_number (строка с номером дела — обязательный параметр) передаётся в качестве аргумента при создании экземпляра
case_participants (список по умолчанию пустой)
listening_datetimes (список по умолчанию пустой)
is_finished (значение по умолчанию False) 
verdict (строка по умолчанию пустая)

У экземпляра должны быть следующие методы:
set_a_listening_datetime — добавляет в список listening_datetimes судебное
заседание (структуру можете придумать сами)
add_participant — добавляет участника в список case_participants (можно просто
ИНН)
remove_participant — убирает участника из списка case_participants
make_a_decision — вынести решение по делу, добавить verdict и сменить
атрибут is_finished на True
"""
import datetime

class CourtCase:
    def __init__(self, case_number):
        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""
    
    # Метод добавляет в список listening_datetimes судебное
    def set_a_listening_datetime(self, date_time):
        self.listening_datetimes.append(date_time) 
    
    # Метод добавляет участника в список case_participants (можно просто ИНН)
    def add_participant(self, participant):
        self.case_participants.append(participant)

    # Метод убирает участника из списка case_participants
    def remove_participant(self, participant):
        self.case_participants.remove(participant)
    
   # Метод выносит решение по делу, добавить verdict и сменить атрибут is_finished на True
    def make_a_decision(self, verdict):
        self.verdict = verdict
        self.is_finished = True

# Пример использования
case = CourtCase("12345")
print(case.case_number)

case.set_a_listening_datetime("2024-04-10 10:00")
print(case.listening_datetimes)

case.add_participant("1234567890")
print(case.case_participants)

case.make_a_decision("Вынесено решение.")
print(case.verdict)
print(case.is_finished)