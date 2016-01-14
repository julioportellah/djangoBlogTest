from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	data={'mydata':'Hello wolrd '}
	#return render(request,'blog/index.html',data)
	return render(request,'blog/index.html',data)
#	return HttpResponse("Hello World")
# Create your views here.
#def index_troll(request):
#	return HttpResponse("Troll+LOL=Trolol")
