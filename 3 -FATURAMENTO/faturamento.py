from JsonHandle import *
from calc import calc

def main():
    Json_path ="3 -FATURAMENTO\dados.json"
    data = JSONReader(Json_path)
    calc(data)

    #json_str = '{"name": "John", "age": 30, "city": "New York"}'

if __name__ == '__main__':
    main()