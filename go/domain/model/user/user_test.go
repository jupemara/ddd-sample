package user_test

import (
	"testing"

	"github.com/jupemara/ddd-guys/go/domain/model/user"
)

func TestNewUser_ChangeName(t *testing.T) {
	user, err := user.NewUser("John", "Smith")
	if err != nil {
		t.Errorf("error message: %v", err)
	}
	cases := map[string]struct {
		FirstName        string
		LastName         string
		ExpectedFullName string
		ExpectedError    bool
	}{
		"valid in Japanese": {"太郎", "山田", "太郎 山田", false},
		"empty last name":   {"John", "", "", true},
		"empty first name":  {"", "Smith", "", true},
		"all of empty":      {"", "", "", true},
	}
	for k, c := range cases {
		err := user.ChangeName(c.FirstName, c.LastName)
		if (err != nil) != c.ExpectedError {
			t.Errorf("%s: %v", k, err)
		}
		// 変更された結果を確かめてるだけなので、ここ以下のテストはなくてもいいかもとは思います
		if err == nil {
			fullName := user.Name().FullName()
			if fullName != c.ExpectedFullName {
				t.Errorf("%s: unexpected fullname. actual: %s", k, fullName)
			}
		}
	}
}
