from django.db import models
import datetime as dt

# Create your models here.
    '''
    Image location model
    '''
    loc=(
            ("NationalPark","NationalPark"),
            ("Gymstore","Gymstore"),
            ("ParadiceLost","ParadiceLost"),
            ("TreebeadsTexas","TreebeadsTexas"),
            ("MombasaCity","MombasaCity")
            )
    location = models.CharField(max_length=120, choices = loc, null=True)

    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

    @classmethod
    def update_location(cls,loc, update):
        updated = cls.objects.filter(name=loc).update(name=update)
        return updated

    def __str__(self):
        return self.location

class Category (models.Model):
    '''
    Image category model
    '''
    cat=(
        ("Diet","Diet"),
        ("Fashion", "Fashion"),
        ("Exercise", "Exercise"),
    )

    category = models.CharField(max_length=120, choices = cat)
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    @classmethod
    def update_category(cls,cat, update):
        updated = cls.objects.filter(name=cat).update(name=update)
        return updated

    def __str__(self):
        return self.category
class Image (models.Model):
    Image= models.ImageField(upload_to= 'gallary/' )
    Image_name=models.CharField(max_length=50)
    description=models.TextField( max_length=100)
    category=models.ForeignKey("Category", max_length=50,null = True)
    location = models.ForeignKey('Location', max_length=50,null = True)
    post_date = models.DateTimeField(auto_now_add=True)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, update):
        updated = cls.objects.filter(id=id).update(image=update)
        return updated

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('-post_date')
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def searched(cls, query):
        result = cls.objects.filter(
            description__icontains=query).order_by('-post_date')
        return result


    @classmethod
    def filter_by_Category(cls, cat):
        cat = Category.objects.filter(category=cat)
        return cls.objects.filter(category=cat)

   
   

    @classmethod
    def today_pics(cls):
        today = dt.date.today()
        images = cls.objects.filter(post_date__date=today)
        return images


    @classmethod
    def filter_by_Location(cls, loc):
        loc = cls.objects.filter(location=loc)
        return cls.objects.filter(location=loc)


    @classmethod
    def search_by_Category(cls,search_term):
        cat = cls.objects.filter(category__category__icontains=search_term)
        return cat
    



