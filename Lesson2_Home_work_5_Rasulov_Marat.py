"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

raw_prices = [52.64, 46.5, 97.0, 42.13, 4.03, 2.0]

def format_prices(raw_price):
    formated_prices = []
    for price in raw_prices:
        formated_prices.append(f'{int(price)} руб {int((price - int(price)) * 100):2d} коп')
    return formated_prices

print('Raw data:', raw_prices)
print('Formated:', format_prices(raw_prices))
print('ID inited:', id(raw_prices))
raw_prices.sort()
print('ID sorted:', id(raw_prices))
print('Formated and sorted', format_prices(raw_prices))
sorted_reversed = sorted(raw_prices, reverse=True)
print('Formated and sorted reversed', format_prices(sorted_reversed ))
print('Top 5:', format_prices(sorted_reversed[:5]))