from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django_tables2 import RequestConfig

from polls.tables import DriverTable, TestingTable
from .models import Driver, Testing
from .forms import DriverForm, NewTestingForm


class New_Testing(generic.TemplateView):
    model = Testing
    template_name = 'polls/new_testing.html'

    def get(self, request):
        form = NewTestingForm()
        posts = Testing.objects.all()

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewTestingForm(request.POST)
        if form.is_valid():
            form.save()
            table = TestingTable(Testing.objects.all())
            RequestConfig(request).configure(table)
            # REDIRECT IS NOW AT AN INCORRECT PAGE!!
            return redirect('../acceleration', {'table': table})

        return render(request, self.template_name, {'form': form})


class new_driver(generic.TemplateView):
    # inherits froms TemplateView class
    model = Driver
    template_name = 'polls/new_driver.html'

    def get(self, request):
        form = DriverForm()
        posts = Driver.objects.all()

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            table = DriverTable(Driver.objects.all())
            RequestConfig(request).configure(table)
            return redirect('../drivers', {'table': table})
            # posts = Driver.objects.all()
            # args = {'form': form, 'posts': posts}
            # return redirect('/polls/drivers', args)

        return render(request, self.template_name, {'form': form})


def Drivers(request):
    table = DriverTable(Driver.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'polls/drivers.html', {'table': table})


def home(request):
    return render(request, 'polls/home.html')


def acceleration(request):
    # inherits froms TemplateView class
    template_name = 'polls/acceleration.html'
    table = TestingTable(Testing.objects.all())
    return render(request, template_name, {'table': table})

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# #The render() function takes the request object as its first argument,
# # a template name as its second argument and a dictionary as its optional third argument.
# # It returns an HttpResponse object of the given template rendered with the given context.
# # The context is a dictionary mapping template variable names to Python objects.
#
#
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#
# #alternative with django shortcut
# # def detail(request, question_id):
# #     question = get_object_or_404(Question, pk=question_id)
# #     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
