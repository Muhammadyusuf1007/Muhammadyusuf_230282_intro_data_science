def typeBasedTransformer(**kwargs):
    transformed_data = {}    
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed_data[key] = value ** 2
        elif isinstance(value, str):
            transformed_data[key] = value[::-1]
        elif isinstance(value, bool):
            transformed_data[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed_data[key] = value[::-1]
        elif isinstance(value, dict):
            transformed_data[key] = {v: k for k, v in value.items() if isinstance(v, (int, str, float))}
        else:
            transformed_data[key] = value
    return transformed_data
if __name__ == "__main__":
    result = typeBasedTransformer(
        number=4, 
        text="Hello", 
        flag=True, 
        sequence=[1, 2, 3], 
        data_dict={"a": 1, "b": 2},
        unsupported={1, 2, 3}
    )
    print(result)

