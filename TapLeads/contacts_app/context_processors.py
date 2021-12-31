# from django.contrib.auth.decorators import login_required

# from .decorators import allowed_users
# from django.contrib.auth import authenticate

def all_over_app(request):
     if request.user.is_authenticated:
          # give the user type
          group = request.user.groups.filter(user=request.user)[0]
          sub_type=str(group.name)
          return {'sub_type' : sub_type}
     else:
          return {'msg' : 'login'}