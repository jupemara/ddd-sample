# DDD sample code between sevral language

- go/ : Golang
- py/ : Python

Those sample codes implement almost same business rule.
Current business rules for this projects are

- ユーザ(DDDで言うところのEntity)は氏名とIdを持つ
- ユーザの氏名(姓、名)は1文字以上16文字以下でなければならない

## Value Object

- Id (ユーザID)
- Name (氏名: 姓、名からなる)

## Entity

- User
  - Id
  - Name
