import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#user: basic data when user creates their account + what makes their account
#username, email, password, posts, followers, following
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    posts = Column(Integer, ForeignKey("posts.id"))
    followers = Column(Integer, ForeignKey("followers.id"))
    following = Column(Integer, ForeignKey("following.id"))
    posts = relationship("Posts")
    followers = relationship("Followers")
    following = relationship("Following")

#posts: basic post structure, photos + reels
#content (photo, video, reel), location, likes/views, timestamp, comments
#not sure how to describe content, so i'll leave it as a string, since it includes a photo/video(jpg/mp4)
class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey("user.id"))
    photo_video = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    likes = Column(Integer, ForeignKey("likes.id"))
    timestamp = Column(String(250), nullable=False)
    comment = Column(String(250), ForeignKey("comment.id"))
    likes = relationship("Likes")
    comment = relationship("Comment")
    user = relationship("User")

#followers: should contain a list of followers by username, and be connected to every user
#so, followers will call the user table as well
class Followers(Base):
    __tablename__= "followers"
    id = Column(Integer, primary_key=True)
    followers = Column(String(250), ForeignKey("user.id"))
    user = relationship("User")

#following: same idea as followers
class Following(Base):
    __tablename__ = "following"
    id = Column(Integer, primary_key=True)
    following = Column(String(250), ForeignKey("user.id"))
    user = relationship("User")

#likes: same idea as followers, but focusing on the likes list for every piece of media
class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    poster_id = Column(Integer, ForeignKey("posts.id"))
    liker = Column(String(250), ForeignKey("user.id"))
    user = relationship("User")
    posts = relationship("Posts")

#comment: same idea as likes, but includes the text description
class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    poster_id = Column(String(250), ForeignKey("posts.id"))
    description = Column(String(250), nullable = False)
    poster = Column(String(250), ForeignKey("user.id"))
    user = relationship("User")
    posts = relationship("Posts")

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
