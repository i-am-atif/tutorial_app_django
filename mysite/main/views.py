from django.shortcuts import render, redirect

# Here, we're using render,
# which will render/provide an actual html file/template for us.
# It will also help us to pass Python objects to that template for us to work with.

from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib import messages


# HERE WE WILL INTERACT WITH MODELS USING THE FOREIGN KEYS

# USED TO STORE A TYPE OF DATA SET INSIDE ANOTHER DATASET
# LIKE A TUTORIAL WILL COME UNDER A SERIES AND A SERIES WILL COME UNDER A CATEGORY

def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
      matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
      series_urls = {}
      for m in matching_series.all():
          part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest(
              "tutorial_published")

# USED TO RETURN THE FIRST SERIES IN THE TUTORIAL

          series_urls[m] = part_one.tutorial_slug
      return render(request=request,
                    template_name='main/category.html',
                    context={"tutorial_series": matching_series, "part_ones": series_urls})
# USED TO RETURN THE CONTENT SERIES MATCHING TO THE TUTORIAL

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
#USED TO POINT TO A SPECIFIC TUTORIAL

    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(
            tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')

# THIS USED TO FILTER  SERIES BY TUTORIAL AND CATEGORIES BY SERIES

        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        return render(request=request,
                      template_name='main/tutorial.html',
                      context={"tutorial": this_tutorial,
        "sidebar": tutorials_from_series,
        "this_tut_idx": this_tutorial_idx})
    return HttpResponse(f"'{single_slug}' Under Construction!")

# THIS WHOLE BLOCK FROM "if single_slug in tutorials:" IS USED TO ALLOW US TO CLICK ON A TUTORIAL THAT WORKS NOW.


def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={"categories": TutorialCategory.objects.all})

# MODIFIED HOMEPAGE FUNCTION TO GIVE US CATEGORIES TO ITERATE OVER RATHER THAN TUTORIALS
