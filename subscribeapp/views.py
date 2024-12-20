from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, RedirectView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, name='get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        return reverse('projectapp:detail', kwargs={'pk' : self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)
        if subscription.exists():  
            subscription.delete()
        else:
            Subscription(user=user, project=project).save() 
           
        return super(SubscriptionView, self).get(request, *args, **kwargs)
    
@method_decorator(login_required, name='get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self): # 가지고 오는 게시글들의 조건을 바꿀 수 있는 함수
        projects = Subscription.objects.filter(user=self.request.user).values_list("project") 
        article_list = Article.objects.filter(project__in=projects) 