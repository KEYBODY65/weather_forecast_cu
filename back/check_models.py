def check_bad_weather(wet_info:dict):
    '''Функция анализа погодных условий'''
    if wet_info['temperature_celsius'] < 0:
        return 'Температура ниже 0, советуем одеться потеплее'
    elif wet_info['temperature_celsius'] > 35:
        return 'Очень жарко, советуем оставаться дома или, если вы на улице оставайтесь в тени'
    elif wet_info['wind_speed'] > 7:
        return 'Сильный ветер, советуем оставаться дома, воизбежании несчастных случаев'
    elif wet_info['precipitation_probability'] > 70:
        return 'Высокая вероятность осадков, не забудьте захватить с собой зонтик'
    else:
        return 'Самле лучшее время для прогулки'
    
