package user_test

import (
	"testing"

	"github.com/jupemara/ddd-guys/go/domain/model/user"
)

func TestNewName(t *testing.T) {
	cases := map[string]struct {
		FirstName string
		LastName  string
		IsError   bool // わかりやすくするためにIsError使ってますが、僕はよくExpectedとかを使います
	}{
		"valid":            {"John", "Smith", false},
		"empty last name":  {"John", "", true},
		"empty first name": {"", "Smith", true},
		"all of empty":     {"", "", true},
	}
	for k, c := range cases {
		_, err := user.NewName(c.FirstName, c.LastName)
		if (err != nil) != c.IsError {
			t.Errorf("%s: failed", k)
		}
	}

}

func TestName_FullName(t *testing.T) {
	cases := map[string]struct {
		FirstName string
		LastName  string
		Expected  string
	}{
		"very normal":   {"John", "Smith", "John Smith"},
		"include space": {"John", " Smi th", "John  Smi th"},
	}
	for k, c := range cases {
		name, err := user.NewName(c.FirstName, c.LastName)
		if err != nil {
			t.Errorf("error message: %v", err)
		}
		if name.FullName() != c.Expected {
			t.Errorf("%s: failed", k)
		}
	}
}
