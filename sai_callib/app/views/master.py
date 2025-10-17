
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.models import Customer, EngineerManagerDetails, LVDTprobeMaster, LVDTprobeTrace, SettingPlugMaster, SettingPlugTrace, SettingRingMaster, SettingRingTrace


@csrf_exempt
def master(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            form_type = data.get('formType')
            form_data = data.get('formData')

            print("form_type",form_type)
            print("form_data",form_data)
            
            

            if form_type == 'setting_plug_trace':
                # Save or update setting_plug_trace table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        # Update existing record
                        obj = SettingPlugTrace.objects.get(id=row_id)
                        obj.master_name = row['masterName']
                        obj.id_no = row['idNo']
                        obj.calibration_report_no = row['calibrationReportNo']
                        obj.valid_upto = row['validUpto']
                        obj.traceability = row['traceability']
                        obj.save()
                    else:
                        # Create new record
                        SettingPlugTrace.objects.create(
                            master_name=row['masterName'],
                            id_no=row['idNo'],
                            calibration_report_no=row['calibrationReportNo'],
                            valid_upto=row['validUpto'],
                            traceability=row['traceability']
                        )

            elif form_type == 'setting_ring_trace':
                # Save or update setting_ring_trace table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = SettingRingTrace.objects.get(id=row_id)
                        obj.master_name = row['masterName']
                        obj.id_no = row['idNo']
                        obj.calibration_report_no = row['calibrationReportNo']
                        obj.valid_upto = row['validUpto']
                        obj.traceability = row['traceability']
                        obj.save()
                    else:
                        SettingRingTrace.objects.create(
                            master_name=row['masterName'],
                            id_no=row['idNo'],
                            calibration_report_no=row['calibrationReportNo'],
                            valid_upto=row['validUpto'],
                            traceability=row['traceability']
                        )

            elif form_type == 'setting_plug_master':
                # Save or update setting_plug_master table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = SettingPlugMaster.objects.get(id=row_id)
                        obj.parameter_name = row['parameterName']
                        obj.ref_size = row['refSize']
                        obj.nominal = row['nominal']
                        obj.save()
                    else:
                        SettingPlugMaster.objects.create(
                            parameter_name=row['parameterName'],
                            ref_size=row['refSize'],
                            nominal=row['nominal']
                        )

            elif form_type == 'setting_ring_master':
                # Save or update setting_ring_master table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = SettingRingMaster.objects.get(id=row_id)
                        obj.parameter_name = row['parameterName']
                        obj.ref_size = row['refSize']
                        obj.nominal = row['nominal']
                        obj.save()
                    else:
                        SettingRingMaster.objects.create(
                            parameter_name=row['parameterName'],
                            ref_size=row['refSize'],
                            nominal=row['nominal']
                        )
            elif form_type == 'lvdt_probe_master':
                # Save or update setting_ring_master table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        obj = LVDTprobeMaster.objects.get(id=row_id)
                        obj.parameter_name = row['parameterName']
                        obj.ref_size = row['refSize']
                        obj.save()
                    else:
                        LVDTprobeMaster.objects.create(
                            parameter_name=row['parameterName'],
                            ref_size=row['refSize'],
                           
                        )

           
                        
            elif form_type == 'lvdt_probe_trace':
                # Save or update setting_plug_trace table data
                for row in form_data['rows']:
                    row_id = row.get('id')  # Assuming each row has a unique ID
                    if row_id:
                        # Update existing record
                        obj = LVDTprobeTrace.objects.get(id=row_id)
                        obj.master_name = row['masterName']
                        obj.id_no = row['idNo']
                        obj.calibration_report_no = row['calibrationReportNo']
                        obj.valid_upto = row['validUpto']
                        obj.traceability = row['traceability']
                        obj.save()
                    else:
                        # Create new record
                        LVDTprobeTrace.objects.create(
                            master_name=row['masterName'],
                            id_no=row['idNo'],
                            calibration_report_no=row['calibrationReportNo'],
                            valid_upto=row['validUpto'],
                            traceability=row['traceability']
                        )

            return JsonResponse({'status': 'success', 'message': 'Data saved successfully.'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
    elif request.method == 'GET':
        
        SettingPlugTrace_value = SettingPlugTrace.objects.all()
        SettingRingTrace_value = SettingRingTrace.objects.all()
        SettingPlugMaster_value = SettingPlugMaster.objects.all()
        SettingRingMaster_value = SettingRingMaster.objects.all()
        LVDTprobeTrace_value = LVDTprobeTrace.objects.all()
        LVDTprobeMaster_value = LVDTprobeMaster.objects.all()
       

        context ={
            
            'SettingPlugTrace_value': SettingPlugTrace_value,
            'SettingRingTrace_value': SettingRingTrace_value,
            'SettingPlugMaster_value' : SettingPlugMaster_value,
            'SettingRingMaster_value' : SettingRingMaster_value,
            'LVDTprobeTrace_value':LVDTprobeTrace_value,
            'LVDTprobeMaster_value':LVDTprobeMaster_value,
            
        }

    elif request.method == 'DELETE':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            form_type = data.get('formType')
            ids_to_delete = data.get('idsToDelete', [])

            if form_type == 'tableBody-1':
                # Delete setting_plug_trace records
                SettingPlugTrace.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-2':
                # Delete setting_ring_trace records
                SettingRingTrace.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-3':
                # Delete setting_plug_master records
                SettingPlugMaster.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-4':
                # Delete setting_ring_master records
                SettingRingMaster.objects.filter(id__in=ids_to_delete).delete()

            elif form_type == 'tableBody-5':
                # Delete engineer_manager_details records
                LVDTprobeTrace.objects.filter(id__in=ids_to_delete).delete()
            elif form_type == 'tableBody-6':
                # Delete engineer_manager_details records
                LVDTprobeMaster.objects.filter(id__in=ids_to_delete).delete()

            else:
                return JsonResponse({'error': 'Invalid form type'}, status=400)

            return JsonResponse({'success': True, 'message': 'Data deleted successfully'})

        except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)

   
    
    return render(request,"app/master.html",context)

