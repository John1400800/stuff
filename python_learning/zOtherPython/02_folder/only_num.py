OPERATORS = []
OPERATORS.extend(range(910, 920)) # Коды МТС — 910..919
OPERATORS.extend(range(980, 990)) # Коды МТС — 980..989
OPERATORS.extend(range(920, 940)) # Коды МегаФона — 920..939
OPERATORS.extend(range(902, 907)) # Коды Билайна — 902..906
OPERATORS.extend(range(960, 970)) # Коды Билайна — 960..969



def operator_code(s: str):
    """Проверяет существование оператора"""
    code = s[1:4]
    if int(code) in OPERATORS:
        return True
    else:
        return 'Exception'

print(operator_code('79188809431'))
