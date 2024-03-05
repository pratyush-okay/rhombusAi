import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    # Your view logic here
    return render(request, 'index.html')  

def process_data(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file)
        first_row = df.iloc[0].to_dict()
        return JsonResponse([first_row], safe=False)

    # return JsonResponse({'error': 'Invalid request'}, status=400)
    return JsonResponse({'message': 'Request processed succesfully'})
