def notas (nt1,nt2,nt3,nt4,nt5):
    #definimos la accion que van a realizar los datos ingresados
    totalSum=nt1+nt2+nt3+nt4+nt5
    prom=totalSum/5
    porc=prom/100
    print("La suma total de sus notas es: ",totalSum)
    print("El promedio de sus notas es de: ",prom)
    print("El porcentaje de sus notas es de: ",porc,"%") 
    
nt1=float(input("La primera calificacion es de: "))
nt2=float(input("La segunda calificacion es de: "))
nt3=float(input("La tercera calificacion es de: "))
nt4=float(input("La cuarta calificacion es de: "))
nt5=float(input("La quinta calificacion es de: "))

notas(nt1,nt2,nt3,nt4,nt5)