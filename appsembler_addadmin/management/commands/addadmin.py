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
                    default=''),
        make_option('--email',
                    action='store',
                    dest='email',
                    default=''),
        make_option('--pswd',
                    action='store',
                    dest='pswd',
                    default=''),
        )

    def handle_noargs(self, **options):
        if not options['username'] or \
           not options['pswd'] or \
           not options['email']:
            return "Missing parameters!\n"

        if User.objects.filter(Q(username=options['username']) |
                               Q(email=options['email'])):
            self.stdout.write(u"Admin %s already exists!\n" % \
                           options['username'])
            return

        admin = User.objects.create_superuser(username=options['username'],
                                              email=options['email'],
                                              password=options['pswd'])
        self.stdout.write(u"Created admin %s!\n" % admin.username)
