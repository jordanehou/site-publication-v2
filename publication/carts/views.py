from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from courses.models import Course
from .cart import Cart
from .forms import CartAddCourseForm

# Create your views here.

@require_POST
def cart_add(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    
    
    cart.add(course=course)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    cart.remove(course)
    return redirect('cart:cart_detail')

def cart_detail(request):
    """View to display the cart and its item """
    cart = Cart(request)
    return render(request, 
                  'cart/detail.html', 
                  {'cart':cart})