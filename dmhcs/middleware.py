from django.shortcuts import redirect
from django.urls import reverse

class LogoutOnBrowserBackMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        regs_urls = [
            '/regs/dashboard',
            '/regs/research_dashboard',
            '/regs/researchdashpublications',
            '/regs/researchdashprofile',
            '/regs/regulator_dashboard',
            '/regs/regulatordash_hospitals',
            '/regs/regulatordashprofile',
            '/regs/visualdata',
            '/regs/regulatordash_published',
            '/regs/regulatordash_reports',
            '/regs/loader',
            '/regs/hospital_dashboard',
            '/regs/registerpatient',
            '/regs/hospitaldashprofile',
            '/regs/hospitaldash_delivery',
            '/regs/hospitaldash_medicaldata',
            '/regs/retrieve_user',
            '/regs/register_patient'
        ]

       
        #all_app_urls = regs_urls + accounts_urls

        if request.user.is_authenticated and not any(url in request.path for url in regs_urls):
            request.session['logout_on_browser_back'] = True
        elif not request.user.is_authenticated and request.session.get('logout_on_browser_back'):
            del request.session['logout_on_browser_back']

        response = self.get_response(request)
        return response
