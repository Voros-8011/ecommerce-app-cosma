from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

User = get_user_model()

class VendoreReqiuredMixin:
    def dispatch(self ,req,*args,**kwargs):
        if req.user.role != 'vendor':
            raise PermissionDenied
        return super().dispatch(req,*args,**kwargs)

class Owner_List_view(ListView):
    '''nothing maaa maan'''

class Owner_Detail_view(DetailView):
    '''nothing maaa maan'''


class Owner_Update_View(LoginRequiredMixin,UpdateView,VendoreReqiuredMixin):
    '''
    sub-class Owner_Update_View to pass to req to the form and limit the
    querest to the requsting view
    '''
    def get_queryset(self):
        print('update get quryset called')
        qs = super(Owner_Update_View,self).get_queryset()
        return qs.filter(owner=self.request.user)
    




class Owner_Create_View(LoginRequiredMixin,CreateView,VendoreReqiuredMixin):

    def form_valid(self,form):
        print('form_valid called')
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(Owner_Create_View,self).form_valid(form)
    


class Owner_Delet_View(LoginRequiredMixin,DeleteView,VendoreReqiuredMixin):
    '''
    sub-class Owner_Update_View to pass to req to the form and limit the
    querest to the requsting view
    '''
    def get_queryset(self):
        print('update get quryset called')
        qs = super(Owner_Delet_View,self).get_queryset()
        return qs.filter(owner=self.request.user)