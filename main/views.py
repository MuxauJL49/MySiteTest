from django.shortcuts import render


def index(request):
    data = {
        'title':'Newjdkfjkjdjf',
        'values' : ['one', 'twodfkj', 'jdkjfk', 'Hello'],
        'obj' : {
            'car': 'bmw',
            'age': 'dfdf',
            'num': 14
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')