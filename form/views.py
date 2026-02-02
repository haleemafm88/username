from django.shortcuts import render

def result(request):
    
    username = request.GET.get('username')
    
    all_data = request.GET

    return render(request, 'result.html', {
        'username': username,
        'all_data': all_data
    })

