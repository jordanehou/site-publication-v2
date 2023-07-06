from re import template
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
#students registration
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
#students enroll course
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import CourseEnrollForm, UserForm, ProfileForm
#accessing the course contents
from django.views.generic.list import ListView
#from courses.models import Course
from django.views.generic.detail import DetailView

# aide a deduire si l'utilisateur a entrer les informations correcte lors du loggin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .models import videoDef 
from .forms import *


def welcome(request):
    models = videoDef.objects.all()
    return render(request, 'students/index.html', {'videoD': models})

def register(request):
    registered = False
    if request.method == 'POST':
        #here we join the two form, to get only one form, 
        # reason while we have only user_form to get the form
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            # on n'enregistre pas encore le profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return HttpResponseRedirect('logins')
        else:
            #pricise the error to the user
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm
        profile_form = ProfileForm
    content = {
        'registered': registered,
        'form1': user_form,
        'form2': profile_form
    }
    return render(request, 'students/register.html', content)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(username=username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                HttpResponseRedirect("This user is unactive")
        else:
            return HttpResponse("Incorrect user name or password")
    else:
        return render(request, 'students/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')





'''
# Create your views here.

class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html' #template
    form_class = UserCreationForm #form to fill by student
    success_url = reverse_lazy('student_course_list') #render

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result

#students enroll course
class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail', args = [self.course.id])

#accessing the course contents
#list all course that student enroll
class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course 
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

#display individual course
class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.all()[0]
        return context
'''