from django.dispatch import receiver
from social_django.signals import pre_update

@receiver(pre_update)
def update_user_social_data(sender, user, **kwargs):
    if kwargs['backend'].name == 'discord':
        user.email = kwargs['response']['email']
        user.username = kwargs['response']['username']
        user.save()