import requests

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Levanta exceção se status >= 400
        print(f"[INFO] GET {url} -> {response.status_code} ({response.elapsed.total_seconds()*1000:.0f} ms)")
        for user in response.json()[:3]:  # Mostra os 3 primeiros
            print(f"- {user['name']} ({user['email']})")
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha na requisição: {e}")

if __name__ == "__main__":
    get_users()
    ..
    
