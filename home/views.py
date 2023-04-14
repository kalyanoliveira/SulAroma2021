from django.shortcuts import render
# Import blog models.py classes to interact with database
from blog.models import blogPost
# Import home models.py classes to interact with database
from .models import carouselSlide
# Import random for generation of random integer
import random


# Create your views here.
def index(request):

    if carouselSlide.objects.exists(): # If carousel slide(s) exist(s)
        carouselSlides = carouselSlide.objects.all() # Carousel slides data

        if blogPost.objects.exists(): # If blog post(s) exist(s)
            latestBlogPost = blogPost.objects.all().order_by('-created_on').first() # Latest blog post data

            if blogPost.objects.count() > 1: # If more than one blog post exists
                notLatestPosts = list(blogPost.objects.exclude(pk=latestBlogPost.id)) # List of all posts but the latest
                randomBlogPost = random.choice(notLatestPosts) # Sampling above list for one random post / random blog post data
                # HttpResponse of home/index.html
                return render(request, "home/index.html", {
                    'pageName':'Home',
                    'latestBlogPost': latestBlogPost,
                    'randomBlogPost': randomBlogPost,
                    'carouselSlides': carouselSlides,
                })

            else: # If only one blog post exists
                # HttpResponse of home/index.html
                return render(request, "home/index.html", {
                    'pageName':'Home',
                    'latestBlogPost': latestBlogPost,
                    'carouselSlides': carouselSlides,
                })

        else: # If no blog posts exist
            # HttpResponse of home/index.html
            return render(request, "home/index.html", {
                'pageName':'Home',
                'carouselSlides': carouselSlides,
                'noPosts':'string',
            })

    else: # If no carousel slides exist
        if blogPost.objects.exists(): # If blog post(s) exist(s)
            latestBlogPost = blogPost.objects.all().order_by('-created_on').first() # Latest blog post data

            if blogPost.objects.count() > 1: # If more than one blog post exists
                notLatestPosts = list(blogPost.objects.exclude(pk=latestBlogPost.id)) # List of all posts but the latest
                randomBlogPost = random.choice(notLatestPosts) # Sampling above list for one random post / random blog post data
                # HttpResponse of home/index.html
                return render(request, "home/index.html", {
                    'pageName':'Home',
                    'latestBlogPost': latestBlogPost,
                    'randomBlogPost': randomBlogPost,
                })

            else: # If only one blog post exists
                # HttpResponse of home/index.html
                return render(request, "home/index.html", {
                    'pageName':'Home',
                    'latestBlogPost': latestBlogPost,
                })

        else: # If no blog posts exist
            # HttpResponse of home/index.html
            return render(request, "home/index.html", {
                'pageName':'Home',
                'noPosts':'string',
            })