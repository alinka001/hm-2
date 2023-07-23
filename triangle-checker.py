class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides
    
    def is_triangle(self):
        if all(isinstance(el, (int, float)) for el in self.sides):
            self.sides.sort()
            side_1, side_2, side_3 = self.sides
            if side_1 > 0 and side_2 > 0 and side_3 > 0 :
                if side_1 + side_2 > side_3:
                    return "– Ура, можно построить треугольник!"
                return "– Жаль, но из этого треугольник не сделать"
            return "– С отрицательными числами ничего не выйдет!"
        return "– Нужно вводить только числа!"        
      
            
            
        
            
    
triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4]) #!!!!!
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())
           

#– Нужно вводить только числа!;
