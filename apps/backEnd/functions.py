from django.contrib import messages
import threading
from . models import Posts, Users, NumUsersConnected

def sendErrors(request, errors):
    for key in errors:
        messages.error(request, errors[key], extra_tags = key)
    return errors