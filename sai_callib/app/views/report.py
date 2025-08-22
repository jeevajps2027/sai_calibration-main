from django.http import JsonResponse
from django.shortcuts import render
from app.models import MainCalibration

def report(request):
    if request.method == "POST":
        certificate_no = request.POST.get("certificate_no")
        
        try:
            # Retrieve the MainCalibration object based on the certificate number
            main_calibration = MainCalibration.objects.prefetch_related('equipments', 'results').get(certificate_num=certificate_no)
            
            
            # Serialize the main calibration details
            main_calibration_data = {
                'certificate_num': main_calibration.certificate_num,
                'work_order': main_calibration.work_order,
                'date_of_issue': main_calibration.date_of_issue,
                'date_of_calibration': main_calibration.date_of_calibration,
                'next_calibration': main_calibration.next_calibration,
                'customer_address': main_calibration.customer_address,
                'range': main_calibration.range,
                'least_count': main_calibration.least_count,
                'identification_no': main_calibration.identification_no,
                'si_no': main_calibration.si_no,
                'make': main_calibration.make,
                'customer_ref': main_calibration.customer_ref,
                'date_calib': main_calibration.date_calib,
                'date_of_receipt': main_calibration.date_of_receipt,
                'calib_procedure_no': main_calibration.calib_procedure_no,
                'location': main_calibration.location,
                'inward_no': main_calibration.inward_no,
                'environment': main_calibration.environment,
                'uncertainty': main_calibration.uncertainty,
                'calib_engineer': main_calibration.calib_engineer,
                'quality_manager': main_calibration.quality_manager,
            }
            print("main_calibration_data",main_calibration_data)

            # Serialize related CalibrationEquipment objects
            equipments = [
                {
                    'sr_no': equipment.sr_no,
                    'master_name': equipment.master_name,
                    'id_no': equipment.id_no,
                    'calibration_no': equipment.calibration_no,
                    'valid_upto': equipment.valid_upto,
                    'traceability': equipment.traceability,
                }
                for equipment in main_calibration.equipments.all()
            ]

            print("equipments",equipments)


            # Serialize related CalibrationResult objects
            results = [
                {
                    'container_id': result.container_id,
                    'parameter': result.parameter,
                    'ref_size': result.ref_size,
                    'nominal': result.nominal,
                    'observation_size': result.observation_size,
                    'error': result.error,
                }
                for result in main_calibration.results.all()
            ]
            print("results",results)

            # Combine all the data into a single response
            response_data = {
                'main_calibration': main_calibration_data,
                'equipments': equipments,
                'results': results,
            }

            return JsonResponse(response_data)

        except MainCalibration.DoesNotExist:
            return JsonResponse({'error': 'Certificate number not found'}, status=404)

    # Render the HTML page for GET requests
    return render(request, "app/report.html")
