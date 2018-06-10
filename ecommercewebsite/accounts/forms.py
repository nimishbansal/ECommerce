from allauth.account.forms import SignupForm

class CustomizedSignupForm(SignupForm):
    def __init__(self,*args,**kwargs):
        super(CustomizedSignupForm,self).__init__(*args,**kwargs)
        self.fields["email"].label=""
        self.fields["username"].label=""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""





