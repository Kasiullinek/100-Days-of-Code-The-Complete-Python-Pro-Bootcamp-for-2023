# from turtle import Turtle, Screen
#
# Sam = Turtle()
# print(Sam)
# Sam.shape("turtle")
# Sam.color("DarkGreen")
# Sam.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# print(my_screen.canvheight)
# my_screen.exitonclick()

######################################################################################
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)