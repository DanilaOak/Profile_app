from django import template
from profile_app.models import Profile

register = template.Library()


@register.inclusion_tag('profile_app/link.html')
def edit_list(request):
    profile = Profile.objects.get(user=request.user)
    return {
        'link': 'admin/profile_app/profile/{}/change/'.format(profile.id),
        'title': 'profile in admin',
    }
