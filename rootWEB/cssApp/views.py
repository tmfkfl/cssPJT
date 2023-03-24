from django.shortcuts import render

# Create your views here.

def index(request):
    print(">>>>>>>>>>>debug 127.0.0.1:8000/css/main     main()  call~~~~")
    return render(request, 'css/index.html')

def external(request):
    print(">>>>>>>>>>>debug 127.0.0.1:8000/css/external    external()  call~~~~")
    return render(request, 'css/external.html')

def selector(request):
    print(">>>>>>>>>>>debug 127.0.0.1:8000/css/selector    selector()  call~~~~")
    return render(request, 'css/selector.html')

def descendant(request):
    print(">>>>>>>>>>>debug 127.0.0.1:8000/css/descentdant    descendant()  call~~~~")
    return render(request, 'css/descendant.html')

def box(request):
    print(">>>>>>>>>>>debug 127.0.0.1:8000/css/box    box()  call~~~~")
    return render(request, 'css/box.html')

def layout(request):
    print(">>>>>>>>>>>debug 127.0.0.1:8000/css/layout    layout()  call~~~~")
    return render(request, 'css/layout.html')

