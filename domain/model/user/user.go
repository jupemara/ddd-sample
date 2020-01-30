package user

import (
	"errors"
)

type User struct {
	id   *Id
	name *Name
}

func NewUser(
	firstName string,
	lastName string,
) (*User, error) {
	name, err := NewName(firstName, lastName)
	if err != nil {
		return nil, errors.New("assertion error")
	}
	id, err := NewId()
	if err != nil {
		return nil, errors.New("assertion error")
	}
	return &User{
		id:   id,
		name: name,
	}, nil
}

func (u *User) ChangeName(
	firstName string,
	lastName string,
) error {
	/*
		- user.Nameで直接アクセスできるよりかは、明示的にChangeNameを入れるほうがDDDっぽいです
		- メソッド名がビジネス要件を表しているし、何より、初期作成のときと、変更時で違うロジックが入るときはここに追加のロジックを入れることができます
		  - e.g: 初回登録時は氏名は入力必須ではないけど、実際にサービスを利用するタイミングで氏名の入力が必須になるケースなど
	*/
	name, err := NewName(firstName, lastName)
	if err != nil {
		return errors.New("assertion error")
	}
	u.name = name
	return nil
}

func (u *User) Name() *Name {
	/*
	   - name属性をreadonlyにさらけ出してます
	   - ここは結構悩みどころで、user.FullName() みたいに呼び出したいときは、ダブルディスパッチぽく、`return u.name.FullName()` だけする関数を用意しておくと、userオブジェクトを使う側がFullNameについての詳細をしらなくていいし、name属性がusername属性みたいに名前が変わっても対応ができます
	     - アプリケーションの要件次第ですが、表示のロジックにFullNameが必要なときは、ドメイン層(つまりEntityやValueObject)では`u.name`だけをさらけ出して、ビューに近いレイヤーで別途ビュー用のオブジェクトを作って`user_view.FullName`みたいにダブルディスパッチするのもアリです
	*/
	return u.name
}

func (u *User) Id() string {
	return u.id.Value()
}
