from django.shortcuts import render
from app.models import InterlinkData

def keyboard(request):
    message = ''
    message_type = 'success'

    if request.method == 'POST':
        punch_number = request.POST.get('punch_number', '').strip()

        if punch_number:
            try:
                match = InterlinkData.objects.using('client_db').filter(CompSrNo=punch_number).exists()
                if match:
                    message = "✅ THIS PUNCH NUMBER IS CHECKED IN THE PREVIOUS STATION"
                else:
                    message = "❌ THIS PUNCH NUMBER IS NOT CHECKED"
                    message_type = 'error'
            except Exception as e:
                message = f"Error checking database: {e}"
                message_type = 'error'

    return render(request, 'app/keyboard.html', {
        'message': message,
        'message_type': message_type
    })
