from django import forms
from .models import *


class ItemForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for filed in self.visible_fields():
            filed.field.widget.atrs["class"] = "form-control"

    class Meta:
        model = Item
        exclude = ("user", "code",)
