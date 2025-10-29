def generar_codigos_tiendas(nombre1, nombre2):
    """Genera códigos de 3 letras para las tiendas"""
    codigo1 = nombre1[:3].upper()
    codigo2 = nombre2[:3].upper()
    
    # Si son iguales, agregar "2" al segundo
    if codigo1 == codigo2:
        codigo2 = codigo2 + "2"
    
    return codigo1, codigo2

def procesar_despacho(categoria):
    """Retorna el costo de despacho según la categoría"""
    costos_despacho = {
        'cerca': 1000,
        'normal': 5000,
        'lejos': 10000,
    }
    return costos_despacho.get(categoria.lower(), None)

def procesar_instruccion(instruccion, costo_actual):
    """Procesa una instrucción y retorna el nuevo costo y descripción"""
    partes = instruccion.strip().split()
    
    if len(partes) < 2:
        return None, "Instrucción inválida"
    
    # Caso 1: Descuento
    if partes[0].lower() == 'descuento':
        try:
            descuento = float(partes[1])
            nuevo_costo = costo_actual - descuento
            descripcion = f"Descuento ${descuento}"
            return nuevo_costo, descripcion
        except ValueError:
            return None, "Valor de descuento inválido"
    
    # Caso 2: Despacho
    elif partes[0].lower() == 'despacho':
        categoria = partes[1].lower()
        costo_despacho = procesar_despacho(categoria)
        
        if costo_despacho is None:
            return None, "Categoría de despacho inválida. Use: cerca, normal, lejos"
        
        nuevo_costo = costo_actual + costo_despacho
        descripcion = f"Despacho {categoria} ${costo_despacho}"
        return nuevo_costo, descripcion
    
    # Caso 3: Cantidad y precio (X Z)
    else:
        try:
            cantidad = int(partes[0])
            precio_unitario = float(partes[1])
            
            if cantidad >= 10:
                # Compra mayorista: un producto gratis
                costo_productos = (cantidad - 1) * precio_unitario
                descripcion = f"{cantidad} productos x ${precio_unitario} = ${costo_productos} (Mayorista: -${precio_unitario})"
            else:
                costo_productos = cantidad * precio_unitario
                descripcion = f"{cantidad} productos x ${precio_unitario} = ${costo_productos}"
            
            nuevo_costo = costo_actual + costo_productos
            return nuevo_costo, descripcion
            
        except ValueError:
            return None, "Formato inválido. Use: cantidad precio (ej: 5 1000)"

def main():
    print("=== COMPARADOR DE TIENDAS ===\n")
    
    # Configuración inicial
    nombre1 = input("Ingrese el nombre de la primera tienda: ").strip()
    nombre2 = input("Ingrese el nombre de la segunda tienda: ").strip()
    
    if not nombre1 or not nombre2:
        print("Error: Debe ingresar ambos nombres de tiendas")
        return
    
    codigo1, codigo2 = generar_codigos_tiendas(nombre1, nombre2)
    print(f"\nTiendas identificadas como: {codigo1} y {codigo2}")
    
    # Inicializar costos
    costo1 = 0
    costo2 = 0
    ronda = 1
    
    print("\n=== INSTRUCCIONES ===")
    print("1. 'descuento X' - Descuenta X del total")
    print("2. 'despacho categoria' - Suma costo de envío (express/normal/economico/gratis)")
    print("3. 'X Z' - X cantidad, Z precio unitario")
    print("4. 'salir' - Terminar el programa\n")
    
    while True:
        print(f"--- RONDA {ronda} ---")
        
        # 3 instrucciones para cada tienda (6 total por ronda)
        for tienda_actual in [1, 2]:
            codigo_actual = codigo1 if tienda_actual == 1 else codigo2
            costo_actual = costo1 if tienda_actual == 1 else costo2
            
            print(f"\nInstrucciones para tienda {codigo_actual}:")
            
            for instruccion_num in range(1, 4):  # 3 instrucciones por tienda
                while True:
                    prompt = f"{codigo_actual} - Instrucción {instruccion_num}/3: "
                    instruccion = input(prompt).strip()
                    
                    if instruccion.lower() == 'salir':
                        print("\nPrograma terminado por el usuario.")
                        return
                    
                    nuevo_costo, descripcion = procesar_instruccion(instruccion, costo_actual)
                    
                    if nuevo_costo is not None:
                        # Actualizar el costo correspondiente
                        if tienda_actual == 1:
                            costo1 = nuevo_costo
                            costo_actual = costo1
                        else:
                            costo2 = nuevo_costo
                            costo_actual = costo2
                        
                        print(f"  -> {descripcion} (Total: ${nuevo_costo})")
                        break
                    else:
                        print(f"  Error: {descripcion}")
        
        # Aplicar corrección de montos negativos al final de cada ronda
        if costo1 < 0:
            print(f"  {codigo1} tenía monto negativo (${costo1}), ajustado a $0")
            costo1 = 0
        if costo2 < 0:
            print(f"  {codigo2} tenía monto negativo (${costo2}), ajustado a $0")
            costo2 = 0
        
        # Mostrar resumen de la ronda
        print(f"\n=== RESUMEN RONDA {ronda} ===")
        print(f"{codigo1}: ${costo1}")
        print(f"{codigo2}: ${costo2}")
        
        # Verificar si alguna tienda superó el presupuesto
        presupuesto_superado = False
        if costo1 > 100000 or costo2 > 100000:
            presupuesto_superado = True
            print("\n PRESUPUESTO SUPERADO - JUEGO TERMINADO")
            if costo1 > 100000:
                print(f"{codigo1} superó el presupuesto de $100,000 con ${costo1}")
            if costo2 > 100000:
                print(f"{codigo2} superó el presupuesto de $100,000 con ${costo2}")
        
        # Si se superó el presupuesto, terminar el juego
        if presupuesto_superado:
            break
        
        ronda += 1
        print("\n" + "="*50)
    
    # Resultado final
    print(f"\n=== RESULTADO FINAL ===")
    print(f"{codigo1} ({nombre1}): ${costo1}")
    print(f"{codigo2} ({nombre2}): ${costo2}")
    
    # Determinar ganador final
    if costo1 > 100000 and costo2 > 100000:
        # Ambas superaron el presupuesto - gana la que menos gastó
        if costo1 < costo2:
            diferencia = costo2 - costo1
            print(f"\n GANADOR: {codigo1} ({nombre1})")
            print(f"Razón: Ambas superaron el presupuesto, pero {codigo1} gastó ${diferencia} menos")
        elif costo2 < costo1:
            diferencia = costo1 - costo2
            print(f"\n GANADOR: {codigo2} ({nombre2})")
            print(f"Razón: Ambas superaron el presupuesto, pero {codigo2} gastó ${diferencia} menos")
        else:
            print(f"\n EMPATE")
            print(f"Razón: Ambas tiendas superaron el presupuesto con el mismo monto (${costo1})")
    elif costo1 > 100000:
        # Solo tienda 1 superó el presupuesto - gana tienda 2
        print(f"\n GANADOR: {codigo2} ({nombre2})")
        print(f"Razón: {codigo1} superó el presupuesto de $100,000")
    elif costo2 > 100000:
        # Solo tienda 2 superó el presupuesto - gana tienda 1
        print(f"\n GANADOR: {codigo1} ({nombre1})")
        print(f"Razón: {codigo2} superó el presupuesto de $100,000")

if __name__ == "__main__":
    main()
