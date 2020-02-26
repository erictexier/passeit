import os
import json
from flask_blog import db
from flask_blog.models import Post, User
ajson = "/Users/eric/42_folder/passeit/code_snippets/Python/Flask_Blog/09-Pagination/posts.json"
with open(ajson,"r") as f:
    data = json.load(f)
user = User.query.first()
for d in data:
    new_post = Post(title=d['title'], content=d['content'], user_id=user.id)
    db.session.add(new_post)
db.session.commit()
