from django.views.generic import TemplateView



class HomePageView(TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomePageView, self).get_context_data(*args, **kwargs)
    #     context['tops'] = Player.objects.featured().order_by('-goals')[:3]
    #     context['top_clubs'] = Club.objects.all().order_by('-points')[:3]
    #     return context
