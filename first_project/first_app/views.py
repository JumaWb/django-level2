from django.shortcuts import render

# View for the index page
def index(request):
    my_dict = {'insert_content': "HELLO, I'M FROM FIRSTAPP!"}
    return render(request, 'first_app/index.html', context=my_dict)
