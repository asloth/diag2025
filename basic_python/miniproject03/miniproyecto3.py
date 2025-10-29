import csv

def load_available_tests_hours() -> dict:
    try:
        with open("disponibilidad.txt", "r") as file:
            lines = [line.strip().split(" ") for line in file.readlines()]
            result = {line[0].lower(): int(line[1]) for line in lines if len(line) == 2}
            return result
    except FileNotFoundError:
        print("File disponibilidad.txt not found")
        return {}

def load_pacients() -> dict:
    pacients_file = "pacientes.csv"
    pacients_dict = {}
    try:
        with open(pacients_file, "r") as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                if len(row) > 1:  
                    patient_name = row[0].strip().title()
                    tests = [test.strip().lower() for test in row[1:]]
                    pacients_dict[patient_name] = tests
        return pacients_dict
    except FileNotFoundError:
        print("File pacientes.csv not found")
        return {}

def verify_available_test_for_pacient(pacient_tests: list, tests_availables: dict) -> tuple:
    temp = tests_availables.copy()
    for test in pacient_tests:
        if temp.get(test, 0) > 0:
            temp[test] -= 1
        else:
            return False, test  
    
    tests_availables.clear()
    tests_availables.update(temp)
    return True, ""

def add_tests(existing_tests:dict,new_tests:list) -> None:
    for new_test in new_tests:
        test_name = new_test.lower()
        try:
            existing_tests[test_name] +=1
        except :
            print("Test %s not found, will be passed" % new_test)
            continue

def print_welcome():
    """Print welcome message"""
    print("="*60)
    print("    BIENVENIDO AL SISTEMA DE GESTIÓN DE LABORATORIO MÉDICO")
    print("="*60)
    print("Comandos disponibles:")
    print("• ATENDER [nombre_paciente] - Atender a un paciente")
    print("• AGREGAR [examen1] [examen2] ... - Agregar disponibilidad")
    print("• STOP - Terminar el programa")
    print("="*60)
    print()

def print_availability(tests_dict: dict) -> None:
    print("Disponibilidad actual:")
    for test, hours in tests_dict.items():
        print(f"{test}: {hours}")
    print()

def main():
    print_welcome()

    # Load initial data
    available_tests = load_available_tests_hours()
    patients = load_pacients()
    
    if not available_tests:
        print("No se pudo cargar la disponibilidad de exámenes.")
        return
    
    if not patients:
        print("No se pudo cargar la información de pacientes.")
        return
    
    # Print initial availability
    print_availability(available_tests)
    
    # Main program loop
    while True:
        try:
            instruction = input("Ingrese una instrucción: ").strip()
            
            if not instruction:
                continue
                
            parts = instruction.split()
            command = parts[0].upper()
            
            if command == "STOP":
                print("Programa terminado.")
                break
                
            elif command == "ATENDER":
                if len(parts) < 2:
                    print("Formato incorrecto. Use: ATENDER nombre_paciente")
                    continue
                    
                patient_name = parts[1].title()
                
                if patient_name not in patients:
                    print(f"Paciente {patient_name} no encontrado.")
                    print()
                else:
                    patient_tests = patients[patient_name]
                    can_attend, unavailable_test = verify_available_test_for_pacient(patient_tests, available_tests)
                    
                    if can_attend:
                        print(f"Paciente {patient_name} atendido exitosamente.")
                        print()
                    else:
                        print(f"No se pudo atender al paciente {patient_name}.")
                        print(f"Examen sin disponibilidad: {unavailable_test}")
                        print()
                
            elif command == "AGREGAR":
                if len(parts) < 2:
                    print("Formato incorrecto. Use: AGREGAR examen1 examen2 ...")
                    continue
                    
                tests_to_add = parts[1:]
                add_tests(available_tests, tests_to_add)
                print("Disponibilidad agregada exitosamente.")
                
            else:
                print("Comando no reconocido. Use: ATENDER, AGREGAR o STOP")
            
            print_availability(available_tests)
            
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
