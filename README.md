sample code Golang of DDD for creating user domain object

## Value Object

- `domain/model/user/id.go`
    + システム内で一意のIDを持つという要件
- `domain/model/user/name.go`
    + ユーザの氏名オブジェクトの例です
- `domain/model/user/user_id.go`
    + User Entity内部では使われていませんが、ユーザIDをユーザが自分で指定できるとき、ユーザIDは4文字以上32文字以下という成約を持つ

## Entity

- `domain/model/user/user.go`

## 各種ユニットテスト

- `domain/model/user/*_test.go`

[table driven tests](https://github.com/golang/go/wiki/TableDrivenTests)という手法で、テストケースを列挙して書いてます
