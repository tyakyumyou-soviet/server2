from django import forms
from django.core.exceptions import ValidationError

widget_textarea = forms.Textarea(
    attrs={
        "class": "form-control"
    }
)

widget_textinput = forms.TextInput(
    attrs={
        "class": "form-control"
    }
)


class TextForm(forms.Form):
    text = forms.CharField(label="", widget=widget_textarea)

    # 自動的に呼ばれます。エラーを発生させると簡単に表示できます
    def clean(self):
        # djangoもともとのバリデーションを実行してデータを取得
        data = super().clean()
        text = data["text"]
        if len(text) < 4:
            raise ValidationError("テキストが短すぎます。")

        # 最後は必ずデータ全体を返します
        return data
