servers = []
for i in range(3):
    server_name = input(f"enter the servera name {i+1}: ")
    servers.append(server_name)
print(f"servers are the dame:{servers}")


ips = []

for i in range(3):
    servers_ips = input(f"enter the ip of service {servers[i]} : ")
    ips.append(servers_ips)
    
print(f"the ips with the serviqces are : {list(zip(servers, ips))}")


# task 3 view of ip addresser per serviice

def prompt_yes_no(prompt: str) -> bool:
    while True:
        choice = input(prompt).strip().lower()
        if choice in {"y", "n"}:
            return choice == "y"
        print("please enter y or n")


view_choice = prompt_yes_no("do you want to view any ip address? y/n: ")
if view_choice:
    while True:
        service_to_view = input("enter the servuce name you want to view: ")
        if service_to_view in servers:
            print(f"the ip for service {service_to_view} is {ips[servers.index(service_to_view)]}")
            break
        print("service not found")
        retry = prompt_yes_no("would you like to try again? y/n: ")
        if not retry:
            break

# task 4  edit of ip addresser per service

edit_choice = prompt_yes_no("do you want to edit any ip address? y/n: ")

if edit_choice:
    while True:
        service_to_edit = input("enter the servuce name you want to edit: ")
        if service_to_edit in servers:
            new_ip = input(f"enter the new ip for service {service_to_edit}: ")
            ips[servers.index(service_to_edit)] = new_ip
            print(f"updated ip addresses are: {list(zip(servers, ips))}")
            break
        print("service not found")
        retry = prompt_yes_no("would you like to try again? y/n: ")
        if not retry:
            break
