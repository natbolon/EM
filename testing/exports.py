from django.http import HttpResponse

from testing.models import Lap_time


def export_CSV_acc(queryset, event):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(event)
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)

    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Time"),
        smart_str(u"Lap Length"),
        smart_str(u"Date"),
        smart_str(u"Driver"),
        smart_str(u"Location"),
        smart_str(u"Params"),

        smart_str(u"Front Camber"), smart_str(u"Rear Camber"),
        smart_str(u"Front Toe"), smart_str(u"Rear Toe"),
        smart_str(u"Front Pressure"), smart_str(u"Rear Pressure"),
        smart_str(u"Front Weight"), smart_str(u"Rear Weight"),
        smart_str(u"Front Height"), smart_str(u"Rear Height"),
        smart_str(u"Roll Bar"), smart_str(u"Antiroll Bar"),

        smart_str(u"Front Wing Flap1"), smart_str(u"Front Wing Flap2"),
        smart_str(u"Rear Wing Flap1"), smart_str(u"Rear Wing Flap2"),
        smart_str(u"DRS"),

        smart_str(u"Mode"),
        smart_str(u"Continuous Current"), smart_str(u"Peak Current"),
        smart_str(u"KP Current"), smart_str(u"TI Current"),
        smart_str(u"KP Speed"), smart_str(u"TI Speed"),

        smart_str(u"Initial Temperature Inverter"), smart_str(u"Final Temperature Inverter"),
        smart_str(u"Initial Temperature Motor"), smart_str(u"Final Temperature Motor"),
        smart_str(u"Initial Temperature Battery"), smart_str(u"Final Temperature Battery"),
        smart_str(u"Initial Minimum Voltage"), smart_str(u"Final Minimum Voltage"),
        smart_str(u"Initial Temperature Pneu FL"), smart_str(u"Final Temperature Pneu FL"),
        smart_str(u"Initial Temperature Pneu FR"), smart_str(u"Final Temperature Pneu FR"),
        smart_str(u"Initial Temperature Pneu RL"), smart_str(u"Final Temperature Pneu RL"),
        smart_str(u"Initial Temperature Pneu RR"), smart_str(u"Final Temperature Pneu RR"),

    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.id),
            smart_str(obj.time),
            smart_str(obj.length_lap),
            smart_str(obj.date),
            smart_str(obj.params.driver),
            smart_str(obj.params.location),
            smart_str(obj.params),

            smart_str(obj.params.front_camber), smart_str(obj.params.rear_camber),
            smart_str(obj.params.front_toe), smart_str(obj.params.rear_toe),
            smart_str(obj.params.front_pressure), smart_str(obj.params.rear_pressure),
            smart_str(obj.params.front_weight), smart_str(obj.params.rear_weight),
            smart_str(obj.params.front_height), smart_str(obj.params.rear_height),
            smart_str(obj.params.roll_bar), smart_str(obj.params.antiroll_bar),

            smart_str(obj.params.fw_flap1_degrees), smart_str(obj.params.fw_flap2_degrees),
            smart_str(obj.params.rw_flap1_degrees), smart_str(obj.params.rw_flap2_degrees),
            smart_str(obj.params.drs),

            smart_str(obj.params.mode),
            smart_str(obj.params.cont_current_p), smart_str(obj.params.peak_current_p),
            smart_str(obj.params.kp_current), smart_str(obj.params.ti_current),
            smart_str(obj.params.kp_speed), smart_str(obj.params.ti_speed),

            smart_str(obj.temp_inv_ini), smart_str(obj.temp_inv_end),
            smart_str(obj.temp_motor_ini), smart_str(obj.temp_motor_end),
            smart_str(obj.temp_bat_ini), smart_str(obj.temp_bat_end),
            smart_str(obj.volt_min_ini), smart_str(obj.volt_min_end),

            smart_str(obj.temp_pneu_FL_ini), smart_str(obj.temp_pneu_FL_end),
            smart_str(obj.temp_pneu_FR_ini), smart_str(obj.temp_pneu_FR_end),
            smart_str(obj.temp_pneu_RL_ini), smart_str(obj.temp_pneu_RL_end),
            smart_str(obj.temp_pneu_RR_ini), smart_str(obj.temp_pneu_RR_end),

        ])
    return response


