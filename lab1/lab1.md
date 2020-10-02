# Лабораторна робота No 1.

## Проектування бази даних та ознайомлення з базовими операціями СУБД
PostgreSQL

### Метою роботи є здобуття вмінь проектування бази даних та практичних
навичок створення реляційних баз даних за допомогою PostgreSQL.


Варіант 13

![University Studies](https://github.com/Kyanka/DB/blob/main/lab1/Screenshot_4.png)
<p align="center">Рис.1. Графічний файл розробленої моделі «сутність-зв’язок»</p>
</br></br></br></br>



![Tables](https://github.com/Kyanka/DB/blob/main/lab1/Screenshot_5.png)
<p align="center">Рис.2. Структура нормалізованої бази даних з назвами таблиць та зв’язками між ними</p>
</br>



![Tables](https://github.com/Kyanka/DB/blob/main/lab1/Screenshot_6.png)
<p align="center">Рис.3.1. Вміст таблиці Students</p>
</br>



![Tables](https://github.com/Kyanka/DB/blob/main/lab1/Screenshot_7.png)
<p align="center">Рис.3.2. Вміст таблиці Groups</p>
</br>


![Tables](https://github.com/Kyanka/DB/blob/main/lab1/Screenshot_8.png)
<p align="center">Рис.3.3. Вміст таблиці Teachers</p>
</br>


![Tables](https://github.com/Kyanka/DB/blob/main/lab1/Screenshot_9.png)
<p align="center">Рис.3.4. Вміст таблиці Classes</p>
</br>



![Tables](https://github.com/Kyanka/DB/blob/main/lab1/Screenshot_10.png)
<p align="center">Рис.3.5. Вміст таблиці groups_classes</p>
</br>


### Контрольні запитання

1. Сформулювати призначення діаграм типу «сутність-зв’язок».
  
  -визначають та візуалізують предметну область, представляють сутності, атрибути і зв'язків графічно  
  
2. Назвати основні об’єкти схеми PostgreSQL.
  - scheme -> public -> tables

3. Навести приклади різних типів зв’язків у базах даних (1:1, 1:N, N:M)
  Розглянемо на прикладі Університету
  - 1:1 -> Пасажир може зайняти тільки одне місце, і місце може бути зайняте тільки одним пасажиром
  - 1:n -> Пасажирів може перевіряти тільки один контролер, але контролер може перевіряти багато пасажирів
  - n:m -> Багато пасажирів може їхати на багатьох автобусах, і навпаки
  
### Висновки
  
  Під час виконання даної лабораторної роботи ми навчились проектувати базу даних створювати реляційні 
  бази даних за допомогою PostgreSQL.
