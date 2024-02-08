class myshape():
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
shape1=myshape(color="blue",is_filled=True)
shape2=myshape(color="red",is_filled=False)
print("shape 1-",shape1.color,"Is_filled:",shape1.is_filled)
print("shape 2",shape2.color,"is_filled:",shape2.is_filled)

        