def export_CSV_skidpad(queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=skidpad.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)

    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Total Time"),
        smart_str(u"Left 1 Time"), smart_str(u"Left 2 Time"),
        smart_str(u"Right 1 Time"), smart_str(u"Right 2 Time"),

        smart_str(u"Date"),
        smart_str(u"Driver"),
        smart_str(u"Location"),
        smart_str(u"Params"),

        smart_str(u"Front Camber"), smart_str(u"Rear Camber"),
        smart_str(u"Front Toe"), smart_str(u"Rear Toe"),
        smart_str(u"Front Pressure"), smart_str(u"Rear Pressure"),
        smart_str(u"Front Weight"), smart_str(u"Rear Weight"),
        smart_str(u"Front Height"), smart_str(u"Rear Height"),
        smart_str(u"Roll Bar"), smart_str(u"Antiroll Bar"),

        smart_str(u"Front Wing Flap1"), smart_str(u"Front Wing Flap2"),
        smart_str(u"Rear Wing Flap1"), smart_str(u"Rear Wing Flap2"),
        smart_str(u"DRS"),

        smart_str(u"Mode"),
        smart_str(u"Continuous Current"), smart_str(u"Peak Current"),
        smart_str(u"KP Current"), smart_str(u"TI Current"),
        smart_str(u"KP Speed"), smart_str(u"TI Speed"),

        smart_str(u"Initial Temperature Inverter"), smart_str(u"Final Temperature Inverter"),
        smart_str(u"Initial Temperature Motor"), smart_str(u"Final Temperature Motor"),
        smart_str(u"Initial Temperature Battery"), smart_str(u"Final Temperature Battery"),
        smart_str(u"Initial Minimum Voltage"), smart_str(u"Final Minimum Voltage"),
        smart_str(u"Initial Temperature Pneu FL"), smart_str(u"Final Temperature Pneu FL"),
        smart_str(u"Initial Temperature Pneu FR"), smart_str(u"Final Temperature Pneu FR"),
        smart_str(u"Initial Temperature Pneu RL"), smart_str(u"Final Temperature Pneu RL"),
        smart_str(u"Initial Temperature Pneu RR"), smart_str(u"Final Temperature Pneu RR"),

    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.id),
            smart_str(obj.time),
            smart_str(obj.l1_time), smart_str(obj.l2_time),
            smart_str(obj.r1_time), smart_str(obj.r2_time),

            smart_str(obj.date),
            smart_str(obj.params.driver),
            smart_str(obj.params.location),
            smart_str(obj.params),

            smart_str(obj.params.front_camber), smart_str(obj.params.rear_camber),
            smart_str(obj.params.front_toe), smart_str(obj.params.rear_toe),
            smart_str(obj.params.front_pressure), smart_str(obj.params.rear_pressure),
            smart_str(obj.params.front_weight), smart_str(obj.params.rear_weight),
            smart_str(obj.params.front_height), smart_str(obj.params.rear_height),
            smart_str(obj.params.roll_bar), smart_str(obj.params.antiroll_bar),

            smart_str(obj.params.fw_flap1_degrees), smart_str(obj.params.fw_flap2_degrees),
            smart_str(obj.params.rw_flap1_degrees), smart_str(obj.params.rw_flap2_degrees),
            smart_str(obj.params.drs),

            smart_str(obj.params.mode),
            smart_str(obj.params.cont_current_p), smart_str(obj.params.peak_current_p),
            smart_str(obj.params.kp_current), smart_str(obj.params.ti_current),
            smart_str(obj.params.kp_speed), smart_str(obj.params.ti_speed),

            smart_str(obj.temp_inv_ini), smart_str(obj.temp_inv_end),
            smart_str(obj.temp_motor_ini), smart_str(obj.temp_motor_end),
            smart_str(obj.temp_bat_ini), smart_str(obj.temp_bat_end),
            smart_str(obj.volt_min_ini), smart_str(obj.volt_min_end),

            smart_str(obj.temp_pneu_FL_ini), smart_str(obj.temp_pneu_FL_end),
            smart_str(obj.temp_pneu_FR_ini), smart_str(obj.temp_pneu_FR_end),
            smart_str(obj.temp_pneu_RL_ini), smart_str(obj.temp_pneu_RL_end),
            smart_str(obj.temp_pneu_RR_ini), smart_str(obj.temp_pneu_RR_end),

        ])
    return response


