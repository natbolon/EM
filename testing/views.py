
from django.db.models import Avg, Min, Max
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django_tables2 import RequestConfig
from django_tables2.export import TableExport

from testing.resources import DriverResource, AccelerationResource, AutoXResource, SkidPadResource, TestingResource, \
    EnduranceResource, LapsResource
from testing.tables import DriverTable, TestingTable, AccelerationTable, SkidPadTable, AutoXTable, EnduranceTable, \
    LapTable
from .models import Driver, Testing, Acceleration, Skid_Pad, AutoX, Endurance, Lap_time
from .forms import DriverForm, NewTestingForm, AccForm, SkForm, AXForm, ResultsForm, Lap, LapTimeForm


class New_Testing(generic.TemplateView):
    model = Testing
    template_name = 'testing/new_testing.html'

    def get(self, request):
        obj = Testing.objects.all()
        if len(obj) == 0:
            form = NewTestingForm()
        else:
            data = obj[::-1][0]
            form = NewTestingForm(initial=model_to_dict(data))

        drivers = Driver.objects.all()
        if len(drivers) == 0:
            return redirect('../new_driver')

        form.fields['driver'].queryset = drivers
        args = {'form': form, }
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewTestingForm(request.POST)
        if form.is_valid():
            form.save()
            obj = Testing.objects.all()
            data = obj[::-1][0]
            table = TestingTable(obj)
            RequestConfig(request).configure(table)
            if data.event == "Acceleration":
                return redirect("../acceleration")

            elif data.event == "Skid Pad":
                return redirect("../skidpad")

            elif data.event == "Autocross":
                return redirect("../autocross")

            elif data.event == "Endurance":
                return redirect("../endurance")

            return redirect("../event")

        print(form.errors)
        return render(request, self.template_name, {'form': form})


class New_Driver(generic.TemplateView):
    model = Driver
    template_name = 'testing/new_driver.html'

    def get(self, request):
        form = DriverForm()

        args = {'form': form, }
        return render(request, self.template_name, args)

    def post(self, request):
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            table_driver = DriverTable(Driver.objects.all())
            RequestConfig(request).configure(table_driver)
            return redirect('../drivers', {'table': table_driver})

        return render(request, self.template_name, {'form': form})


class Drivers(generic.TemplateView):
    model = Driver
    template_name = 'testing/drivers.html'

    def get(self, request):
        table = DriverTable(Driver.objects.all())
        RequestConfig(request).configure(table)

        export_format = request.GET.get('_export', )
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


class Old_Testing(generic.TemplateView):
    template_name = 'testing/old_testing.html'

    def get(self, request, *args, **kwargs):
        event = kwargs['event']
        model, _, table = self.check_model(event)
        button = 'blocks/best_conf.html'
        if event not in ['acceleration', 'skidpad', 'autocross']:
            button = 'endurance/nothing.html'

        RequestConfig(request).configure(table)
        return render(request, self.template_name, {'table': table, 'event': event, 'button': button})

    def post(self, request, **kwargs):
        event = kwargs['event']

        if 'export_csv' in request.POST:
            model, model_rs, table = self.check_model(event)
            return self.export(event, model_rs)
        else:
            return best_results(request, event)

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

        elif event == "endurance":
            model = Endurance
            model_rs = EnduranceResource()
            info = Endurance.objects.all()
            table = EnduranceTable(info)

        elif event == "laps":
            model = Lap_time
            model_rs = LapsResource()
            info = Lap_time.objects.all()
            table = LapTable(info)

        else:
            model = Testing
            model_rs = TestingResource()
            info = Testing.objects.all()
            table = TestingTable(info)

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


def check_event(event):
    if event == "acceleration":
        obj = Testing.objects.filter(event="Acceleration")
        run = AccForm()
        stat_obj = Acceleration.objects.all()
        req = 'blocks/acceleration_request.html'

    elif event == "skidpad":
        obj = Testing.objects.filter(event="Skid Pad")
        run = SkForm()
        stat_obj = Skid_Pad.objects.all()
        req = 'blocks/skid_pad_request.html'

    else:
        obj = Testing.objects.filter(event="Autocross")
        run = AXForm()
        stat_obj = AutoX.objects.all()
        req = 'blocks/autocross_request.html'

    return obj, run, stat_obj, req


def event_get(request, event):
    obj, run, stat_obj, req = check_event(event)
    if len(obj) == 0:
        return None

    data = obj[::-1][0]
    table = TestingTable(obj)
    RequestConfig(request).configure(table)
    if event == "skidpad":
        stat = statistics_sk(stat_obj)
        stat_view = 'blocks/statistics_sk.html'
    else:
        stat = statistics(stat_obj)
        stat_view = 'blocks/statistics.html'

    args = {'table': table, 'data': data, 'run': run, 'req': req,
            'res': ResultsForm(), 'stat': stat, 'stat_view': stat_view}

    return args


