Необходимо реализовать сервис с следующим функционалом
с на языке Python использованием фреймворка Django.
- В базе данных PostgreSQL должна быть таблица currency c колонками:
  - id — первичный ключ
  - name — название валюты
  - rate — курс валюты к рублю

- Должна быть консольная команда для обновления данных в таблице currency.

- Данные по курсам валют можно взять отсюда: http://www.cbr.ru/scripts/XML_daily.asp

- Реализовать 2 REST API метода:
  - GET /currencies — должен возвращать список курсов валют с возможность пагинации
  - GET /currency/ — должен возвращать курс валюты для переданного id
  - API должно быть закрыто bearer авторизацией.