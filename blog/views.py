from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.models import User
from .forms import PostForm, ProfileUpdateForm, UserUpdateForm
from .models import Post, Profile


@login_required()
def profile(request, pk):
    user_profile = Profile.objects.get(id=pk)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', pk=request.user.profile.id)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'profile': user_profile,
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'blog/user_profile.html', context)


def add_post(request):
    form = PostForm
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = Post.objects.create(
                title=request.POST['title'],
                author=User.objects.get(id=request.user.id),
                content=request.POST['content']
            )
            obj.save()
            return redirect('home')
        else:
            error = 'Enter a correct data'

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/add_post.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'



