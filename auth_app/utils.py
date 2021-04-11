from django.contrib.auth.models import Group

def have_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False