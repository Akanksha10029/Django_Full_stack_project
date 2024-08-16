from django.shortcuts import render
from .models import Review
from .forms import ReviewForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'review_list.html', {'reviews' : reviews})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form' : form})


def review_edit(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user= request.user)
    if request.method =='POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request,'review_form.html',{'form': form})
            
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user= request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request,'review_confirm_delete.html',{'review': review})