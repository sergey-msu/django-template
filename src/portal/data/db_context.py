from pathlib import Path

from .models.project import Project
from .models.post import Post
from .models.comment import Comment


class DataContext:
    def __init__(self, scripts_folder='scripts/'):
        base_dir = Path(__file__).resolve().parent
        self.scripts_folder = Path.joinpath(base_dir, scripts_folder)


    def get_all_projects(self):
        # avoid of select *, use pagination!
        return Project.objects.all()


    def get_project_by_id(self, id):
        return Project.objects.get(pk=id)


    def get_all_posts(self):
        # avoid of select *, use pagination!
        return Post.objects.all().order_by("-created_on")


    def get_posts_by_category(self, category):
        # avoid of select *, use pagination!
        return Post.objects.filter(categories__name__contains=category) \
                           .order_by("-created_on")

    def get_post_by_id(self, id):
        return Post.objects.get(pk=id)


    def get_comments_by_post(self, post):
        return Comment.objects.filter(post=post)


    def get_most_commented_posts(self, max_cnt=2):
        query = self.query('most_commented_posts', max_cnt=max_cnt)
        result = Post.objects.raw(query)
        
        posts = []
        for row in result:
            post = self.get_post_by_id(row.pk)
            posts.append(post)

        return posts



    def query(self, name, **kwargs):
        with open(f'{self.scripts_folder}/{name}.sql', 'r') as f:
            return f.read().format(**kwargs)



DATA = DataContext()
