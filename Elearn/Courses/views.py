from django.shortcuts import render
from .forms import RecommendForm

def recommend(request):
	form=RecommendForm(request.POST)
	if form.is_valid():
		rform=form.save(commit=False)
		rform.save()
		return redirect('home')
	else:
		form=RecommendForm()
	return render(request,'recommend.html',{'form':form})
