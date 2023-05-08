from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


# python manage.py shell
# Python 3.9.6 (default, Oct 18 2022, 12:41:40)
# [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from blog.models import Post
# >>> from django.contrib.auth.models import User
# >>> User.objects.all()
# <QuerySet [<User: admin>, <User: TestUser>]>
# >>> User.objects.first()
# <User: admin>
# >>> User.objects.filter(username='admin')
# <QuerySet [<User: admin>]>
# >>> User.objects.filter(username='admin').first()
# <User: admin>
# >>> user = User.objects.filter(username='admin').first()
# >>> user
# <User: admin>
# >>> user.id
# 1
# >>> user.pk
# 1
# >>> user = User.objects.get(id=1)
# >>> user
# <User: admin>
# >>> Post.objects.all()
# <QuerySet []>
# >>> post_1 = Post(title='Blog1',content='First post content!',author=user)
# >>> post_1.save()
# >>> Post.objects.all()
# <QuerySet [<Post: Post object (1)>]>
# >>> post_2 = Post(title='Blog2',content='Second post content!',author=user)
# >>> post_2.save()
# >>> post_3 = Post(title='Blog3',content='Third post content!',author_id=user.id)
# >>> post_3.save()
# >>> Post.objects.all()
# <QuerySet [<Post: Blog1>, <Post: Blog2>, <Post: Blog3>]>
# >>> post_3.content
# 'Third post content!'
# >>> post_3
# <Post: Blog3>
# >>> post_3.date_posted
# datetime.datetime(2023, 5, 4, 23, 22, 49, 683464, tzinfo=datetime.timezone.utc)
# >>> post_3.author.email
# 'admin@gmail.com'
# >>> user.post_set.all()
# <QuerySet [<Post: Blog1>, <Post: Blog2>, <Post: Blog3>]>
# >>> user.post_set.create(title='Blog 4',content='Fourth content!')
# <Post: Blog 4>
# >>> user.post_set.all()
# <QuerySet [<Post: Blog1>, <Post: Blog2>, <Post: Blog3>, <Post: Blog 4>]>
# >>> Post.objects.all()
# <QuerySet [<Post: Blog1>, <Post: Blog2>, <Post: Blog3>, <Post: Blog 4>]>


# Adding dummy data
# python manage.py shell
# import json
# from blog.models import Post
# with open('posts.json') as f:
#     posts_json = json.load(f)
# for post in posts_json:
#     post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
#     post.save()

# Adding pagination
# from django.core.paginator import Paginator

# posts = ['1','2','3','4','5']
# p = Paginator(posts,2)
# p.num_pages
# for page in p.page_range:
#     print(page)
# p1 = p.page(1)
# p1
# p1.number
# p1.object_list
# p1.has_previous
# p1.has_next
# p1.next_page_number
