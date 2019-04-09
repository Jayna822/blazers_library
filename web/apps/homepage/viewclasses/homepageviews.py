import logging

log = logging.getLogger(__name__)

from web.lib.viewclasses.blazerview import BlazersView

class HomePageView(BlazersView):

    template_name = 'user/home/homepage.html'

    def do_get_context(self, **kwargs):
        return {
            'announcements': ['Welcome to the site!',
                              'New books are coming April 15th!'],
            'new_books': ['Book1', 'Book2', 'Book3']
        }