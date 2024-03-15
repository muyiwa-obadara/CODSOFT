# Titanic Survival Predictions
___
On February 15, 1912, the Titanic sank in the North Atlantic ocean after striking an iceberg. The Titanic was a British passenger airliner which was operated by White Star Line and was sailing from Southampton, England to New York in the United State.

![Titanic](https://th.bing.com/th/id/OIF.gWP9t3V7Nk18r56WwZinUg?rs=1&pid=ImgDetMain)

> Of the 2,240 passengers and crew on board, more than 1,500 lost their lives in the disaster. . . . 
[HISTORY.COM](https://www.history.com/topics/early-20th-century-us/titanic) EDITORS UPDATED: MARCH 12, 2024 | ORIGINAL: NOVEMBER 9, 2009 

For 891 passengers aboard, the following variables were record.

|     | Variable      | Description                                                        | Typw      |
|---- |---------------|--------------------------------------------------------------------|-----------|
|1.   | PassengerID   | A unique ID to represent the passeneger in the data table.         | `integer` |
|2.   | Survived      | Passenger's survival status `0: not survived`, `1: survived`       | `integer` |
|3.   | Pclass        | The social status of the passenger `1: 1st` `2: 2nd`, `3: 3rd`     |           |
|4.   | Name          | Passener's name                                                    | `str`     |
|5.   | Sex           | Passenger's sex   `male`, `female`                                 | `str`     |
| 6.  | Age           | Passenger's age                                                    | `int`     |
| 7   | SibSp         | Number os siblings/spouse aboard                                   | `int`     |
| 8.  | Parch         | Number of parents/children aboard                                  | `int`     |
| 9.  | Ticket        | Ticcket ID                                                         | `str`     |
| 10. | Fare          | Passengers fare (GBP)                                              | `float`   |
| 11. | Cabin         | Cabin                                                              | `str`     |
| 12. | Embarked      | Location of Embarkment                                             | `str`     |

`str` : String.
___
In this project, a model was developed to predict the survival status of a passenger based on other attributes listed above.