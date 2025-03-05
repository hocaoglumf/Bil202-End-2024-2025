def number_to_string(argument):
    match argument:
        case 0:
            return "sıfır"
        case 1:
            return "bir"
        case 2:
            return "iki"
        case default:
            return "birşey"

head = number_to_string(2)
print(head)
print(number_to_string)
