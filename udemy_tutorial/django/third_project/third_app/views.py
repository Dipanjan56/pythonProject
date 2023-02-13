from django.shortcuts import render


# Create your views here.
def example_view(request):
    return render(request, 'third_app/example.html')  # third_app/templates/third_app/example.html


def variable_view(request):
    third_app_var = {'first_name': 'Dipanjan',
                     'last_name': 'Kundu',
                     'some_list': [1, 2, 3],
                     'some_dict': {'inside_key': 'inside_variable'}}
    return render(request, 'third_app/variable.html', context=third_app_var)
