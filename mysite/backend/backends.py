"""."""
from django.contrib.auth.backends import BaseBackend
from user.models import Users


class Backend(BaseBackend):
    """."""

    def authenticate(self, request, username=None, password=None):
        """."""
        try:
            user = Users.objects.get(username=username)

            if user.check_password(password):

                return user

            pass

        except Users.DoesNotExist:

            pass

    def get_user(self, user_id):
        """."""
        try:
            user = Users.objects.get(id=user_id)

            return user.id

        except Users.DoesNotExist:

            return None
