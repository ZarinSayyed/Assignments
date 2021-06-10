#Assignment 4: SimpleSearch
class IceCreamMachine:
  def __init__(self,ingredients,topping):
    self.ingredients=ingredients
    self.topping=topping
   
  def scoops(self): 
    try:  
        result=[]
        for i in self.ingredients:
            for j in self.topping:
                result.append([i,j])
        return result
    except:
        print("Error")
        
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate_sauce"])
print(machine.scoops())