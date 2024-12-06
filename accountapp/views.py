from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_owner_required
from accountapp.forms import AccountUpdateForm

from articleapp.models import Article

# '''
# deco_arr = [account_owner_required, login_required] 장고 5.0 안됨?
# #https://docs.djangoproject.com/ko/5.0/_modules/django/utils/decorators/
# '''
# '''
# @login_required
# def hello_world(request):
#     #return HttpResponse('Hello')
#     #return render(request, 'base.html')

    
#     if request.method == "POST":
#         temp = request.POST.get('hello_world_input')
#         new = HelloWorld() # 모델
#         new.text = temp
#         new.save() # db에 저장됨

#         #hello_world_list = HelloWorld.objects.all() # 모두 가져옴

#         #return render(request, 'accountapp/hello_world.html', context={'text':temp})
#         #return render(request, 'accountapp/hello_world.html', context={'hello_world_output':new})#객체 내보냄
#         #return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#     else:
#         #return render(request, 'accountapp/hello_world.html', context={'text':'GET method'})
#         hello_world_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})
# '''
# 클래스 base view
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home') # 로그인 성공하면 재연결
    # 함수형 뷰 reverse() 클래스형 뷰 reverse_lazy()
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(login_required, name='dispatch')
@method_decorator(account_owner_required, name='dispatch')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home') 
    template_name = 'accountapp/update.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(account_owner_required, name='dispatch')
class AccountDeleteView(DetailView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

# '''

# # 클래스 base view
# class AccountCreateView(CreateView):
#     model = User
#     form_class = UserCreationForm
#     success_url = reverse_lazy('accountapp:hello_world') # 로그인 성공하면 재연결
#     # 함수형 뷰 reverse() 클래스형 뷰 reverse_lazy()
#     template_name = 'accountapp/create.html'

# class AccountDetailView(DetailView, MultipleObjectMixin):
#     model = User
#     context_object_name = 'target_user'
#     template_name = 'accountapp/detail.html'

#     paginate_by = 25

#     def get_context_data(self, **kwargs):
#         object_list = Article.objects.filter(writer=self.get_object())
#         return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

# @method_decorator(login_required, name='dispatch')
# @method_decorator(account_owner_required, name='dispatch')
# class AccountUpdateView(UpdateView):
#     model = User
#     context_object_name = 'target_user'
#     form_class = AccountUpdateForm
#     success_url = reverse_lazy('accountapp:hello_world') 
#     template_name = 'accountapp/update.html'

# @method_decorator(login_required, name='dispatch')
# @method_decorator(account_owner_required, name='dispatch')
# class AccountDeleteView(DetailView):
#     model = User
#     context_object_name = 'target_user'
#     success_url = reverse_lazy('accountapp:login')
#     template_name = 'accountapp/delete.html'

# '''

