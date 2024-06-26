from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email.lower())
        user = self.model(email=email, is_active=is_active, is_admin=is_admin)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, is_active=True, is_admin=True, password=password)
        user.is_superuser = True
        user.save(using=self._db)

        return user