class AccelerationV(generic.TemplateView):
    model = Acceleration
    template_name = 'testing/event.html'

    def get(self, request, data=None, table=None):
        args = event_get(request, 'acceleration')
        if not args:
            return redirect('../new_testing')

        return render(request, "testing/event.html", args)

    def post(self, request):
        form = AccForm(request.POST)
        model_instance = form.save(commit=False)
        model_instance.params = Testing.objects.all()[::-1][0]

        if form.is_valid():
            form.save()

            args = event_get(request, 'acceleration')
            if not args:
                return redirect('../new_testing')

            return render(request, "testing/event.html", args)

        args = event_get(request, 'acceleration')
        if not args:
            return redirect('../new_testing')
        return render(request, "testing/event.html", args)


class SKV(generic.TemplateView):
    model = Skid_Pad
    template_name = 'testing/event.html'

    def get(self, request):

        args = event_get(request, 'skidpad')
        if not args:
            return redirect('../new_testing')

        return render(request, "testing/event.html", args)

    def post(self, request, data=None, table=None):
        form = SkForm(request.POST)
        model_instance = form.save(commit=False)
        model_instance.params = Testing.objects.all()[::-1][0]

        if form.is_valid():
            form.save()
            args = event_get(request, 'skidpad')
            if not args:
                return redirect('../new_testing')

            return render(request, "testing/event.html", args)

        args = event_get(request, 'skidpad')
        if not args:
            return redirect('../new_testing')

        return render(request, "testing/event.html", args)


class AutoXV(generic.TemplateView):
    model = AutoX
    template_name = 'testing/event.html'

    def get(self, request, **kwargs):
        args = event_get(request, 'autocross')
        if not args:
            return redirect('../new_testing')

        return render(request, "testing/event.html", args)

    def post(self, request):
        form = AXForm(request.POST)
        model_instance = form.save(commit=False)
        model_instance.params = Testing.objects.all()[::-1][0]

        if form.is_valid():
            form.save()
            args = event_get(request, 'autocross')
            if not args:
                return redirect('../new_testing')

            return render(request, "testing/event.html", args)

        args = event_get(request, 'autocross')
        if not args:
            return redirect('../new_testing')

        return render(request, "testing/event.html", args)


class EnduranceV(generic.TemplateView):
    model = Endurance
    template_name = 'testing/event.html'

    def get(self, request, **kwargs):
        obj = Testing.objects.filter(event="Endurance")
        if not obj:
            return redirect('../new_testing')
        data = obj[::-1][0]

        lap_form = Lap()
        info_req = "endurance/length_request.html"

        args = {'table': None, 'data': data, 'run': lap_form, 'info_req': info_req,
                'res': None, 'stat': None, 'stat_view': 'endurance/nothing.html', 'res_view': 'endurance/nothing.html'}

        return render(request, "endurance/endurance.html", args)

    def post(self, request):
        obj = Testing.objects.filter(event="Endurance")
        data = obj[::-1][0]
        table = TestingTable(obj)
        RequestConfig(request).configure(table)

        if 'SUBMIT_1' in request.POST:
            form = Lap(request.POST)
            if form.is_valid():
                data_lap = form.cleaned_data
                length = float(data_lap.get('length'))
                laps = round(11000 / length)

                return create_endurance(request, laps, length, data, table)

        elif 'SUBMIT_TIME' in request.POST:
            return create_lap(request, data, table)

        elif 'SUBMIT_SETUP' in request.POST:
            end_form = NewTestingForm(request.POST)
            if end_form.is_valid():
                end_form.save()

            instance = Endurance.objects.all()[::-1][0]

            obj = Testing.objects.filter(event="Endurance")
            data = obj[::-1][0]
            table = TestingTable(obj)
            RequestConfig(request).configure(table)

            instance.__setattr__('setup_mid', data)
            instance.save()

            run = LapTimeForm()
            info_req = "endurance/endurance_request.html"

            stat = statistics(None)
            stat_view = 'blocks/statistics.html'
            args = {'table': table, 'data': data, 'run': run, 'info_req': info_req,
                    'res': ResultsForm(), 'stat': stat, 'stat_view': stat_view, 'res_view': 'blocks/results.html'}
            # USE render! If redirect display of info does not work
            return render(request, "endurance/endurance.html", args)


