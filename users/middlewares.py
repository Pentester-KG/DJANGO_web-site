from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ExpWorkMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            exp = int(request.POST.get('exp_work'))
            if exp <= 1:
                return HttpResponseBadRequest('Ваш опыт мал для регистрации')
            elif 1 <= exp <= 3:
                request.experience_work = 'Junior'
            elif 3 <= exp <= 10:
                request.experience_work = 'Middle'
            elif 10 <= exp <= 25:
                request.experience_work = 'Senior'
            else:
                return HttpResponseBadRequest('Извините вы не подходите для регистрации')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'experience_work', 'Стаж не определен')


