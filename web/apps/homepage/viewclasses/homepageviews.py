import logging

log = logging.getLogger(__name__)

import sys
sys.path.append('..')

from blazers import db
from web.lib.viewclasses.blazerview import BlazersView


class HomePageView(BlazersView):

    template_name = 'user/home/homepage.html'

    def do_get_context(self, **kwargs):
        books = db.find('Book')
        return {
            'announcements': ['Welcome to the site!',
                              'New books are coming April 15th!'],
            'new_books': books
        }