def export_CSV_endurance(queryset, event):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(event)
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)

    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Time"),
        smart_str(u"Lap Length"),
        smart_str(u"Date"),
        smart_str(u"Driver"),
        smart_str(u"Location"),
        smart_str(u"Params"),

        smart_str(u"Front Camber"), smart_str(u"Rear Camber"),
        smart_str(u"Front Toe"), smart_str(u"Rear Toe"),
        smart_str(u"Front Pressure"), smart_str(u"Rear Pressure"),
        smart_str(u"Front Weight"), smart_str(u"Rear Weight"),
        smart_str(u"Front Height"), smart_str(u"Rear Height"),
        smart_str(u"Roll Bar"), smart_str(u"Antiroll Bar"),

        smart_str(u"Front Wing Flap1"), smart_str(u"Front Wing Flap2"),
        smart_str(u"Rear Wing Flap1"), smart_str(u"Rear Wing Flap2"),
        smart_str(u"DRS"),

        smart_str(u"Mode"),
        smart_str(u"Continuous Current"), smart_str(u"Peak Current"),
        smart_str(u"KP Current"), smart_str(u"TI Current"),
        smart_str(u"KP Speed"), smart_str(u"TI Speed"),

        smart_str(u"Initial Temperature Inverter"), smart_str(u"Final Temperature Inverter"),
        smart_str(u"Initial Temperature Motor"), smart_str(u"Final Temperature Motor"),
        smart_str(u"Initial Temperature Battery"), smart_str(u"Final Temperature Battery"),
        smart_str(u"Initial Minimum Voltage"), smart_str(u"Final Minimum Voltage"),
        smart_str(u"Initial Temperature Pneu FL"), smart_str(u"Final Temperature Pneu FL"),
        smart_str(u"Initial Temperature Pneu FR"), smart_str(u"Final Temperature Pneu FR"),
        smart_str(u"Initial Temperature Pneu RL"), smart_str(u"Final Temperature Pneu RL"),
        smart_str(u"Initial Temperature Pneu RR"), smart_str(u"Final Temperature Pneu RR"),

    ])

    for end in queryset:
        writer.writerow([
            smart_str(end.id),
            smart_str(' '),
            smart_str(end.length_lap),
            smart_str(end.setup_ini.date),
            smart_str(' '),
            smart_str(end.setup_ini.location)

        ])

        laps = Lap_time.objects.filter(endurance=end.id)
        n_laps = len(laps)/2
        i = 1
        for obj in laps:
            if i > n_laps:
                setup = end.setup_mid
            else:
                setup = end.setup_ini
            writer.writerow([
                smart_str(i),
                smart_str(obj.time),
                smart_str(' '),
                smart_str(' '),
                smart_str(obj.driver),
                smart_str(' '),
                smart_str(setup.id),

                smart_str(setup.front_camber), smart_str(setup.rear_camber),
                smart_str(setup.front_toe), smart_str(setup.rear_toe),
                smart_str(setup.front_pressure), smart_str(setup.rear_pressure),
                smart_str(setup.front_weight), smart_str(setup.rear_weight),
                smart_str(setup.front_height), smart_str(setup.rear_height),
                smart_str(setup.roll_bar), smart_str(setup.antiroll_bar),

                smart_str(setup.fw_flap1_degrees), smart_str(setup.fw_flap2_degrees),
                smart_str(setup.rw_flap1_degrees), smart_str(setup.rw_flap2_degrees),
                smart_str(setup.drs),

                smart_str(setup.mode),
                smart_str(setup.cont_current_p), smart_str(setup.peak_current_p),
                smart_str(setup.kp_current), smart_str(setup.ti_current),
                smart_str(setup.kp_speed), smart_str(setup.ti_speed),

                smart_str(obj.temp_inv_ini), smart_str(obj.temp_inv_end),
                smart_str(obj.temp_motor_ini), smart_str(obj.temp_motor_end),
                smart_str(obj.temp_bat_ini), smart_str(obj.temp_bat_end),
                smart_str(obj.volt_min_ini), smart_str(obj.volt_min_end),

                smart_str(obj.temp_pneu_FL_ini), smart_str(obj.temp_pneu_FL_end),
                smart_str(obj.temp_pneu_FR_ini), smart_str(obj.temp_pneu_FR_end),
                smart_str(obj.temp_pneu_RL_ini), smart_str(obj.temp_pneu_RL_end),
                smart_str(obj.temp_pneu_RR_ini), smart_str(obj.temp_pneu_RR_end),

            ])
            i += 1
    return response
