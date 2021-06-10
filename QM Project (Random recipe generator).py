#!/usr/bin/env python
# coding: utf-8

# # Random recipe generator for Pasta, Entreés and side dishes
# ### Just follow along and get an entire meal planned for you and your guests

# In[2]:


choice = input ("What do you want to cook? (Pasta or else)")

if choice == "else":
    print ("Try our random recipe generator below")
else:
    random1 = int (input ("Then choose a number between 1 to 3: "))

if random1 == 1 :
    print ("Eggplant Garlic pasta")
    
if random1 == 2:
    print ("Pasta carbonara")
    
if random1 == 3:
    print ("Summer tagliatele")


# In[3]:


answer1 = input ("Do you like this recipe idea? (yes/no):")
if answer1 == "yes":
    people1 = int (input ("How many people are you cooking for?"))
    
    if random1 == 1:
        oil = 0.5*people1
        garlic = 1*people1
        eggplant= 0.5*people1
        tomatoe = 0.5*people1
        rig = 125*people1
        print ("Ingredients:\n",oil, " cup(s) of olive oil\n",garlic, " Clove(s) of garlic, peeled and finely chopped\n",eggplant, " eggplant(s), peeled and diced\n",tomatoe, " can(s) of plum tomatoes with juice \n",rig,"g Rigatoni\n")
        print ("Preparation:\n\tStep 1\nHeat olive oil in a large skillet over medium heat; cook and stir garlic until fragrant for 1 to 2 minutes.\n\tStep 2\nAdd eggplant; cook, stirring constantly, until eggplant is softened, about 5 minutes.\n\tStep3\nAdd tomatoes and juice; cook until sauce is slightly reduced, about 20 minutes\n\tStep4\nInthe meantime, cook your pasta in boiling water until al dente. Once finished, drain and add to the sauce pan")
        
    if random1 == 2:
        yolk = 1.5*people1
        parm = 20*people1
        panc = 75*people1
        spag = 150*people1
        gar = 0.5*people1
        print ("Ingredients:\n",yolk, " large Eggyolks\n",parm, "g Parmesan\n",panc,"g Pancetta\n",spag,"g Spaghetti\n",gar," Cloves of garlic\nolive oil\n")
        print ("Preparation:\n\tStep 1\nPut the egg yolks into a bowl, finely grate in the Parmesan, season with pepper, then mix well with a fork and put aside.\n\t Step 2\nCut any hard skin off the pancetta and set aside, then chop the meat.\n\tStep3\nCook the spaghetti in a large pan of boiling salted water until al dente.\n\tStep 4\nMeanwhile, rub the pancetta skin, if you have any, all over the base of a medium frying pan (this will add fantastic flavour, or use 1 tablespoon of oil instead), then place over a medium-high heat.\n\tStep 5\nPeel the garlic, then crush with the palm of your hand, add it to the pan and leave it to flavour the fat for 1 minute. Stir in the pancetta, then cook for 4 minutes, or until it starts to crisp up.\n\tStep 6\nPick out and discard the garlic from the pan, then, reserving some of the cooking water, drain and add the spaghetti. Toss well over the heat so it really soaks up all that lovely flavour, then remove the pan from the heat.\n\tStep 7\nAdd a splash of the cooking water and toss well, season with pepper, then pour in the egg mixture – the pan will help to cook the egg gently, rather than scrambling it. Toss well, adding more cooking water until it’s lovely and glossy.\n\tStep 8\nServe with a grating of Parmesan and an extra twist of pepper.")
        
    if random1 == 3:
        bas = 0.5*people1
        garl = 0.5*people1
        alm = 25*people1
        par = 13*people1
        lem = 0.25*people1
        pota = 0.5*people1
        bean = 65*people1
        tag = 150*people1
        veg = 100*people1
        print ("Ingredients:\n",bas," bunch(es) of basil\n",garl, " Cloves of garlic\n",alm, "g blanched almonds",par,"g parmesan cheese\n",lem, " lemon(s)\n",pota," maris piper potatoe(s)\n",bean, "g green beans\n",tag,"g Tagliatelle\n",veg, "g summer vegetables of your choice, like borad beans, peas, tenderstem broccoli ...\n")
        print ("Preparation:\n\tStep 1\nPick most of the basil leaves into a pestle and mortar and bash to a paste with a pinch of sea salt. Peel and bash in the garlic, then pound in the almonds until fine.\n\tStep 2\nMuddle in 4 tablespoons of oil, finely grate in the Parmesan and then squeeze in the lemon juice. Season to your liking.\n\tStep 3\nScrub and finely slice the potato, trim just the stalks off the beans, then place both in a pan of boiling salted water with the tagliatelle and cook according to the pasta packet instructions.\n\tStep 4\nPrep the delicate summer veg as necessary, adding them to the pan for the last 3 minutes. Drain, reserving a mugful of starchy cooking water, then toss with the pesto, loosening with a splash of reserved cooking water, if needed.\n\tStep 5\nDrizzle with some olive oil, and finish with the remaining basil and a fine grating of Parmesan.")
