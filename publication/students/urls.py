from django.urls import path
from . import views
#import cache
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('user_register', views.register, name='register'),
    path('logins', views.user_login, name='login'),
    path('logouts', views.user_logout, name='logouts'),


    #path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
    #path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    #path('courses/', views.StudentCourseListView.as_view(), name='student_course_list'),
    #path('course/<pk>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail'),
    #path('course/<pk>/<module_id>/', cache_page(60 * 15)(views.StudentCourseDetailView.as_view()), name='student_course_detail_module'),
    
]