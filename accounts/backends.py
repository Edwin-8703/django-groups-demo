

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailBackend(ModelBackend):
    """
    Authenticate using email instead of username.
    The user's full name (first_name + last_name) will naturally
    show in templates via {{ request.user.get_full_name }} or
    {{ request.user.first_name }}.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # username field on the form actually contains the email
            user = User.objects.get(email__iexact=username)
        except User.DoesNotExist:
            return None
        except User.MultipleObjectsReturned:
            # If duplicate emails exist, take the most recent active one
            user = User.objects.filter(email__iexact=username, is_active=True).last()

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None