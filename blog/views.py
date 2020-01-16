from django.shortcuts import render
from django.views import generic
from blog.models import Post
from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Post, PostCategory

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/allblogs.html'
    paginate_by = 3


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    query = Post.objects.filter(status=1)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'query':query})


def about_view(request):
    template_name = 'about.html'
    context = {}
    return render(request, template_name, context)


def service_view(request):
    template_name = 'services.html'
    context = {}
    return render(request, template_name, context)


class SearchPostCategoryView(ListView):

    template_name = "blog/allblogs.html"

    def get_queryset(self):
        model = Post

        self.category = get_object_or_404(
            PostCategory, name=self.kwargs['category'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category'] = self.category
        return context

