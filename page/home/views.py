from django.views.generic import TemplateView
from page.home.models import Home


class HomeTemplateView(TemplateView):
    template_name = 'diplom/activar/home.html'

    def get_content_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.all()
