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
                return acceleration(request, data, table)
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


def acceleration(request, data=None, table=None):
    # inherits froms TemplateView class
    if data == None:
        data = Testing.objects.all()[::-1][0]
    if table == None:
        table = TestingTable(Testing.objects.all())
    RequestConfig(request).configure(table)
    run = AccForm()
    args = {'table': table, 'data': data, 'run': run}
    print('correct path')
    # USE render! If redirect display of info does not work
    return render(request, "testing/event.html", args)

