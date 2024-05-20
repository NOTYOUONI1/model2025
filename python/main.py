detels = {
    'name': "rakib",
    'age': 15
}


def l_o_d():
    print('list function call')
    i = input('List count: ')
    result = []
    result1 = []
    num = 0

    for num in range(int(i)):
        xii = input(f"List number {num + 1}: ")
        result.append(xii)
        result1.append(xii)

    for xy in result1:
        vowel_count = 0
        for char in xy:
            if char in 'aeiou':
                vowel_count += 1
        result.append({xy: vowel_count})

    print(result)
    return result

def mul():
    i = input('Auto or num $$ ')
    is_running = True

    if i.lower() == 'auto':
        find_num = int(input('Find mul number $$ '))
        mul = 1
        min_mul = 1
        while is_running:
            if mul * min_mul == find_num:
                print({find_num: [mul, min_mul]})
                is_running = False
            elif min_mul == 10:
                mul += 1
                min_mul = 1
            elif mul == 10:
                is_running = False
            else:
                min_mul += 1
    elif i.lower() == 'num':
        mul = int(input('Enter first number $$ '))
        min_mul = int(input('Enter second number $$ '))
        print(f"{mul} * {min_mul} = {mul * min_mul}")
    else:
        print("Invalid input")
    return


def weather():
    import requests

    city_name = input('Enter city name $$ ')
    tempq = str(input('Temp min_temp max_temp and options $$ '))
    api_key = '873c80b754317b6dacdff147927ee8f9'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    if tempq == 'options':
        response = requests.get(f"{base_url}?q={city_name}&appid={api_key}&units=metric")
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()  # Parse the JSON response
        print(weather_data)
    elif tempq == 'temp'or'min_temp'or'max_temp':
        try:
            # Make the API request
            response = requests.get(f"{base_url}?q={city_name}&appid={api_key}&units=metric")
            response.raise_for_status()  # Raise an exception for HTTP errors
            weather_data = response.json()  # Parse the JSON response

            # Extract and print the temperature
            temperature = weather_data['main'][tempq]
            resi = f"The current temperature in {city_name} is {temperature}°C."
            print(resi)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except KeyError:
            print(f"Could not retrieve weather data for {city_name}. Please check the city name.")
    elif not tempq == 'temp'or'min_temp'or'max_temp'or 'options':
        print('invalid')
def print_i():
    print(input('Enter print Text && '))
    return

def add_detels():
    i = input('Datals cunt number enter int $$ ')
    num = 0
    for no in range(int(i)):
        val = input(f"add datals name {num+1}: ")
        val1 = input(f"add datals value name {num}: ")
        detels[val] = val1
    return

def robot():
    vc = input('Robot on $$ ')
    if vc == 'on':
        print('Robot on OK')
        bool = True
        while bool:
            xiixz = input('Enter Function Name or deles && ')
            func_list = {'list': l_o_d,
                         'print': print_i,
                         'mul':mul,
                         'weather':weather
                         }
            if xiixz in func_list:

                func_list[xiixz]()
            elif xiixz == "view list":
                print(str(func_list))
            elif xiixz == 'add d':
                add_detels()
            elif xiixz == 'exit':
                bool = False
            elif xiixz == 'view options':
                print(f"view list \nadd d \nview d \n{func_list.keys()}")
            elif xiixz == 'view d':
                print(detels)
            else:
                if xiixz in detels:
                    print(detels[xiixz])
    else:
        print('Robot off')
    return

robot()
