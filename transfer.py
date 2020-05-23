from emoji import emojize
from datetime import date
from parsing_tut_by import parse


BEL = emojize(':Belarus:')
USA = emojize(':United_States:')
RUS = emojize(':Russia:')
EU = emojize(':European_Union:')
COURSE_LIST = parse()
USD = COURSE_LIST['Доллар США']
RUB = COURSE_LIST['100 российских рублей']
EUR = COURSE_LIST['Евро']


def dec(number):
    return round(number, 2)

def transfer_usd(money):
    MONEY = int(money)
    return f'{BEL} {dec(MONEY*USD)}\n{USA} {MONEY}\n{EU} {dec(USD/EUR*MONEY)}\n{RUS} {dec(MONEY*USD/RUB*100)}'

def transfer_eur(money):
    MONEY = int(money)
    return f'{BEL} {dec(MONEY*EUR)}\n{USA} {dec(EUR/USD*MONEY)}\n{EU} {MONEY}\n{RUS} {dec(MONEY*EUR/RUB*100)}'

def transfer_rub(money):
    MONEY = int(money)
    return f'{BEL} {dec(MONEY/100*RUB)}\n{USA} {dec(MONEY/100*RUB/USD)}\n{EU} {dec(MONEY/100*RUB/EUR)}\n{RUS} {MONEY}'

def transfer_byn(money):
    MONEY = int(money)
    return f'{BEL} {MONEY}\n{USA} {dec(MONEY/USD)}\n{EU} {dec(MONEY/EUR)}\n{RUS} {dec(MONEY/RUB*100)}'

def show_course():
    return f'Курсы НБРБ на {date.today()}:\n{USA} {USD}\n{EU} {EUR}\n{RUS} {RUB}'


