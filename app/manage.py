from app import app, db, migrate
from app.models import User, Post, Comment, Tag

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post = Post, Comment=Comment, Tag=Tag, migrate=migrate)