from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django_tables2 import RequestConfig

from testing.tables import DriverTable, TestingTable
from .models import Driver, Testing
from .forms import DriverForm, NewTestingForm, AccForm


class New_Testing(generic.TemplateView):
    model = Testing
    template_name = 'testing/new_testing.html'

    def get(self, request):
        form = NewTestingForm()
        form.fields['driver'].queryset = Driver.objects.all()
        posts = Testing.objects.all()

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewTestingForm(request.POST)
        if form.is_valid():
            form.save()
            data = Testing.objects.all()[::-1][0]
            table = TestingTable(Testing.objects.all())
            RequestConfig(request).configure(table)
            event = data.event
            if event == "Acceleration":
                print('heloo')
                run = AccForm()
            else:
                print(event)
                run = AccForm()
            args = {'table': table, 'data': data, 'run': run}
            # REDIRECT IS NOW AT AN INCORRECT PAGE!!
            # USE render! If redirect display of info does not work

            return render(request, "testing/event.html", args)
        print(form.errors)
        return render(request, self.template_name, {'form': form})


class new_driver(generic.TemplateView):
    # inherits froms TemplateView class
    model = Driver
    template_name = 'testing/new_driver.html'

    def get(self, request):
        form = DriverForm()
        posts = Driver.objects.all()

        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            table_driver = DriverTable(Driver.objects.all())
            RequestConfig(request).configure(table_driver)
            return redirect('../drivers', {'table': table_driver})
            # posts = Driver.objects.all()
            # args = {'form': form, 'posts': posts}
            # return redirect('/testing/drivers', args)
        print(form.errors)
        return render(request, self.template_name, {'form': form})


def Drivers(request):
    table = DriverTable(Driver.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'testing/drivers.html', {'table': table})


def home(request):
    return render(request, 'testing/home.html')


def acceleration(request):
    # inherits froms TemplateView class
    data = Testing.objects.last()
    table = TestingTable(Testing.objects.all())
    RequestConfig(request).configure(table)
    args = {'table': table, 'data': data}
    # REDIRECT IS NOW AT AN INCORRECT PAGE!!
    # USE render! If redirect display of info does not work
    return render(request, "testing/event.html", args)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'testing/index.html', context)
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
#     return render(request, 'testing/detail.html', {'question': question})
#
# #alternative with django shortcut
# # def detail(request, question_id):
# #     question = get_object_or_404(Question, pk=question_id)
# #     return render(request, 'testing/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'testing/results.html', {'question': question})
