from django.shortcuts import render,redirect
from . models import post,Comment
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .forms import CommentForm


context={'posts':[Comment.objects.all(),post.objects.all()]}

class postListView(LoginRequiredMixin,ListView):
    model=post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']




class postDetailView(LoginRequiredMixin,DetailView):
    model=post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
        context['title']=post.objects.last()
        return context


class postUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=['company','position','package','location','vanue','time','last_registration_date','description']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author

        
def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser

        return WrappedClass
    return wrapper

@superuser_required()
class postCreateView(LoginRequiredMixin,CreateView):
    model=post
    fields=['company','position','package','location','vanue','time','last_registration_date','description']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class postDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author


class postCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog/comment_form.html'
    context_object_name='comments'
    fields = ('comment',)

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = CommentForm(request.POST, pk)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post.objects.get(id=pk)
            new_comment.save()
            return redirect('post-detail',pk)

students=dict(Infosys=['Aman Singh','Kamal Raj','Rahul Kumar','Ajay Tomar'],
            Google=['Sanskar Choudhary','Raj Jhalaya','Ankur Sable'],
            HCL=['Viraj Singh','Ajay Thakur'],
            Microsoft=['Rishbha Patil','Heera Thakur','Rahul Tomar'])
def placed(req):
    return render(req,'blog/placed_students.html',{'title':'Placements','posts':students})
def about(req):
    return render(req,'blog/about.html')