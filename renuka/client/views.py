from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
def home_view(request):


def form_view(request):
    if request.method == 'POST':
# VALUE INSIDE BRACKETS ARE ID FROM HTML TAGS
        user_email = request.POST['mail_id']
        username = request.POST['name']
        dept = request.POST['dept']
        type = request.POST['type']
        try:
            user = BookUser(isbn=book_isbn, email_id=user_email, name=username, dept=dept, type=type)
            book_save = Book.objects.get(isbn=book_isbn)
            book_save.books_count-=1
            book_save.save()
            user.save()         

            return HttpResponseRedirect("/success")
        except:
            return HttpResponseRedirect("/fail")
    else:
        return render(request, "reserve.html")     

def costumes_view(request):

def ornaments_view(request):

def accessories_view(request):






    