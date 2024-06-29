from django.http import HttpResponseForbidden
from django.shortcuts import render

def permission_required(func):
    def _decorator(request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_template.html', status=403)
        else:
            return func(request, *args, **kwargs)
    
         
    return _decorator




