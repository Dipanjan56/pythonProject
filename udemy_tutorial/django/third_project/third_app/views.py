from django.shortcuts import render


# Create your views here.
def example_view(request):
    return render(request, 'third_app/example.html')  # third_app/templates/third_app/example.html


def variable_view(request):
    third_app_var = {'first_name': 'Dipanjan',
                     'last_name': 'kuNdu',
                     'some_list': [1, 2, 3, 4],
                     'some_dict': {'inside_key': 'inside_variable'},
                     'user_logged_in': True}
    return render(request, 'third_app/variable.html', context=third_app_var)


def inherited_view(request):
    return render(request, 'third_app/inherited.html')


