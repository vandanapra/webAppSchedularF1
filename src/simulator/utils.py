

def print_machines(machines):
    print("*******************************************************")
    print("*************Machines in the Virtual Factory***********")
    print("*******************************************************")
    for machine in machines:
        print(
            "Name:", machine.name,
            "Line:", machine.line,
            "Machine No:", machine.machine_no,
            "Status:", machine.status
        )


def print_inventory(inventory):
    print("******************Storage Inventory******************")
    for item in inventory:
        print(item.assembly_code, end=", ")
    print("")
