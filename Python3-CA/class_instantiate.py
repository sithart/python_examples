class Circle:
  pi = 3.14
  def area(self,radius):
    area = self.pi * radius ** 2
    return area


# Instance created

circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)