package user

import "errors"

type UserId struct {
	value string
}

func NewUserId(value string) (*UserId, error) {
	for _, v := range []bool{
		len(value) < 4,
		len(value) > 32,
	} {
		if v {
			return nil, errors.New("assertion error")
		}
	}
	return &UserId{value}, nil
}

func (u *UserId) Value() string {
	return u.value
}
