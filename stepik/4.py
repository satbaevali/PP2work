text=input().strip()
moneta=60
total=len(text)*moneta
rubbles=total//100
copika=total%100
print(f"{rubbles} p.{copika} коп.")