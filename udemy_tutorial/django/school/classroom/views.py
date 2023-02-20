from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Teacher

# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')

"""this is called class based view - template view -> it will connect to thet template we are providing"""


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


"""this is called class based view - form view -> it will connect to the forms we are providing"""


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URl?
    # it is actual url not a template
    success_url = reverse_lazy("classroom:thank_you")

    # what to do with the form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


"""Model Based View -> CreateView
It will by default try to search model_form.html e.g. teacher_form.html
also once you hit the submit button it will save the information in model instance by using .save() method
"""


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank_you')


"""Model Based View -> ListView
It will by default try to search model_list.html e.g. teacher_list.html
"""


class TeacherListView(ListView):
    model = Teacher
    """if you want the exact model view as per structuring"""
    fields = '__all__'
    """if you want to create your customized view for listing"""
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'


"""Model Based View -> DetailView
It will by default try to search model_detail.html e.g. teacher_detail.html
"""


class TeacherDetailView(DetailView):
    model = Teacher
    # PK -> {{teacher}}
    # will return only one model entry


"""Model Based View -> UpdateView
It will by share model_form.html e.g. teacher_form.html
"""


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')


"""Model Based View -> UpdateView
It is a Form --> Confirm Delete Button
It will by default try to search model_confirm_delete.html e.g. teacher_confirm_delete.html
"""


class TeacherDeleteView(DeleteView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')

