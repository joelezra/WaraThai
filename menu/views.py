from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Menu, Comment
from .forms import CommentForm

# Create your views here.
class MenuList(generic.ListView):
  queryset = Menu.objects.all()
  template_name = 'menu/menu.html'
  paginate_by = 6


def menu_detail(request, pk):
  """
  Display an individual :model:`blog.Post`.

  **Context**

  ``post``
      An instance of :model:`blog.Post`.
  ``comments``
      All approved comments related to the post
  ``comment_count``
      A count of approved comments in the related post.
  ``comment_form``
      An instance of :form:`blog.CommentForm`.

  **Template:**

  :template:`blog/post_detail.html`
  """

  queryset = MenuItem.objects.all()
  item = get_object_or_404(queryset, pk=pk)
  comments = post.comments.all().order_by("-created_on")
  comment_count = post.comments.all().filter(approved=True).count()
  comment_form = CommentForm()

  if request.method == "POST":
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.author = request.user 
      comment.post = post
      comment.save()
      messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
      )

  return render(
    request,
    "menu/menu_detail.html",
    {
      "item": item,
      "comments": comments,
      "comment_count": comment_count,
      "comment_form": comment_form,
    },
  )

def comment_edit(request, pk, comment_id):
  """
  View to edit comments

  **Context**

  ``post``
    An instance of :model:`blog.Post`
  ``comment``
    A single comment related to the post.
  ``comment_form``
    An instance of :form:`blog.CommentForm`.
  """
  if request.method == "POST":
    queryset = MenuItem.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment_form = CommentForm(data=request.POST, instance=comment)

    if comment_form.is_valid() and comment.author == request.user:
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.approved = False
      comment.save()
      messages.add_message(
        request, messages.SUCCESS,
        'Comment Updated!'
      )
    else:
      messages.add_message(
        request, messages.ERROR,
        'Error updating comment!'
      )

  return HttpResponseRedirect(reverse('menu_detail', args=[pk]))

def comment_delete(request, pk, comment_id):
  """
  View to delete comments

  **Context**

  ``post``
    An instance :model:`blog.Post`
  ``comment``
    A single comment related to the post.
  """
  queryset = MenuItem.objects.all()
  post = get_object_or_404(queryset, pk=pk)
  comment = get_object_or_404(Comment, pk=comment_id)

  if comment.author == request.user:
    comment.delete()
    messages.add_message(
      request, messages.SUCCESS,
      'Comment has been deleted!'
    )
  else:
    messages.add_message(
      request, messages.ERROR,
      'You can only delete your own comments!'
    )

  return HttpResponseRedirect(reverse('menu_detail', args=[pk]))