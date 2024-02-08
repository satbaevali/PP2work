class myshape():
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    def __str__(self):
        return f"Myshape -Color:{self.color},Is_filled:{self.is_filled}"
shape=myshape(color="black",is_filled=True)
print(shape)