else:
    print ("maybe try again")


# # Random entreé generator

# In[5]:


random2 = int (input ("Please enter a number from 1 to 3:"))

if random2 == 1 :
    print ("Tomatoe, Red wine and chorizo risotto")
    
if random2 == 2:
    print ("Asian Salmon and sweet potatoe traybake")
    
if random2 == 3:
    print ("Baked sweet potatoes with avocado and queso fresco")


# In[ ]:


answer2 = input ("Do you like this recipe? (yes/no):")
if answer2 == "yes":
    people2 = int (input ("How many people are you cooking for?"))
    
    if random2 == 1:
        shall = people2
        ga = 0.5*people2
        cho = 40*people2
        parl = 0.5*people2
        sto = 0.5*people2
        tom = 0.5*people2
        rice = 150*people2
        wine = 100*people2
        par = 25*people2
        print ("Ingredients:\n",shall," shallot(s)\n",ga, " Cloves of garlic\n",cho,"g Chorizo",parl, " bunch(es) of parsley\n",sto," liter(s) of stock\n",tom," can(s) of tomatoes\n",rice,"g of risotto rice\n",wine,"ml of red wine\n",par,"g of parmesan\n")
        print ("Preparation:\n\tStep 1\nPeel and finely chop the shallots and garlic, finely chop the chorizo, then pick and finely chop the parsley leaves, finely chopping the stalks.\n\tStep 2\nDrizzle 2 tablespoons of olive oil into a wide, shallow pan. Add the parsley stalks, shallot, garlic and chorizo to the heated oil and cook over a medium-high heat for about 5 minutes, or until the shallot is softened and the chorizo is beginning to crisp.\n\tStep 3\nIn another pan, heat the stock with the tinned tomatoes. Add the rice to the shallot mixture and stir to coat the grains. Cook over a high heat for 1 to 2 minutes, or until the grains have cracked and are slightly translucent at the tips, then pour in the red wine.Stir well and cook until almost all the wine has evaporated. \n\tStep 4\nAdd the hot stock and tomato mixture, ladle by ladle, stirring well with each addition, and only adding more when the previous ladle is almost fully absorbed. You may not need all of the mixture, or you may need to top it up with a little water.The rice should be tender but with a little bite in the middle. When it’s cooked, add one last ladle of liquid.\n\tStep 5\nFinely grate the Parmesan, then add to the pan with some seasoning. Stir well, take off the heat and cover. Leave for 5 minutes or so before stirring again, tasting and adjusting the seasoning, if necessary.\n\tStep 6\nServe topped with extra grated Parmesan and the chopped parsley leaves.")
        
    if random2 == 2:
        sw = 0.5*people2
        le = people2
        gi = 1.25*people2 
        g = people2
        ses = 0.5*people2
        st = 75*people2
        co = 75*people2
        li = 4*people2
        ch = people2
        sa = 200*people2
        print ("Ingredients:\n",sw," Sweet potatoe(s)\n",le," Lemongrass stick(s)\n",gi,"cm piece of ginger\n",g," Cloves of garlic\n",ses," teaspoon(s) of sesame oil\n",st,"ml of stock",co, "ml of coconut milk\n",li, " lime leaves\n",ch, " red chili(es)\n",sa, "g Salmon\n")
        print ("Preparation:\n\tStep 1\nPreheat the oven to 190°C/375°F/gas 5.\n\t Step 2\nScrub the sweet potato, then slice into thin rounds. Arrange the slices, overlapping, in a large roasting tin.\n\tStep 3\nBruise the lemongrass, then finely chop the tender parts. Peel and finely chop the ginger and garlic. Finely slice the chilli.\n\tStep 4\nMix the sesame oil, stock, coconut milk and two-thirds each of the lemongrass, ginger and garlic. Pour over the potatoes, tuck in the lime leaves (or squeeze the juice on top and scatter over the zest) and sprinkle over the chilli.\n\tStep 5\nRoast for 20 to 25 minutes, or until the potatoes are done. About 8 to 10 minutes before the cooking time is up, sit the fish on the potatoes and top with the rest of the lemongrass, ginger and garlic.\n\tStep 6\nWhen the fish is just cooked, drizzle with soy sauce, if you like.")
        
    if random2 == 3:
        swe = 2*people2
        avo = people2
        lim = people2
        pum = 20*people2
        che = 75*people
        print ("Ingredients:\n",swe," Sweet Potatoes\n",avo," Avocado(s)\n",lim," Lime(s)\n",pum,"g of pumpkin seeds\n",che,"g Mexican queso fresco or spanish manchego\n")
        print ("Preparation:\n\tStep 1\nPreheat the oven to 180ºC/gas 4.\n\tStep 2\nDrizzle the potatoes with oil, sprinkle with sea salt and black pepper, wrap in foil and bake in the oven for 1 hour to 1 hour 15 minutes, or until tender.\n\tStep 3\nWhen the potatoes are nearly done, destone and roughly chop the avocados and toss with the juice from half a lime.\n\tStep 4\nToast the pumpkin seeds in a dry pan for a few minutes until slightly golden.\n\tStep 5\nTop the potatoes with the avocado, crumble over the cheese and sprinkle with the toasted seeds. Serve with lime wedges for squeezing")
