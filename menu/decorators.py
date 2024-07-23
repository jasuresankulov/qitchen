from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def sign_up_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('create_user')  # Перенаправить на страницу регистрации
        return view_func(request, *args, **kwargs)
    return _wrapped_view
