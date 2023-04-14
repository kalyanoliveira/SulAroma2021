from django.shortcuts import render
# Import app-level models.py classes to interact with database
from .models import blogPost, blogComment
# Other Django related imports
from django import forms 
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# Django comment form. Fields: author, body
# widget=forms.TextInput(attrs={}) adds bootstrap classes to forms
class newCommentForm(forms.Form):
    comFormAuthor = forms.CharField(label="Nome",max_length=64,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome'}))
    comFormBody = forms.CharField(label="Comentário",max_length=1024,widget=forms.Textarea(attrs={'class': 'form-control','rows':'3', 'placeholder':'Escreva seu comentário aqui'}))

# Index function that is called by app-level urls.py
def index(request, pIntVariable):
    if request.method == "POST": # Is user submitting a comment form?
        submittedCommentForm = newCommentForm(request.POST)
        if submittedCommentForm.is_valid(): # Server-side validation
            # Split saved data into variables
            tempAuthor = submittedCommentForm.cleaned_data["comFormAuthor"]
            tempBody = submittedCommentForm.cleaned_data["comFormBody"]
            tempPostID = request.POST["subComFormPostID"] # Save pk of blogPost to which comment belongs
            # Save comment
            bc = blogComment(author=tempAuthor, body=tempBody, post_id=tempPostID)
            bc.save()
            # Redirect to URL corresponding to blog/views.py index function (which is defined in blog/urls.py). Uses pIntVariable = pk of blogPost to which comment belongs
            return HttpResponseRedirect(reverse("blog:index", args=(tempPostID,)))
        else:
            # Save pk of blogPost to which comment belongs
            tempPostID = request.POST["subComFormPostID"]
            # HttpResponse of blog/index.html
            return render(request, "blog/index.html",{
                'pageName':'Blog',
                'blogPosts' : blogPost.objects.all().order_by('created_on'), # Array of blog posts
                'form': submittedCommentForm, # Uses submitted comment form
                'displayedPostID' : tempPostID, # Pk of blogPost to which comment belongs
                'formError': 'Erro na publicação. Favor checar se todos campos de entrada estão preenchidos, e checar número de caracteres de cada campo de entrada' # Error message
            })
    else: # User is not submitting a comment form. I.e., normal response of blog posts' webpage
        # HttpResponse of blog/index.html
        return render(request, "blog/index.html", {
            'pageName':'Blog',
            'blogPosts' : blogPost.objects.all().order_by('created_on'), # Array of blog posts
            'form': newCommentForm(), # Uses blank comment form
            'displayedPostID': pIntVariable, # URL <int:pIntVariable> (from blog/urls.py definition)
        })