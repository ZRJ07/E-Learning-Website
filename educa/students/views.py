from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm
from django.views.generic.list import ListView
from courses.models import Course
from django.views.generic.detail import DetailView

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#from .tl import estimate_label
#import matplotlib.image as mpimg

# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)

#         image = mpimg.imread(myfile)
#         _, col = estimate_label(image)
#         return render(request, 'students/ai.html', {
#             'uploaded_file_url': uploaded_file_url,
#             'col': col
#         })
#     return render(request, 'students/ai.html')


# to view the student registration form
class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')
    # check the username and password
    def form_valid(self, form):
        result = super(StudentRegistrationView,
                        self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result



