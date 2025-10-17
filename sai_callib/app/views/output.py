from datetime import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render
from app.models import LVDTprobeMaster, LVDTprobeTrace, SettingPlugMaster, SettingPlugTrace, SettingRingMaster, SettingRingTrace,MainCalibration, CalibrationEquipment, CalibrationResult



def output(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            print("Data received from the frontend:", data)

              # Enhanced date conversion function to handle multiple formats
            def convert_to_date(date_str):
                for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
                    try:
                        return datetime.strptime(date_str, fmt).date()
                    except (ValueError, TypeError):
                        continue
                return None  # Return None if the date format is invalid or empty

            # Extract and convert dates to correct format
            main_calibration_data = {
                'certificate_num': data.get('certificate_num', ''),
                'work_order': data.get('work_order', ''),
                'date_of_issue': convert_to_date(data.get('date_of_issue', '')),
                'date_of_calibration': convert_to_date(data.get('date', '')),
                'next_calibration': convert_to_date(data.get('next_calibration', '')),
                'customer_address': data.get('customer_address', ''),
                'range': data.get('range', ''),
                'least_count': data.get('least_count', ''),
                'identification_no': data.get('identification_no', ''),
                'si_no': data.get('si_no', ''),
                'make': data.get('make', ''),
                'customer_ref': data.get('customer_ref', ''),
                'date_calib': convert_to_date(data.get('date_calib', '')),
                'date_of_receipt': convert_to_date(data.get('date_of_receipt', '')),
                'calib_procedure_no': data.get('calib_procedure_no', ''),
                'location': data.get('location', ''),
                'inward_no': data.get('inward_no', ''),
                'environment': data.get('environment', ''),
                'uncertainty': data.get('uncertainity', ''),
                'calib_engineer': data.get('calib_engineer', ''),
                'quality_manager': data.get('quality_manager', ''),
            }

            # Create and save the main calibration record
            main_calibration = MainCalibration.objects.create(**main_calibration_data)

            # Save calibration equipment data
            for equipment in data.get('tableData', []):
                CalibrationEquipment.objects.create(
                    main_calibration=main_calibration,
                    sr_no=equipment.get('sr_no'),
                    master_name=equipment.get('master_name', ''),
                    id_no=equipment.get('id_no', ''),
                    calibration_no=equipment.get('calibration_no', ''),
                    valid_upto=equipment.get('valid_upto', ''),
                    traceability=equipment.get('traceability', ''),
                )

            # Save calibration results data
            for result_set in data.get('calibrationOutputTable', []):
                container_id = result_set.get('containerId')
                for result in result_set.get('rows', []):
                    CalibrationResult.objects.create(
                        main_calibration=main_calibration,
                        container_id=container_id,
                        parameter=result.get('parameter', ''),
                        ref_size=result.get('ref_size', ''),
                        nominal=result.get('nominal', ''),
                        observation_size=result.get('observation_size', ''),
                        error=result.get('error', ''),
                    )

            # Send a success response back to the JavaScript
            return JsonResponse({'status': 'success', 'message': 'Data saved successfully.'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data.'}, status=400)
    
    elif request.method == 'GET':
        # Fetch existing values for display in the template
        SettingPlugTrace_value = SettingPlugTrace.objects.all()
        SettingRingTrace_value = SettingRingTrace.objects.all()
        SettingPlugMaster_value = SettingPlugMaster.objects.all()
        SettingRingMaster_value = SettingRingMaster.objects.all()
        LVDTprobeTrace_value= LVDTprobeTrace.objects.all()
        LVDTprobeMaster_value = LVDTprobeMaster.objects.all()


        context = {
            'SettingPlugTrace_value': SettingPlugTrace_value,
            'SettingRingTrace_value': SettingRingTrace_value,
            'SettingPlugMaster_value': SettingPlugMaster_value,
            'SettingRingMaster_value': SettingRingMaster_value,
            'LVDTprobeTrace_value':LVDTprobeTrace_value,
            'LVDTprobeMaster_value':LVDTprobeMaster_value
        }
        return render(request, "app/output.html", context)
    
    # elif request.method == 'DELETE':
    #     # Delete all records from each specified table
    #     try:
    #         MainCalibration.objects.all().delete()
    #         CalibrationEquipment.objects.all().delete()
    #         CalibrationResult.objects.all().delete()

    #         return JsonResponse({'status': 'success', 'message': 'All data deleted successfully.'})
    #     except Exception as e:
    #         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)