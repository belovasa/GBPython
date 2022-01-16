import requests
def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    result_value_str=''
    code = code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if code not in response:
        return None
    result_value_str = response[response.find('<Value>', response.find(code)) + 7:response.find('</Value>', response.find(code))]
    i = result_value_str.find(',')
    result_value_str = result_value_str[:i]+'.'+result_value_str[i+1:]
    result_value = float(result_value_str)
    return result_value
