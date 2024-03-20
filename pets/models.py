from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Student(models.Model):
    # No need for id, it's automatically built in
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    num_cats = models.IntegerField(default=0)

    class Meta:
        ordering = ["last_name"]

    def __str__(self): return self.first_name + ' ' + self.last_name


class Cat(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.owner.num_cats += 1
            self.owner.save()
        super(Cat, self).save(*args, **kwargs)



    def delete(self, *args, **kwargs):
        print("Kill cat")
        self.owner.num_cats -= 1
        self.owner.save()
        super(Cat, self).delete(*args, **kwargs)

    class Meta:
        ordering = ["name"]

    def __str__(self): return self.name

# DJango docs says overriding delete() won't always work: https://docs.djangoproject.com/en/dev/topics/db/models/#overriding-model-methods So we are using signals instead
@receiver(post_delete, sender=Cat)
def update_num_cats_on_delete(sender, instance, **kwargs):
    instance.owner.num_cats -= 1
    instance.owner.save()