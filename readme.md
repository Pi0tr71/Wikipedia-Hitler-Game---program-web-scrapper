
# Gra w Wikipedia Hitlera

**Ten program to gra eksploracyjna w Wikipedii, której celem jest znalezienie najkrótszej ścieżki algorytmem BFS od początkowej strony Wikipedii do strony docelowej. Gra wykorzystuje programowanie asynchroniczne przy użyciu asyncio, web scraping przy użyciu BeautifulSoup oraz wizualizację ścieżek przy użyciu NetworkX i Matplotlib.**

---

## Jak Grać

1. Określ początkowy URL (`start_url`), słowo kluczowe docelowe (`target_keyword`), maksymalną głębokość (`max_depth`) oraz limit wyświetlanych linków dla artykułów z najkrótszej ścieżki (`limit_data_per_depth_in_graph`) w sekcji `__main__` skryptu.

### Przykład w Pythonie:

```python
start_url = "Pinniped"
target_keyword = "Adolf_Hitler"
max_depth = 3
limit_data_per_depth_in_graph = 30
```

2. Uruchom skrypt. Program będzie eksplorować strony Wikipedii, szukając najkrótszej ścieżki od strony początkowej do słowa kluczowego docelowego.
3. Maksymalna głębokość (`max_depth`) określa maksymalny poziom eksploracji.

**Jeśli ścieżka zostanie znaleziona w określonej głębokości, program wyświetli najkrótszą ścieżkę wraz z czasem trwania eksploracji.** Dodatkowo, wizualna reprezentacja eksplorowanych ścieżek zostanie wyświetlona przy użyciu NetworkX i Matplotlib.

---

## Użyte Technologie

- **Python**: Język programowania używany do napisania całego skryptu.
- **Programowanie asynchroniczne (asyncio)**: Biblioteka asyncio pozwala na wykonywanie asynchronicznych żądań webowych, co umożliwia efektywne eksplorowanie wielu stron Wikipedii jednocześnie.
- **Web Scraping (BeautifulSoup)**: BeautifulSoup jest używany do analizy zawartości HTML i wydobycia istotnych linków ze stron Wikipedii.
- **NetworkX i Matplotlib**: Te biblioteki są wykorzystywane do stworzenia wizualnej reprezentacji eksplorowanych ścieżek w formie grafu.

---

## Klasy

### Klasa `WikipediaHitlerGame`

**Atrybuty:**
- `start_url`: Początkowa strona Wikipedii.
- `target_keyword`: Słowo kluczowe docelowe do osiągnięcia.
- `max_depth`: Maksymalna głębokość do zbadania.
- `visited_links`: Zbiór do śledzenia odwiedzonych stron Wikipedii.
- `session`: Sesja `aiohttp ClientSession` do asynchronicznych żądań webowych.

**Metody:**
- `parse_article(url)`: Asynchronicznie analizuje zawartość strony Wikipedii i wydobywa poprawne linki do artykułów.
- `play_game()`: Rozpoczyna grę w eksplorację Wikipedii i zwraca najkrótszą ścieżkę, jeśli zostanie znaleziona.
- `close_session()`: Zamyka sesję `aiohttp ClientSession`.
- `create_graph(result_path, limit_data_per_depth_in_graph)`: Tworzy graf za pomocą NetworkX i Matplotlib do wizualizacji eksplorowanych ścieżek.

---

## Wizualizacja

Wizualizacja obejmuje:
- **Węzły** reprezentujące strony Wikipedii.
- **Krawędzie** reprezentujące połączenia.
- **Różne kolory** do odróżnienia ścieżek na różnych głębokościach. Strony początkowe i docelowe są podświetlone, a ogólna struktura grafu zapewnia klarowną reprezentację procesu eksploracji.

---

## Zachęta

Zachęcamy do dostosowywania parametrów w sekcji `__main__`, aby eksplorować różne ścieżki i głębokości na Wikipedii. Odkryj, jak Wikipedia jest połączona i znajdź najkrótszą drogę do wybranego celu!
