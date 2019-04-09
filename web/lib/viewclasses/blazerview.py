import logging

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic.base import View
from django.utils.encoding import force_text

log = logging.getLogger('blazers.web')


class BlazersView(View):

    AUDIT_PAGE_VIEWS =  True

    request = None
    template_name = None
    success_url = None
    template_url = None
    appconfig = None
    _update_session = True

    def do_get_context(self, **kwargs):
        raise NotImplementedError

    def do_post_context(self, **kwargs):
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update(self.do_get_context(**kwargs))

        if self.template_url is not None:
            return HttpResponseRedirect(self.get_template_url())

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update(self.do_post_context(**kwargs))

        return HttpResponseRedirect(self.get_success_url())

    '''
    context: {
                'announcements': ['Welcome to the site!', 'New books are coming April 15th!'],
                'new_books': ['Book1', 'Book2', 'Book3'],
                'params': {}
                }
    template: ['user/home/homepage.html']
    '''
    def render_to_response(self, context, **response_kwargs):
        """
        Force session.modified = True to force rewriting of session cookie
        """
        # self.request.session.modified = True
        response = TemplateResponse(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs)

        return response

    def _set_upload_handlers(self, request):
        return None

    def get_context_data(self, **kwargs):
        context = dict()
        context['params'] = kwargs
        return context

    def get_template_names(self):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            return [self.template_name]

    def get_success_url(self):
        """
        Returns the supplied success URL.
        """
        if self.success_url:
            # Forcing possible reverse_lazy evaluation
            url = force_text(self.success_url)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")
        return url

    def get_template_url(self):
        """
        Returns the supplied success URL.
        """
        if self.template_url:
            # Forcing possible reverse_lazy evaluation
            url = force_text(self.template_url)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a template_url.")
        return url

    def get_base_url_parts(self):
        protocol = 'http://'
        if self.request.is_secure():
            protocol = 'https://'
        host = self.request.META['HTTP_HOST']
        return protocol, host

    def get_base_url(self):
        return ''.join(self.get_base_url_parts())

    # def exit_support_mode(self, user=None):
    #     affiliationmgr.exit_support_mode(user or self.user)
    #     self.request.session.pop('supportmode', None)