from time import sleep
import turtle


def draw_circle(color, time):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    sleep(time)


class TrafficLight:
    __color = {"red": 5, "yellow": 2, "green": 5}

    def running(self):
        turtle.hideturtle()
        turtle.speed(0)
        turtle.color("white")
        for key, value in self.__color.items():
            draw_circle(key, value)
            if key != "yellow":
                for i in ["white", key, "white", key]:
                    draw_circle(i, 0.5)
            if key == "green":
                for key_rev, value_rev in reversed(self.__color.items()):
                    if key_rev != "green":
                        draw_circle(key_rev, value_rev)


tl = TrafficLight()
tl.running()
