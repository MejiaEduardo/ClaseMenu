Algoritmo Facturacion
	Definir ISV,Total,Subtotal,DSC_TC,DSC_TE,DSC_EFECTIVO,Descuento como real 
	Definir prc_unt, cnt_prd como entero
	
	Escribir "productos"
	Leer cnt_prd
	Escribir "Precio producto"
	Leer prc_unt
	Escribir "Descuento a aplicar,seleccione opcion"
	Escribir "1. DSC_TC"
	Escribir "2. DSC_TE"
	Escribir "3. DSC_EFECTIVO"
	leer Descuento
	
	Subtotal= cnt_prd*prc_unt
	
	
	Si (Descuento==1) entonces
		Dsc_TC= Subtotal*0.10
	Sino
		Si (Descuento==2) entonces
			DSC_TE=subtotal*0.30
		Sino
			Si  (Descuento==3) entonces
				Dsc_EFECTIVO=Subtotal*0.05
			FinSi
		FinSi
	Finsi 
	
	Descuento= DSC_TC+DSC_TE+DSC_EFECTIVO
	ISV= Subtotal+0.15
	Total= subtotal+ISV-Descuento
	
	Escribir "Descuentos:"
    Escribir "Descuento para tarjeta de crédito:", DSC_TC
    Escribir "Descuento para tercera edad:", DSC_TE
    Escribir "Descuento por pago en efectivo:", DSC_EFECTIVO
    Escribir "ISV:", ISV
    Escribir "Subtotal:", Subtotal
    Escribir "Total:", Total
    Escribir "Descuento total:", Descuento
	Imprimir Descuentos, ISV, Subtotal,Total,Descuento 
	
	
	
FinAlgoritmo
