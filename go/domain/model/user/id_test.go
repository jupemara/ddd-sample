package user_test

import (
	"testing"

	"github.com/jupemara/ddd-guys/go/domain/model/user"
)

// NewIdのテスト、ほぼUUIDのテストなので不要って思うかもしれませんが、ライブラリの動作確認をしたり(go run xxx.goみたいに手元で確認すると再現性がない)、忘れた頃に使い方を見直す場所として時々書いたりします

func TestNewId(t *testing.T) {
	id, err := user.NewId()
	if err != nil {
		t.Errorf("error message: %v", err)
	}
	if len(id.Value()) <= 0 {
		t.Errorf("something wrong within generating UUID. actual value: %s", id.Value())
	}
}
