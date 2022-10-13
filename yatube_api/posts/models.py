from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=256,
        unique=True,
        verbose_name="group",
        help_text="group_title",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="slug",
        help_text="Group slug",
    )
    description = models.TextField(
        verbose_name="description",
        help_text="Group description",
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ("-id",)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(
        upload_to="posts/", null=True, blank=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="group",
        help_text="Group",
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("pub_date",)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("-created",)

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Follower",
        help_text="Follower",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="following",
        help_text="Following",
    )

    class Meta:
        verbose_name = "Follow"
        verbose_name_plural = "Follows"
        ordering = ("-id",)
        constraints = (
            models.UniqueConstraint(
                fields=("user", "following"),
                name="unique_user_following_pair",
            ),
            models.CheckConstraint(
                check=~models.Q(following=models.F("user")),
                name="self_following_is_not_allowed",
            )
        )

    def __str__(self):
        return f"<{self.user}:{self.following}>"

    def clean(self):
        if self.user == self.following:
            raise ValidationError("User can not follows himself.")
