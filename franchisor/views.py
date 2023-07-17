from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views import View
from .form import fProfileForm
from .models import fProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .form import ContactForm
from django.contrib.auth.models import User


def display(request):
    profiles = fProfile.objects.all()

    selected_city=request.GET.get('city')
    selected_investment=request.GET.get('investment')

    if selected_city:
        profiles=profiles.filter(city=selected_city)

    # if selected_investment:
    #     profiles=profiles.filter(investment=selected_investment)

    cities=fProfile.objects.values_list('city',flat=True).distinct()
    # investments=fProfile.objects.values_list('investment',flat=True).distinct()
    context = {
        'profiles': profiles,
        'cities':cities,
        'selected_city':selected_city,
        # 'investments':investments,
        # 'selected_investments':selected_investment
    }
    return render(request, 'detail.html', context)

@login_required
def account_redirect(request):
    return redirect('franchisor:user_profile', pk=request.user.pk)

class ProfileView(View):
     def get(self,request,pk,*args, **kwargs):
          profile=fProfile.objects.get(pk=pk)
          user= profile.user

          context ={
               'user' : user,
               'profile' :profile,

          }

          return render(request,'detailed_display.html',context)


class userProfileView(View,LoginRequiredMixin,UserPassesTestMixin):
    
    def get(self,request,pk,*args, **kwargs):
          profile=fProfile.objects.get(pk=pk)
          user=profile.user
          context ={
               'user' : user,
               'profile' :profile,

          }
          
          return render(request,'user_profile_display.html',context)
    
    def test_func(self):
          profile = self.get_object()
          return self.request.user == profile.user

class Index(View):
    def get(self,request,*args,**kwargs):
        user_count = fProfile.objects.count()
        context = {
          'user_count': user_count
          
     }
        return render(request,'index.html')

# Create your views here.

class Data(View):
    
    def get(self,request,*args,**kwargs):
        form = fProfileForm()

        context={
            'form':form,
        }

        return render(request,'form.html',context)
    
    def post(self,request,*args,**kwargs):
        form = fProfileForm(request.POST,request.FILES)

        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.user=request.user
            new_post.save()

            return redirect('franchisor:account_redirect')
        
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     model = fProfile
     
     fields = ['name','phone_number','operation_commenced','franchise_commenced','LOGO','city','about_us','mission','vision','category','investment','brand_fee','royalty','anticipated_return_on_investment','likely_payback_period','floor_area_required','employees_requires','standard_agreement','franchise_term','term_renewable']
     template_name = 'profile_edit.html'
     
     
          
     def get_success_url(self):
          pk = self.kwargs['pk']
          return reverse_lazy('franchisor:user_profile', kwargs={'pk': pk})

     def test_func(self):
          profile = self.get_object()
          return self.request.user == profile.user
     




def contact(request):
    
    if request.method == 'POST':
            message="Your message along with your MailID has been sent to the franchisor. Keep checking your Mail for further communication.Till then Keep LinkingUP!!"
            email=request.POST.get('email',False)
            name=request.POST.get('name',False)
            send_mail(
                'Your Message has been sent',
                message,
                'chittigk4158@gmail.com',
                [email],
                fail_silently=False
            )
                 
            # Optionally, you can redirect the user to a success page
    return render(request, 'response.html')
    

def feedback(request):
    if request.method == 'POST':
        message='We have received your feedback. Our team will work on it. Thank you!. Keep Linking Up!'
        email=request.POST.get('email',False)
        name=request.POST.get('name',False)
        send_mail(
            'Thank You for your feedback.',
            message,
            'chittigk4158@gmail.com',
            [email],
            fail_silently=False
        )

    return render(request, 'success.html')


def test(request):
     return render(request, 'detail.html')