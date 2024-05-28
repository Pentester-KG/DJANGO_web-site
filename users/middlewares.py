from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class ExpWorkMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            exp_work = int(request.POST.get('exp_work'))
            if exp_work <= 1:
                return HttpResponseBadRequest('Ваш опыт мал для регистрации')
            elif 1 <= exp_work <= 3:
                request.experience_work = 'Junior'
            elif 3 <= exp_work <= 10:
                request.experience_work = 'Middle'
            elif 10 <= exp_work <= 25:
                request.experience_work = 'Senior'
            else:
                return HttpResponseBadRequest('Извините вы не подходите для регистрации')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'experience_work', 'Стаж не определен')


