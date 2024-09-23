"""JSON MANUPULATION"""

"""
From a given input json (nested json), create a list of all keys and another list of all values

"""


def extract_keys_and_values(json_obj, keys_list=None, values_list=None):
    if keys_list is None:
        keys_list = []
    if values_list is None:
        values_list = []

    # If the current object is a dictionary, loop through its keys and values
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            keys_list.append(key)
            # Recursively call the function for nested dictionaries or lists
            extract_keys_and_values(value, keys_list, values_list)

    # If the current object is a list, iterate through the list
    elif isinstance(json_obj, list):
        for item in json_obj:
            extract_keys_and_values(item, keys_list, values_list)

    # If it's a value, add it to the values list
    else:
        values_list.append(json_obj)

    return keys_list, values_list


if __name__=='__main__':
    nested_json = {
        "name": "John",
        "age": 30,
        "address": {
            "city": "New York",
            "zipcode": "10001"
        },
        "hobbies": ["reading", "swimming"],
        "is_active": True
    }

    keys, values = extract_keys_and_values(nested_json)
    print("Keys:", keys)
    print("Values:", values)