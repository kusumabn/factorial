from django.shortcuts import render
def home(request):
    n1 = 5
    result = 1
    for i in range(1, n1 + 1):
        result *= i
        square = n1 ** 2
    return render(request, 'app51/index.html', {'factorial': result, 'number': n1, 'square': square})

