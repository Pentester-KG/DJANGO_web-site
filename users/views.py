from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, middlewares, forms


class RegisterView(CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'users/register.html'
    success_url = '/login/'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        exp_work = form.cleaned_data['exp_work']
        if exp_work <= 1:
            self.object.experience_work = 'Junior'
        elif 1 <= exp_work <= 3:
            self.object.experience_work = 'Middle'
        elif 3 <= exp_work <= 25:
            self.object.experience_work = 'Senior'
        else:
            self.object.experience_work = 'Стаж не определен'
        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.UserProfile

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experience_work'] = getattr(self.request, "experience_work", 'Стаж не определен')
        return context








