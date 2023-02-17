from bs4 import BeautifulSoup
import requests
import json

data = []
url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"
for i in range(2844): #add pages
    params = {
        "_paginador_fila_actual": f"{i+1}",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"class": "tabla_datos"})
        if table is not None:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                row_data = {}
                for i, cell in enumerate(cells):
                    row_data[f"columna_{i+1}"] = cell.text.strip()
                if len(row_data) > 1: 
                    data.append(row_data)
                    with open("archivo.json", "w") as f:
                        json.dump(data, f)
        else:
            print("No se encontró la tabla.")
    else:
        print(f"Error al realizar la solicitud: {response.status_code}")
