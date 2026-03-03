from django.shortcuts import render

# Create your views here.
def MenuView(request): # the MenuView
    
    MenuItems = [ # list that contains all the menu items
        {'name': 'Pizza 🍕', 'price': 120, 'type': 'Main dish', 'Available': True},
        {'name': 'Burger 🍔', 'price': 80, 'type': 'Main dish', 'Available': True},
        {'name': 'Coke 🥤', 'price': 20, 'type': 'Drink', 'Available': True},
        {'name': 'Ice Cream 🍦', 'price': 50, 'type': 'Dessert', 'Available': False},   
        {'name': 'Pasta 🍝', 'price': 120, 'type': 'Main dish', 'Available': True},
        {'name': 'Salad 🥗', 'price': 60, 'type': 'Main dish', 'Available': False},
        {'name': 'Water 💧', 'price': 10, 'type': 'Drink', 'Available': True},
        {'name': 'Cake 🍰', 'price': 40, 'type': 'Dessert', 'Available': True},
        {'name': 'Steak 🥩', 'price': 150, 'type': 'Main dish', 'Available': True},
        {'name': 'Juice 🍊', 'price': 30, 'type': 'Drink', 'Available': True},
        {'name': 'Pie 🥧', 'price': 50, 'type': 'Dessert', 'Available': False},
        {'name': 'Pina Colada 🍍', 'price': 70, 'type': 'Drink', 'Available': True},
        {'name': 'Fries 🍟', 'price': 30, 'type': 'Appetizer', 'Available': True},
        {'name': 'Onion Rings 🧅', 'price': 40, 'type': 'Appetizer', 'Available': True},
        {'name': 'Garlic Bread 🧄', 'price': 25, 'type': 'Appetizer', 'Available': False},
        {'name': 'Mozzarella Sticks 🧀', 'price': 45, 'type': 'Appetizer', 'Available': True},
    ]

    SelectedType = request.GET.get('type', None) # get the selected type from the request, if there is no type selected it will be None
    SearchedKeyword = request.GET.get('search', None) # get the searched keyword from the request, if there is no keyword searched it will be None
    # print(SearchedKeyword)
    # print(SelectedType)
    
    # filtering phase
    if SelectedType is None:
        SelectedType = "All"    
    if SelectedType != 'All' and SelectedType is not None and SelectedType != '':
        MenuItems = [item for item in MenuItems if item['type'] == SelectedType]    
    if SearchedKeyword != '' and SearchedKeyword is not None:
        MenuItems = [item for item in MenuItems if SearchedKeyword.lower() in item['name'].lower()]
    
    context = { # dictionary that contains the menu items, the selected type, and the searchkey as well as the title
        'Title':"🍴 Abdelmohsen' Menu 🍴",
        'MenuItems': MenuItems, 
        'SelectedType': SelectedType,
        'SearchedKeyword': SearchedKeyword} 
    return render(request, 'Menu.html', context)
