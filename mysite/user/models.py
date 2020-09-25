"""."""
from django.db import models
import uuid
import bcrypt


class Users(models.Model):
    """."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    username = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    bio = models.TextField()
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @staticmethod
    def hash(data, salt):
        """."""
        try:
            return bcrypt.hashpw(data.encode("utf-8"), salt.encode("utf-8")).\
                decode("utf-8")

        except:
            return ""

    def check_password(self, password):
        """."""
        _hash = self.hash(password, self.password)

        if _hash == self.password:

            return True

        return False

    class Meta:
        """."""

        db_table = "users"


class Friends(models.Model):
    """."""

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, related_name="u")
    friend = models.ForeignKey(Users, models.DO_NOTHING, related_name="f")
    chat_id = models.UUIDField(default=uuid.uuid4, editable=False)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @classmethod
    def manage_chat(cls, user_id, friend_id):
        """."""
        me = cls.objects.get(user_id=user_id, friend_id=friend_id)

        friend = cls.objects.get(user_id=friend_id, friend_id=user_id)

        if not me.chat_id:

            me.chat_id = uuid.uuid4()

            me.save()

            friend.chat_id = me.chat_id

            friend.save()

        return me.chat_id

    class Meta:
        """."""

        db_table = "friends"

        unique_together = (("user", "friend"),)
