```python
import random
n=int(input("the scale of your matric:"))
end=int(input("your goal:"))
a=[[0 for col in range(n)] for row in range(n)]


def move_left(x):
    for i in range(n):
        for j in range(n):
            if j>0:
                if x[i][j-1]==0:
                    xyg=0
                    for k in range(j,n):
                        if a[i][k]!=0:
                            xyg=a[i][k]
                            a[i][k]=0
                            break
                    x[i][j-1]=xyg
    for i in range(n):
        for j in range(n):
            if j>0:
                if x[i][j-1]==x[i][j]:
                    x[i][j-1]=2*x[i][j]
                    x[i][j]=0
    for i in range(n):
        for j in range(n):
            if j>0:
                if x[i][j-1]==0:
                    xyg=0
                    for k in range(j,n):
                        if a[i][k]!=0:
                            xyg=a[i][k]
                            a[i][k]=0
                            break
                    x[i][j-1]=xyg
    return(x)

def move_right(x):
    for i in range(n):
        for j in range(n-1,-1,-1):
            if j<n-1:
                if x[i][j+1]==0:
                    xyg=0
                    for k in range(j,-1,-1):
                        if a[i][k]!=0:
                            xyg=a[i][k]
                            a[i][k]=0
                            break
                    x[i][j+1]=xyg
    for i in range(n):
        for j in range(n-1,-1,-1):
            if j<n-1:
                if x[i][j+1]==x[i][j]:
                    x[i][j+1]=2*x[i][j]
                    x[i][j]=0
    for i in range(n):
        for j in range(n-1,-1,-1):
            if j<n-1:
                if x[i][j+1]==0:
                    xyg=0
                    for k in range(j,-1,-1):
                        if a[i][k]!=0:
                            xyg=a[i][k]
                            a[i][k]=0
                            break
                    x[i][j+1]=xyg
    return(x)

def new(x):
    t=0
    while t==0:
        i=random.randint(0,n-1)
        j=random.randint(0,n-1)
        if x[i][j]==0:
            t=1
            x[i][j]=2
    return(x)
            
        

max=2
min=0
a=new(a)
for i in range(n):
        print(a[i])
print('\n')
while max!=end:
    a=new(a)
    for i in range(n):
        print(a[i])
    print('\n')
    nextmove=input("next move:")
    if nextmove=='a':
        a=move_left(a)
    elif nextmove=='d':
        a=move_right(a)
    elif nextmove=='w':
        a=[[r[col] for r in a] for col in range(len(a[0]))]
        a=move_left(a)
        a=[[r[col] for r in a] for col in range(len(a[0]))]
    elif nextmove=='s':
        a=[[r[col] for r in a] for col in range(len(a[0]))]
        a=move_right(a)
        a=[[r[col] for r in a] for col in range(len(a[0]))]
    min=max
    for i in range(n):
        for j in range(n):
            if a[i][j]>max:
                max=a[i][j]
            if a[i][j]<min:
                min=a[i][j]
    if min>1:
        print("Game Over")
        waiting=input("Game Over")
        break
    print(max)
    print(min)
    for i in range(n):
        print(a[i])
    print('\n')

if end==max:
    print("你赢了")
    waiting=input("you win")

```

