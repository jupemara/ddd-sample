package user

import (
	"errors"
)

type Name struct {
	firstName string
	lastName  string
}

func NewName(firstName string, lastName string) (*Name, error) {
	for _, v := range []bool{
		len(firstName) < 1,
		len(lastName) < 1,
	} {
		if v {
			return nil, errors.New("assertion error")
		}
	}
	return &Name{firstName, lastName}, nil
}

func (n *Name) FirstName() string {
	return n.firstName
}

func (n *Name) LastName() string {
	return n.lastName
}

func (n *Name) FullName() string {
	return n.FirstName() + " " + n.LastName()
}
