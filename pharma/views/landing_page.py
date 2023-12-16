from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    """
    Renders the landing page.

    Uses a template to display the landing page content.
    """
    template_name = 'pharma/landing_page.html'
