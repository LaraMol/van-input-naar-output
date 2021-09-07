#Lara Mollaoglu Pizza calculator
print(' welke pizza wilt u: Small €5.00, Medium €10.00, Large €15.00')
keuzepizza = input (' Kies de afmeting') #hier vul jij je code in

if keuzepizza == ("small"):  #hier checked het wat je wilt
    prijspizza = float(5.00)
    hoeveelpizza = int(input("hoeveel pizza's wilt u?"))
elif keuzepizza == ("medium"):
    prijspizza = float(10.00)
    hoeveelpizza = int(input("hoeveel pizza's wilt u?"))
elif keuzepizza == ("large"):
    prijspizza = float(15.00)
    hoeveelpizza = int(input("hoeveel pizza's wilt u?"))
else: print("try again")

print("De afmeting die u heeft gekozen was " + keuzepizza + "De hoeveelheid pizza die u heeft gekozen is" + str(hoeveelpizza)) #en hier krijg jij je antwoord 
berekeningpizza = prijspizza * hoeveelpizza
print("De prijs wordt intotaal: " + str(berekeningpizza)) #en hier is de berekening