else:
    print ("maybe try again")
    


# # Random side dish generator

# In[ ]:


random3 = int (input ("Please enter a number from 1 to 3:"))

if random3 == 1 :
    print ("Bacon dates")
    
if random3 == 2:
    print ("Antipasto sticks")
    
if random3 == 3:
    print ("Watermelon Salad")


# In[ ]:


answer3 = input ("Do you like this recipe? (yes/no):")

if answer3 == "yes":
    people3 = int (input ("How many people are you cooking for?"))
    
    if random3 == 1:
        dat = 2*people3
        cheese = 20*people3
        bacon = 3*people3
    print ("Ingredients:\n",dat, " Dates\n" ,cheese, "g Blue Cheese\n",bacon," Bacon strips")
    print ("Instructions:\n\tStep 1\nPreheat the oven at 200ºC\n\tStep 2\nStuff your dates with the blue cheese\n\tStep 3\nWrap one bacon strip around each Date\n\tStep 4\nPut them on a baking sheet lined with parchment paper\n\tStep 5\nBake them for 5 minutes each side")
   
    if random3 == 2:
        arti = 2*people3
        grape = 2*people3
        mozza = 2*people3
        olive = 2*people3
        print ("Ingredients:\n",arti," marinated artichoke hearts\n",grape, " fresh grape tomatoes\n",mozza, "small mozzarelle balls\n",olive, " marinated olives\na bunch of flat leaved italian parsley\nsalt and pepper\n")
        print ("Instructions:\n\tStep 1\nGather all ingredients\n\tStep 2\nArrange your ingredients on your sticks with one tomate, one mozarella ball, on olive and ne artichoke heart each, adding parsley to personal preference.\n\tStep 3\nDrizzle with olive oil, salt and pepper before serving")
        
    if random3 == 3:
        melon = 150*people3
        onion = 0.5*people3
        feta = 60*people3
        print ("Ingredients:\n",melon,"g Watermelon\n",onion," small red onion(s)\n",feta,"g Feta cheese\na bunch of mint\nolive oil\nSalt and Pepper")
        print ("Instructions:\n\tStep 1\nScoop out and chop the watermelon flesh into chunks, discarding the peel.\n\tStep 2\nPeel and finely slice the onion, crumble the feta, then pick the mint leaves, tearing any larger ones.\n\tStep 3\nPlace it all into a bowl and combine. Drizzle over a little oil and season with black pepper")
