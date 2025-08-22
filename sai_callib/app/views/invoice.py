from django.shortcuts import render
from app.models import WorkOrder, Customer

def invoice(request):
    # Get the value of 'work_order_no' from the GET parameters
    work_order_no = request.GET.get('work_order_no')
    print("Work Order Number:", work_order_no)

    # Initialize variables
    common_data = None
    specific_items = []
    customer_details = None

    if work_order_no:
        try:
            # Fetch the work order(s) matching the provided work order number
            work_order_data = WorkOrder.objects.filter(work_order_no=work_order_no)

            # If no work order matches the provided number, handle it
            if not work_order_data.exists():
                print("No work order data found for the provided work_order_no.")
            else:
                # Prepare common data (same for all items)
                first_work_order = work_order_data.first()
                common_data = {
                    'customer_name': first_work_order.customer_name,
                    'wo_date': first_work_order.wo_date,
                    'work_order_no': first_work_order.work_order_no,
                    'customer_po_no': first_work_order.customer_po_no,
                    'customer_ref_date': first_work_order.customer_ref_date,
                    'order_type': first_work_order.order_type,
                    'customer_address': first_work_order.customer_address,
                }

                # Prepare specific items (vary for each work order)
                for work_order in work_order_data:
                    specific_items.append({
                        'inward_no': work_order.inward_no,
                        'item': work_order.item,
                        'hsn': work_order.hsn,
                        'sr_no': work_order.sr_no,
                        'id_no': work_order.id_no,
                        'range': work_order.range,
                        'make': work_order.make,
                        'channels': work_order.channels,
                    })

                # Fetch customer details based on customer_name
                customer = Customer.objects.filter(customer_name=first_work_order.customer_name).first()
                if customer:
                    customer_details = {
                        'primary_contact_person': customer.primary_contact_person,
                        'secondary_contact_person': customer.secondary_contact_person,
                        'primary_phone_no': customer.primary_phone_no,
                        'secondary_phone_no': customer.secondary_phone_no,
                        'primary_dept': customer.primary_dept,
                        'secondary_dept': customer.secondary_dept,
                    }

        except Exception as e:
            # Handle any errors that might occur during the database query
            print(f"Error fetching work order data: {e}")

    # Pass all data to the template
    return render(request, "app/invoice.html", {
        'common_data': common_data,
        'specific_items': specific_items,
        'customer_details': customer_details,
    })
