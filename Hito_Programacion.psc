Algoritmo Hito_Programacion
	Repetir	 
		Escribir"1-Registrarte"
		Escribir "2-Seleccionar Coche"
		Escribir "3-Pagar"
		Escribir "4-Codigo de Seguimiento"
		Escribir "5- Salir"
		Escribir "Eleccion Nº"
		Leer OP
		Segun OP Hacer
			1:
			Definir Nombre,Apellidos,Correo Como Caracter
			Definir Tlf,DNI Como Entero
			Escribir "Nombre: "
			Leer Nombre
			Escribir "Apellidos: "
			Leer Apellidos
			Escribir "DNI: "
			Leer DNI
			Escribir "Correo: "
			Leer Correo
			Escribir "Tlf: "
			Leer Tlf
		2:
			Escribir"1-NissanGTR"
			Escribir "2-Audi R8 V10"
			Escribir "3-Subaru Impreza STI"
			Escribir "4-Volskwaguen Golf GTI"
			Escribir "5-Range Rover Velar"
			Escribir "Eleccion Nº: "
			Leer OP
			Segun OP Hacer
				1:
					Escribir "Has elegido el Nissan GTR"
				2:
					Escribir "Has elegido el Audi R8 V10"
				3:
					Escribir "Has elegido el Subaru Impreza STI"
				4:
					Escribir "Has elegido el Volskwaguen Golf GTI"
				5:
					Escribir "Has elegido el Range Rover Velar"
			FinSegun
		3:
			Definir tarjeta,Caduca,CVV Como Entero
			Escribir "Tarjeta: "
			Leer Tarjeta
			Escribir "Caduca en: "
			Leer Caduca
			Escribir "CVV: "
			Leer CVV
			Escribir "La factura sera enviada a la siguiente direccion de correo" Correo
		4: 
			Escribir "Su codigo de seguimiento sera envisado al" Tlf "y al siguiente correo" Correo 
		5:
		De Otro Modo:
			Escribir "Eleccion no valida"
		FinSegun
			
	Hasta Que OP=5	
	Escribir "Hasta la Proxima"
	
FinAlgoritmo