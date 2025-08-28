from django.shortcuts import render , redirect
from .models import curr_balance, track_history
from django.contrib import messages

from django.db.models import Sum
# Create your views here.
def index(request):
    if request.method == "POST":
        description = request.POST.get("description")
        amount = float(request.POST.get("amount"))

        current_balance, _ = curr_balance.objects.get_or_create(id=1)
        expense_type = "CREDIT"
        if amount < 0:
            expense_type = "DEBIT"

        if amount == 0:
            messages.success(request, "Amount cannot be zero")
            return redirect('/')

        trackhistory = track_history.objects.create(
            balance=current_balance,
            amount=amount,
            expense_type=expense_type,
            description=description,
        )
        current_balance.balance += amount
        current_balance.save()
        return redirect("/")

    current_balance, _ = curr_balance.objects.get_or_create(id=1)
    income = 0
    expense = 0

    for trackhistory in track_history.objects.all():
        if trackhistory.expense_type == "CREDIT":
            income += trackhistory.amount
        else:
            expense += abs(trackhistory.amount)

    context = {
        'income': income,
        'expense': expense,
        'current_balance': current_balance.balance,
        'transactions': track_history.objects.all()
    }
    return render(request, "index.html", context)


def delete_transaction(request, id):
    tracking_history = track_history.objects.filter(id=id)
    if tracking_history.exists():
        current_balance, _ = curr_balance.objects.get_or_create(id=1)
        tracking_history = tracking_history[0]

        # Reverse transaction effect
        if tracking_history.expense_type == "CREDIT":
            current_balance.balance -= float(tracking_history.amount)
        else:
            current_balance.balance += float(abs(tracking_history.amount))

        current_balance.save()
        tracking_history.delete()

    return redirect('/')

# def index(request):
#     if request.method == "POST":
#         description = request.POST.get("description")
#         amount = request.POST.get("amount")

#         current_balance, _ = curr_balance.objects.get_or_create(id=1)
#         expense_type = "Credit"
#         if float(amount) < 0:
#             expense_type = "Debit"

#         if float(amount) == 0:
#             messages.success(request, "Amount cannot be zero") 
#             return redirect('/')
        
#         trackhistory = track_history.objects.create(
#             balance=current_balance,
#             amount=amount,
#             expense_type=expense_type,
#             description=description,
#         )
#         current_balance.balance += float(trackhistory.amount)
#         current_balance.save()
#         return redirect("/")
    
#     current_balance, _ = curr_balance.objects.get_or_create(id = 1)
#     income = 0
#     expense = 0
    
#     for trackhistory in track_history.objects.all():
#         if trackhistory.expense_type == "Credit":
#             income += trackhistory.amount
#         else:
#             expense += trackhistory.amount
    
#     context = {'income':income, 'expense':expense, 
#                'current_balance':current_balance.balance,
#                'transactions':track_history.objects.all()}
#     return render(request, "index.html", context)

# def delete_transaction(request, id):
#     tracking_history = track_history.objects.filter(id=id)
#     if tracking_history.exists():
#         current_balance,_ = curr_balance.objects.get_or_create(id=1)
#         tracking_history = tracking_history[0]
#         current_balance.balance = current_balance.balance - tracking_history.amount
#         current_balance.save()
#     tracking_history.delete()
#     return redirect('/')