from django.shortcuts import render

def post_list(request):
    return render(request, 'le_posts/post_list.html', {})