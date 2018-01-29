import string
def get_personal_date() ->dict:
    """
    :return return a dir()
    """
    personal_data = {"name": "Jimmy", "a_role": "dancer"}
    return personal_data


def main() -> int:
    default_dict = dict()
    print(default_dict)
    intitalized_dict = dict([('name','jimmy'),('a_role','joker')])
    print(intitalized_dict)
    simple_init_dict = dict(name='jimmy', a_role='dance star')
    print(simple_init_dict)
    simple_init_dict['a_role'] = 'was a bear'
    print(simple_init_dict)
    compre = {x: x**2 for x in range(5)}
    print(compre)

    print(string.punctuation)
    s = "a little lamb, it's fleece".translate({ord(i): None for i in string.punctuation})
    print(s)

    return  0


if __name__=='__main__':
    main()
