from optparse import make_option

from django.core.management.base import NoArgsCommand
from django.db.models import Q
from django.contrib.auth.models import User

class Command(NoArgsCommand):
    help = "Creates an admin (superuser), unless there's already such " \
           "user"

    option_list = NoArgsCommand.option_list + (
        make_option('--username',
                    action='store',
                    dest='username',
                    default=False),
        make_option('--email',
                    action='store',
                    dest='email',
                    default=False),
        make_option('--pswd',
                    action='store',
                    dest='pswd',
                    default=False),
        )

    def handle_noargs(self, **options):
        if User.objects.filter(
            Q(username__iexact=options['username'])|
            Q(email__iexact=options['email'])|
            ):
            print "Admin %s already exists!" % options['username']

        admin = User.objects.create_superuser(username=options['username'],
                                              email=options['email'],
                                              password=options['pswd'])
        print "Created admin %s!" % admin.username