else:
    print ("maybe try again")


# # Random Dessert Generator
# ##### After all, no one can have dinner without something sweet after

# In[25]:


import random

dessert = random.randint(1, 3)

if dessert==1:
    print ("Mini chocolate and berry trifles")
if dessert==2:
    print ("Chocolate berry tarte")
if dessert==3:
    print ("Mocha pot")


# In[8]:


answer4 = input ("Do you like this idea? (yes/no)")

if answer4=="yes":
    if dessert==2:
        print ("\nIngredients: \n5 tablespoons butter, divided \n5 crumbles up chocolate graham crackers\n2 teaspoons sugar\n3 tablespoons heavy whipping cream\n1/8 teaspoon ground cinnamon\n2/3 cup semisweet chocolate chips\n1/3 cup fresh blackberries\n1/3 cup fresh raspberries\nConfectioners' sugar")
        print ("\nPreparation: \n\tStep 1 \nIn a small microwave-safe bowl, melt 4 tablespoons butter; stir in cracker crumbs and sugar. Press onto the bottom and up the sides of two 4-in. fluted tart pans with removable bottoms. Freeze for 1 hour or until firm\n\tStep 2\nIn a small saucepan, combine the cream, cinnamon and remaining butter. Bring to a boil over medium heat, stirring constantly. Remove from the heat; stir in chocolate chips until melted. Pour into crusts. Refrigerate until firm, about 1 hour.\n\tStep 3\n Just before serving, arrange berries over filling; sprinkle with confectioners' sugar.")
    if dessert==1:
        print ("\nIngredients: \n4 thinly crowsway-sliced mini chocolate biskuit rolls \n125ml Chocolate Fudge Topping\n300g frozen mixed berries, thawed \n500ml custard\n2 tablespoons toasted flaked almonds")
        print ("\nPreparation: \n\tStep 1\nDivide half of the mini roll slices among 4 serving glasses and drizzle half of the fudge topping on them. \n\tStep 2\nTop with half of the berries and spoon over half of the custard.\n\tStep 3\n Continue layering with the remaining toppings in the same order. Sprinkle with almonds before serving.")
    if dessert==3:
        print ("\nIngredients: \n200g milk-chocolate with coffee, broken into chunks\n300ml pot double cream \n1 tsp vanilla extract \n2 tbsp creme fraiche ")
        print ("\nPreparation: \n\tStep 1\nMelt the chocolate in the microwave for 2 mins, stirring halfway through, or over a pan of gently simmering water. Leave to cool a little.\n\tStep 2\nUsing an electric whisk, whip the double cream with the vanilla in a bowl until lightly whipped. Fold in the cooled, melted chocolate until fully combined.\n\tStep 3\nSplit the mixture between four small bowls or ramekins and serve topped with a dollop of crème fraîche")
