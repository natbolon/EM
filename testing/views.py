from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from django_tables2.templatetags.django_tables2 import render_table

from testing.resources import DriverResource, AccelerationResource, AutoXResource, SkidPadResource
from testing.tables import DriverTable, TestingTable, AccelerationTable, SkidPadTable, AutoXTable, EnduranceTable
from .models import Driver, Testing, Acceleration, Skid_Pad, AutoX, Endurance
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

            elif data.event == "Skid Pad":
                return redirect("../skidpad")

            elif data.event == "Autocross":
                return redirect("../autocross")

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


class Drivers(generic.TemplateView):
    model = Driver
    template_name = 'testing/drivers.html'

    def get(self, request):
        table = DriverTable(Driver.objects.all())
        RequestConfig(request).configure(table)

        export_format = request.GET.get('_export', None)
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response('table.{}'.format(export_format))

        return render(request, self.template_name, {'table': table})

    def post(self, request):
        return self.export(request)

    def export(self, request):
        person_resource = DriverResource()
        dataset = person_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="drivers.xls"'
        return response


class Old_Testing_Class(generic.TemplateView):
    template_name = 'testing/old_testing.html'

    def get(self, request, *args, **kwargs):
        event = kwargs['event']
        model, _, table = self.check_model(event)

        RequestConfig(request).configure(table)
        return render(request, self.template_name, {'table': table, 'event': event})

    def post(self, request, **kwargs):
        event = kwargs['event']
        model, model_rs, table = self.check_model(event)
        return self.export(event, model_rs)

    def check_model(self, event):
        if event == "acceleration":
            model = Acceleration
            model_rs = AccelerationResource()
            info = Acceleration.objects.all()
            table = AccelerationTable(info)

        elif event == "skidpad":
            model = Skid_Pad
            model_rs = SkidPadResource()
            info = Skid_Pad.objects.all()
            table = SkidPadTable(info)

        elif event == "autocross":
            model = AutoX
            model_rs = AutoXResource()
            info = AutoX.objects.all()
            table = AutoXTable(info)

        else:
            model = Endurance
            model_rs = AccelerationResource()
            info = Endurance.objects.all()
            table = EnduranceTable(info)

        return model, model_rs, table

    def export(self, event, model_rs):
        model_resource = model_rs
        dataset = model_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        filename = '{}.xls'.format(event)
        response['Content-Disposition'] = 'attachment; filename={fn}'.format(fn=filename)
        return response





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


class AutoXV(generic.TemplateView):
    model = AutoX
    template_name = 'testing/event.html'

    def get(self, request, data=None, table=None):
        if data == None:
            data = Testing.objects.all()[::-1][0]

        if table == None:
            table = TestingTable(Testing.objects.all())
        RequestConfig(request).configure(table)
        run = AXForm()
        args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/autocross_request.html'}
        # USE render! If redirect display of info does not work
        return render(request, "testing/event.html", args)

    def post(self, request, data=None, table=None):
        form = AXForm(request.POST)
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
            run = AXForm()
            args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/autocross_request.html'}
            # USE render! If redirect, display of info does not work
            return render(request, "testing/event.html", args)

        if data == None:
            data = Testing.objects.all()[::-1][0]

        if table == None:
            table = TestingTable(Testing.objects.all())
        RequestConfig(request).configure(table)
        run = AXForm()
        args = {'table': table, 'data': data, 'run': run, 'req': 'blocks/autocross_request.html'}
        # USE render! If redirect, display of info does not work
        return render(request, "testing/event.html", args)
