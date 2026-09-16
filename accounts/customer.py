from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
class CustomerRequiredMixin(LoginRequiredMixin):
    def dispatch (self ,req,*args,**kwargs):
        if req.user.role != 'customer':
            return redirect('eccom_home:main')
        return super().dispatch(req, *args, **kwargs)