def create_endurance(request, laps, length, data, table):
    instance = Endurance()
    instance.length_lap = length
    instance.number_laps = laps
    instance.setup_ini = data
    instance.save()

    run = LapTimeForm()
    info_req = "endurance/endurance_request.html"

    stat = statistics(None)
    stat_view = 'blocks/statistics.html'
    args = {'table': table, 'data': data, 'run': run, 'info_req': info_req,
            'res': ResultsForm(), 'stat': stat, 'stat_view': stat_view, 'res_view': 'blocks/results.html'}
    # USE render! If redirect display of info does not work
    return render(request, "endurance/endurance.html", args)


def create_lap(request, data, table):
    form = LapTimeForm(request.POST)
    lap_instance = form.save(commit=False)
    lap_instance.driver = data.driver
    if form.is_valid():
        form.save()
        endurance = Endurance.objects.all()[::-1][0]
        endurance.time_lap.add(lap_instance)
        endurance.save()

        if len(endurance.time_lap.all()) == endurance.number_laps:
            if not endurance.setup_mid:
                form_setup = NewTestingForm(initial=model_to_dict(data))
                form_setup.fields['driver'].queryset = Driver.objects.all()

                stat = statistics(Lap_time.objects.filter(endurance__id=endurance.id))
                stat_view = 'blocks/statistics.html'

                args = {'table': table, 'data': data, 'run': None, 'info_req': 'endurance/nothing.html',
                        'form': form_setup, 'stat': stat, 'stat_view': stat_view,
                        'res_view': 'blocks/new_testing_form.html'}
                # USE render! If redirect display of info does not work
                return render(request, "endurance/endurance.html", args)
            else:
                return redirect("../old_testing/endurance")

        elif len(endurance.time_lap.all()) == 2 * endurance.number_laps:
            return redirect("../old_testing/endurance")

        else:
            run = LapTimeForm()
            info_req = "endurance/endurance_request.html"

            stat = statistics(Lap_time.objects.filter(endurance__id=endurance.id))
            stat_view = 'blocks/statistics.html'
            args = {'table': table, 'data': data, 'run': run, 'info_req': info_req,
                    'res': ResultsForm(), 'stat': stat, 'stat_view': stat_view, 'res_view': 'blocks/results.html'}
            # USE render! If redirect display of info does not work
            return render(request, "endurance/endurance.html", args)


def statistics(obj):
    if not obj:
        avg = '-'
        min = '-'
        runs = 0
        return list((avg, min, runs))

    min = float(obj.aggregate(Min('time'))['time__min'])
    avg = float(obj.aggregate(Avg('time'))['time__avg'])

    min = float("{0:.3f}".format(min))
    avg = float("{0:.3f}".format(avg))
    runs = obj.count()
    return list((avg, min, runs))


def statistics_sk(obj):
    if not obj:
        return list(('-', '-', 0, '-', '-', '-', '-'))

    min_l2 = float(obj.aggregate(Min('l2_time'))['l2_time__min'])
    min_r2 = float(obj.aggregate(Min('r2_time'))['r2_time__min'])
    min_time1 = Skid_Pad.objects.filter(l2_time=min_l2)[0].time
    min_time2 = Skid_Pad.objects.filter(r2_time=min_r2)[0].time
    minimum = min(min_time1, min_time2)

    avg_l2 = float(obj.aggregate(Avg('l2_time'))['l2_time__avg'])
    avg_r2 = float(obj.aggregate(Avg('r2_time'))['r2_time__avg'])
    avg = (avg_l2 + avg_r2)

    runs = obj.count()
    return list((float("{0:.3f}".format(avg)), float("{0:.3f}".format(minimum)), runs,
                 float("{0:.3f}".format(avg_l2)), float("{0:.3f}".format(min_l2)),
                 float("{0:.3f}".format(avg_r2)), float("{0:.3f}".format(min_r2))))


def best_results(request, event):
    if event == "skidpad":
        stats = statistics_sk(Skid_Pad.objects.all())
        runs = stats[2]
        if runs == 0:
            return redirect('../{}'.format(event))
        else:
            min_l = stats[4]
            min_r = stats[6]
            min_time1 = Skid_Pad.objects.filter(l2_time=min_l)[0]
            min_time2 = Skid_Pad.objects.filter(r2_time=min_r)[0]
            if min_time1.time < min_time2.time:
                data = min_time1
            else:
                data = min_time2

            return render(request, 'testing/best_results.html', {'data': data, })

    else:
        if event == "acceleration":
            objs = Acceleration.objects

        elif event == "autocross":
            objs = AutoX.objects

        else:
            objs = Lap_time.objects

        stats = statistics(objs.all())
        if stats[2] == 0:
            # Redirects to New Testing Session as there are no results about it.
            return redirect('../{}'.format(event))
        else:
            min_time = stats[1]
            data = objs.filter(time=min_time)[0]

            return render(request, 'testing/best_results.html', {'data': data, })
