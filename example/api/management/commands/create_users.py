from django.core.management.base import BaseCommand

from example.api.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.first()
        user.first_name="Gregor"
        user.last_name="McCandidate"
        user.username="candidate"
        user.save()
        #users = ['Bob', 'Sally', 'Joe', 'Rachel']
        #users = []
        #for user in users:
        #    username = user.lower()
        #    User.objects.create(username=username, email="{}@example.com".format(username), first_name=user)
