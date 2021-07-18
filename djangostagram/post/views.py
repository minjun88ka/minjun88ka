from django.shortcuts import render
from .models import Post, Tag
from user.models import Dsuser
from .forms import WriteForm
from user.views import login_required
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class WriteView(FormView):
    template_name = 'write.html'
    form_class = WriteForm
    success_url = '/'

    def form_valid(self, form):
        tags = form.data.get('tags').split(',')

        arr_tag = []
        for tag in tags:
            tag = tag.strip()
            tag = Tag(name=tag)
            tag.save()

            arr_tag.append(tag)

        post = Post(
            dsuser=Dsuser.objects.get(id=self.request.session.get('user')),
            title=form.data.get('title'),
            content=form.data.get('content'),
            img_src=self.request.FILES['img_src']
        )
        post.save()

        for each_tag in arr_tag:
            post.tags.add(each_tag)

        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TimelineList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'timeline_list'
    paginate_by = 4

    def get_queryset(self, **kwargs):
        queryset = Post.objects.filter(dsuser=Dsuser.objects.get(id=self.request.session.get('user'))).order_by('-id')
        return queryset

@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    model = Post
    template_name = 'detail_view.html'
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_data = Post.objects.filter(id=self.kwargs['pk'], dsuser=Dsuser.objects.get(
            id=self.request.session.get('user'))).prefetch_related('tags')

        tags = query_data[0].tags.all()
        tag_name = ''
        for idx, tag in enumerate(tags):
            if str(tag) == '':
                continue

            tag_name += '#' + str(tag)

            if idx < len(tags) - 1:
                tag_name += ' '

        context['post_detail'] = query_data
        context['page'] = self.request.GET.get('page', 1)
        context['tags'] = tag_name

        return context
