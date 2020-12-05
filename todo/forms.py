from django import forms
class todoForm(forms.Form):
    task = forms.CharField(max_length=2000, widget =forms.TextInput(attrs = {
        'class':'task-description-field',
        'id':'task-description-field',
        'placeholder':"Task description.."
    }))
    done = forms.BooleanField(required=False, widget = forms.CheckboxInput(attrs={
        'class':'task-done-box',
        'id':'task-done-box',
    }))
