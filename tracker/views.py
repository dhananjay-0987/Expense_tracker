from django.shortcuts import render , redirect
from .models import curr_balance, track_history
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        description = request.POST.get("description")
        amount = request.POST.get("amount")

        current_balance, _ = curr_balance.objects.get_or_create(id=1)
        expense_type = "Credit"
        if float(amount) < 0:
            expense_type = "Debit"

        if float(amount) == 0:
            messages.success(request, "Amount cannot be zero") 
            return redirect('/')
        
        trackhistory = track_history.objects.create(
            balance=current_balance,
            amount=amount,
            expense_type=expense_type,
            description=description,
        )
        current_balance.balance += float(trackhistory.amount)
        current_balance.save()

        print(description, amount)
        return redirect("/")

    return render(request, "index.html")