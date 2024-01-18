## Описание
«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:

* Калькулятор. Арифметические выражения, которые необходимо вычислить
* Прогрессия. Поиск пропущенных чисел в последовательности чисел
* Определение четного числа
* Определение наибольшего общего делителя
* Определение простого числа

### Установка
Необходимо произвести установку пакетного менеджера poetry

```
pip install poetry
```

Далее инициаизируем виртуальное окружение 

```
make install
```

Собираем пакет 

```
make build
```

Для отладки публикации
```
make publish
```

В конце для установки пакета из операционной системы используйте команду:
```
make package-install
```

После выполнения всех установок можно поиграть в следующие игры
```
brain-calc #Калькулятор
brain-progression #Прогрессия
brain-even #Определение четного числа
brain-gcd #Определение наибольшего общего делителя
brain-prime #Определение простого числа
```

### Hexlet tests and linter status:
[![Actions Status](https://github.com/markwinboy/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/markwinboy/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/64ff6d5e82bc41fbc0f3/maintainability)](https://codeclimate.com/github/markwinboy/python-project-49/maintainability)

### Result of the brain-even module 
<a href="https://asciinema.org/a/jGzBtxi4iSB5ODHLzN9FyEfaR" target="_blank"><img src="https://asciinema.org/a/jGzBtxi4iSB5ODHLzN9FyEfaR.svg" /></a>

### Result of the brain-calc module 
[![asciicast](https://asciinema.org/a/t8zpu9VSBMajzFDblGGRB6X3q.svg)](https://asciinema.org/a/t8zpu9VSBMajzFDblGGRB6X3q)

### Result of the brain-gcd module 
[![asciicast](https://asciinema.org/a/lRptXA3XG2aR0tlmrp1Yu5CJr.svg)](https://asciinema.org/a/lRptXA3XG2aR0tlmrp1Yu5CJr)

### Result of the brain-progression module 
[![asciicast](https://asciinema.org/a/sYwE5JNOd6Crcpb77kg29HKYX.svg)](https://asciinema.org/a/sYwE5JNOd6Crcpb77kg29HKYX)

### Result of the brain-prime module 
[![asciicast](https://asciinema.org/a/fKv9gto6RePJoH86I9Ud9OL5h.svg)](https://asciinema.org/a/fKv9gto6RePJoH86I9Ud9OL5h)
