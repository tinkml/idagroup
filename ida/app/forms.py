from django import forms


class UploadFileForm(forms.Form):
    url = forms.URLField(required=False)
    file = forms.FileField(required=False)


class EditImageForm(forms.Form):
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)







