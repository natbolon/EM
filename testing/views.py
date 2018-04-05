from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django_tables2 import RequestConfig

from testing.tables import DriverTable, TestingTable
from .models import Driver, Testing, Acceleration, Skid_Pad
from .forms import DriverForm, NewTestingForm, AccForm, SkForm, AXForm, EnForm


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
            if data.event == "Acceleration":
                return redirect("../acceleration")

            if data.event == "Skid Pad":
                return redirect("../skidpad")
            return redirect("../event", {'data': data, 'table': table})

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
        print('POST-testing')
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


def event(request, data=None, table=None):
    if data == None:
        data = Testing.objects.all()[::-1][0]
    if table == None:
        table = TestingTable(Testing.objects.all())

    event = data.event
    if event == "Acceleration":
        run = AccForm()
        ref = 'blocks/acceleration_request.html'
    elif event == "Skid Pad":
        run = SkForm()
        ref = 'blocks/skid_pad_request.html'
    elif event == "Autocross":
        run = AXForm()
        ref = 'blocks/autocross_request.html'
    else:
        run = EnForm()
        ref = 'blocks/endurance_request.html'
    args = {'table': table, 'data': data, 'run': run, 'req': ref}
    # REDIRECT IS NOW AT AN INCORRECT PAGE!!
    # USE render! If redirect display of info does not work

    return render(request, "testing/event.html", args)


class AccelerationV(generic.TemplateView):
    model = Acceleration
    template_name = 'testing/event.html'

    def get(self, request, data=None, table=None):
        form = AccForm()
        # form.fields['params'].queryset = Testing.objects.all()[::-1][0]

        if data == None:
            data = Testing.objects.all()[::-1][0]

        if table == None:
            table = TestingTable(Testing.objects.all())
        RequestConfig(request).configure(table)
        run = AccForm()
        args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/acceleration_request.html'}
        # USE render! If redirect display of info does not work
        return render(request, "testing/event.html", args)

    def post(self, request, data=None, table=None):
        form = AccForm(request.POST)
        model_instance = form.save(commit=False)
        model_instance.params = Testing.objects.all()[::-1][0]

        if form.is_valid():
            form.save(commit=False)
            if data == None:
                data = Testing.objects.all()[::-1][0]

            if table == None:
                table = TestingTable(Testing.objects.all())
            RequestConfig(request).configure(table)
            form.save()
            run = AccForm()
            args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/acceleration_request.html'}
            # USE render! If redirect display of info does not work
            return render(request, "testing/event.html", args)

        if data == None:
            data = Testing.objects.all()[::-1][0]

        if table == None:
            table = TestingTable(Testing.objects.all())
        RequestConfig(request).configure(table)
        run = AccForm()
        args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/acceleration_request.html'}
        # USE render! If redirect display of info does not work
        return render(request, "testing/event.html", args)


def acceleration(request, data=None, table=None):
    # inherits froms TemplateView class
    if data == None:
        data = Testing.objects.all()[::-1][0]
    if table == None:
        table = TestingTable(Testing.objects.all())
    RequestConfig(request).configure(table)
    run = AccForm()
    args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/acceleration_request.html'}
    # USE render! If redirect display of info does not work
    return render(request, "testing/event.html", args)


class SKV(generic.TemplateView):
    model = Skid_Pad
    template_name = 'testing/event.html'

    def get(self, request, data=None, table=None):
        if data == None:
            data = Testing.objects.all()[::-1][0]

        if table == None:
            table = TestingTable(Testing.objects.all())
        RequestConfig(request).configure(table)
        run = SkForm()
        args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/skid_pad_request.html'}
        # USE render! If redirect display of info does not work
        return render(request, "testing/event.html", args)

    def post(self, request, data=None, table=None):
        form = SkForm(request.POST)
        model_instance = form.save(commit=False)
        model_instance.params = Testing.objects.all()[::-1][0]

        if form.is_valid():
            form.save(commit=False)
            if data == None:
                data = Testing.objects.all()[::-1][0]

            if table == None:
                table = TestingTable(Testing.objects.all())
            RequestConfig(request).configure(table)
            form.save()
            run = SkForm()
            args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/skid_pad_request.html'}
            # USE render! If redirect, display of info does not work
            return render(request, "testing/event.html", args)

        if data == None:
            data = Testing.objects.all()[::-1][0]

        if table == None:
            table = TestingTable(Testing.objects.all())
        RequestConfig(request).configure(table)
        run = SkForm()
        args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/skid_pad_request.html'}
        # USE render! If redirect, display of info does not work
        return render(request, "testing/event.html", args)
    # model = SkidPad
    # template_name = 'testing/event.html'
    #
    # def get(self, request):
    #     data = Testing.objects.all()[::-1][0]
    #     table = TestingTable(Testing.objects.all())
    #     RequestConfig(request).configure(table)
    #     run = SkForm()
    #     ref = 'blocks/skid_pad_request.html'
    #     args = {'table': table, 'data': data, 'run': run, 'req': ref}
    #     # USE render! If redirect display of info does not work
    #     return render(request, "testing/event.html", args)
    #
    # def post(self, request):
    #     form = SkForm(request.POST)
    #     model_instance = form.save(commit=False)
    #     model_instance.params = Testing.objects.all()[::-1][0]
    #     if form.is_valid():
    #         data = Testing.objects.all()[::-1][0]
    #         table = TestingTable(Testing.objects.all())
    #         RequestConfig(request).configure(table)
    #         form.save()
    #         run = SkForm()
    #         ref = 'blocks/skid_pad_request.html'
    #         args = {'table': table, 'data': data, 'run': run, 'req': ref}
    #         # USE render! If redirect display of info does not work
    #         return render(request, "testing/event.html", args)




def autocross(request, data, table):
    pass
