from django.shortcuts import render, redirect
from .forms import PizzaForm, ToppingForm, CommentForm
from .models import Pizza, Topping, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


def index(request):
    return render(request, 'pizza/index.html')


@login_required
def pizzas(request):
    pizzas = Pizza.objects.order_by('date')

    context = {'pizzas': pizzas}

    return render(request, 'pizza/pizzas.html', context)


@login_required
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')

    context = {'pizza': pizza, 'toppings': toppings, 'comments': comments}

    return render(request, 'pizza/pizza.html', context)


@login_required
def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()

    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():

            new_pizza = form.save(commit=False)

            new_pizza.save()

            return redirect('pizza:pizza')

    context = {'form': form}
    return render(request, 'pizza/new_pizza.html', context)


@login_required
def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = ToppingForm()

    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():

            new_topping = form.save(commit=False)

            new_topping.pizza = pizza

            new_topping.save()

            return redirect('pizza:pizza', pizza_id=pizza_id)

    context = {'form': form, 'pizza': pizza}

    return render(request, 'pizza/new_topping.html', context)


@login_required
def edit_topping(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza

    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect('pizza:pizza', pizza_id=pizza.id)

    context = {'topping': topping, 'pizza': pizza, 'form': form}

    return render(request, 'pizza/edit_topping.html', context)


@login_required
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()

    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()

            return redirect('pizza:pizza', pizza_id=pizza_id)

    context = {'form': form, 'pizza': pizza}

    return render(request, 'pizza/new_comment.html', context)
