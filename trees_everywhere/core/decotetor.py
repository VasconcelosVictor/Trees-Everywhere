from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import *

def permission_required(func):
    def _decorator(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            print(request.headers.get('Cookie'))
            # session id_account
            active_account_id = request.session['active_account_id']
            
            # Verifica se o usuário pertence à conta ativa
            try:
                account = Account.objects.get(id=int(active_account_id))
                if request.user not in account.users.all():
                    return render(request, '403_template.html', status=403)
            except Account.DoesNotExist:
                return render(request, '403_template.html', status=403)
            
            
        return func(request, *args, **kwargs)
      

    
         
    return _decorator




