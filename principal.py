from typing import List

class AnalizadorVentas:
        def_init_(
        self,
        dias:int=7,
        meta_semanal:float=50000,0
        ):
        self.dias=dias
        self.meta_semanal=meta_semanal
        self.ventas:list[float]=[]
    
    def solicitar_ventas (self)
        print ("ingreso de ventas diarias\n")
        for dia in range (1,self.dias+1):
            while true:
                try:
                    entrada=input(f"ingrese las ventas del dia {dia}: $")
                    venta=float(entrada)
                    if venta <0:
                        raise ValueError ("la venta no puede ser negativa")
                    self.ventas.append(venta)
                    break
                except ValueError as e:
                    print (f"entrada no valida: {e}")


def main ()
    analizador=AnalizadorVentas()
    analizador.solicitar_ventas()

    if_name-=="_main_":
        main()