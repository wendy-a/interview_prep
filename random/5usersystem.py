def implement_api(api_requests):
    system = {}
    result = []
    for request in api_requests:
        data = request.split()
        action = data[0]
        if action == 'register':
            if data[1] in system:
                result.append('Username already exists')
            else:
                system[data[1]] = [data[2],0]
                result.append('Registered Successfully')
        elif action == 'login':
            if data[1] in system and data[2] == system[data[1]][0] and system[data[1]][1] == 0:
                system[data[1]][1] = 1
                result.append('Logged In Successfully')
            else:
                result.append('Login Unsuccessful')
        elif action == 'logout':
            if data[1] in system and system[data[1]][1] == 1:
                system[data[1]][1] = 0
                result.append('Logged Out Successfully')
            else:
                result.append('Logged Unsuccessful')
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_request = ['register a b', 'register a c', 'login a b', 'login a c', 'login b c', 'logout a']
    print(implement_api(api_request))
