# pytechscrtesttask-scripter
- date - информация о дате совершения операции
- state - статус перевода (EXECUTED - выполнена, CANCELED - отменена)
- operationAmount - сумма операции и валюта
- description - описание типа перевода
- from - откуда
- to - куда

Задача
Вывести на экран список из 5 последних совершенных (выполненных) операций клиента в
формате:
&lt;дата перевода&gt; &lt;описание перевода&gt;

&lt;откуда&gt; -&gt; &lt;куда&gt;

&lt;сумма перевода&gt; &lt;валюта&gt;


Пример для одной операции:

14.10.2018 Перевод организации

Visa Platinum 7000 79** **** 6361 -&gt; Счет **9638
82771.72 руб.

Условия
- решение должно представлять из себя скрипт на языке python
- вывести последние 5 выполенных (EXECUTED) операций на экран
- операции разделены пустой строкой
- дата перевода должна быть в формате ДД.ММ.ГГГГ (пример 14.10.2018)
- сверху списка должны быть самые последние операции (по дате)
- номер карты должен маскироваться и не отображаться целиком, в формате
XXXX XX** **** XXXX
(видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных
пробелом)
- номер счета должен маскироваться и не отображаться целиком, в формате
**XXXX
(видны только последние 4 цифры номера счета)
