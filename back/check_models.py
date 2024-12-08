def check_bad_weather(wet_info:dict):
    '''Функция анализа погодных условий'''
    if wet_info['temperature_celsius'] < 0:
        return 'Очень холодно'
    elif wet_info['temperature_celsius'] > 35:
        return 'Очень жарко'
    elif wet_info['wind_speed_kh'] > 50:
        return 'Сильный ветер'
    elif wet_info['precipitation_probability'] > 70:
        return 'Высокая вероятность осадков'
    else:
        return 'Самле дучшее время для прогулки'
    
