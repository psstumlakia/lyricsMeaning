#   defining our own middleware to deal with the logging required in view.py
#   You should add this to the setting.py too
import re

from django.conf import settings
from django.urls import reverse  # To stop hard coding urls
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

EXEMPT_HOME = [re.compile(settings.LOGIN_HOME.lstrip('/'))]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        print(path)

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        url_is_home = any(url.match(path) for url in EXEMPT_HOME)
        print(url_is_home)
        if url_is_home:
            if not request.user.is_authenticated:
                return None
            url_is_exempt = False

        if path == reverse('logout'.lstrip('/')):
            logout()


        #  If Logged in and accessing login or register pages
        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        # Authenticated and Not an exempt URL(profile), & Not Authenticated and URL is exempt
        elif request.user.is_authenticated or url_is_exempt:
            return None
        #   Not logged in and URL not exempted
        else:
            #   Need Authentication (Profile) , Not logged in and Not an exempt URL(PROFILE)
            return redirect(settings.LOGIN_URL)