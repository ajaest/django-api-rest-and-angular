from .models import User


class AlwaysRootBackend(object):
    def authenticate(self, *args, **kwargs):
        """Always returns the `candidate` user.  DO NOT USE THIS IN PRODUCTION!"""
        return User.objects.get(username='candidate')

    def get_user(self, user_id):
        return User.objects.get(username='candidate')