else:
    print ("Maybe try again then")


# # Code that we may need or use

# In[20]:


import random

q = random.randint(1, 3)

if q==1:
    print ("x")
if q==2:
    print ("Y")
if q==3:
    print ("z")


# In[3]:


from ipywidgets import interact
import ipywidgets as widgets
import math

p = widgets.IntSlider(min=1, max=10)


# In[17]:


from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "https://i.pinimg.com/originals/98/10/5e/98105e960d3de9b19765109d74a4ef23.jpg", width=300, height=300)


# In[ ]:





# In[4]:


people1 = int (input ("How many people are you cooking for?"))

if random1 == 1:
    oil = 0.5*people1
    garlic = 1*people1
    eggplant= 0.5*people1
    tomatoe = 0.5*people1
    rig = 125*people1
    
    print ("Ingredients:")
    print (oil, " cup(s) of olive oil\n",garlic, " Clove(s) of garlic, peeled and finely chopped\n",eggplant, " eggplant(s), peeled and diced\n",tomatoe, " can(s) of plum tomatoes with juice \n",rig,"g Rigatoni")
    
if random1 == 2:
    yolk = 1.5*people1
    parm = 20*people1
    panc = 75*people1
    spag = 150*people1
    gar = 0.5*people1
print ("Ingredients:\n",yolk, " large Eggyolks\n",parm, "g Parmesan\n",panc,"g Pancetta\n",spag,"g Spaghetti\n",gar," Cloves of garlic\nolive oil")
    
if random1 == 3:
    bas = 0.5*people1
    garl = 0.5*people1
    alm = 25*people1
    par = 13*people1
    lem = 0.25*people1
    pota = 0.5*people1
    bean = 65*people1
    tag = 150*people1
    veg = 100*people1
    print ("Ingredients:\n",bas," bunch(es) of basil\n",garl, " Cloves of garlic\n",alm, "g blanched almonds",par,"g parmesan cheese\n",lem, " lemon(s)\n",pota," maris piper potatoe(s)\n",bean, "g green beans\n",tag,"g Tagliatelle\n",veg, "g summer vegetables of your choice, like borad beans, peas, tenderstem broccoli ...")


# In[ ]:


people2 = int (input ("How many people are you cooking for?"))

if random2 == 1:
    shall = people2
    ga = 0.5*people2
    cho = 40*people2
    parl = 0.5*people2
    sto = 0.5*people2
    tom = 0.5*people2
    rice = 150*people2
    wine = 100*people2
    par = 25*people2
    print ("Ingredients:\n",shall," shallot(s)\n",ga, " Cloves of garlic\n",cho,"g Chorizo",parl, " bunch(es) of parsley\n",sto," liter(s) of stock\n",tom," can(s) of tomatoes\n",rice,"g of risotto rice\n",wine,"ml of red wine\n",par,"g of parmesan")
    
if random2 == 2:
    sw = 0.5*people2
    le = people2
    gi = 1.25*people2
    g = people2
    ses = 0.5*people2
    st = 75*people2
    co = 75*people2
    li = 4*people2
    ch = people2
    sa = 200*people2
    print ("Ingredients:\n",sw," Sweet potatoe(s)\n",le," Lemongrass stick(s)\n",gi,"cm piece of ginger\n",g," Cloves of garlic\n",ses," teaspoon(s) of sesame oil\n",st,"ml of stock",co, "ml of coconut milk\n",li, " lime leaves\n",ch, " red chili(es)\n",sa, "g Salmon")
    
if random2 == 3:
    swe = 2*people2
    avo = people2
    lim = people2
    pum = 20*people2
    che = 75*people
print ("Ingredients:\n",swe," Sweet Potatoes\n",avo," Avocado(s)\n",lim," Lime(s)\n",pum,"g of pumpkin seeds\n",che,"g Mexican queso fresco or spanish manchego")
        

