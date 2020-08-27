from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import AccountCreationForm


class SignUp(FormView):
    template_name = 'registration/signup.html'
    form_class = AccountCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
