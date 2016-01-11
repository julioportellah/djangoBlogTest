models.md

In our blog
Features
========
BLog will have the following features
1.Post
2.Categories
3.Tag
4.Author

Let us make a relation between our tables
1. Post can have many categories and categories can have many posts
2.(Many to many) posts and tags
3.(ONe to many) author posts
Attributes for tables
======================
Post
====
1.Title
2.created_date
3.body
4.tags
5.categories
6.Autor

Categories
==========
1.cat_name
2.cat_description

Author
======
1.Author name
2.Author email (not mandatory)
3.Author bio

Tag
===
tag_name