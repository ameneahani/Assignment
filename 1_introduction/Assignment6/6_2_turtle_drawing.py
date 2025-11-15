import turtle
i = 20
p = turtle.Pen()

for n in range (3,i):
    first_teta = 90*(n+2)/n
    teta = 360/n
    p.left(first_teta)
    p.forward(30+40+(n-3)*4/n*10)
    for i in range(n-1):
        p.left(teta)
        p.forward(30+40+(n-3)*4/n*10)
    p.up()
    p.left(-(90*(n-2)/n))
    p.forward(15)
    p.down()


