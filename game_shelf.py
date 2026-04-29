class ArrayList:
    def __init__(self):
        self.MEMORY_SPACE = 5
        self.lastPosition = 0
        self.array = [None] * self.MEMORY_SPACE

    def get(self, position: int):
        if position < 0 or position > self.size() - 1:
            raise IndexError("Index out of bounds exception")
        return self.array[position]

    def size(self):
        return self.lastPosition

    def capacity(self):
        return len(self.array)

    def add(self, value):
        if self.lastPosition == self.capacity():
            self._resizeMemory()
        self.array[self.lastPosition] = value
        self.lastPosition += 1

    def insertAt(self, value, position: int):
        if position < 0 or position > self.lastPosition:
            raise IndexError("Index out of bounds exception")
        if self.lastPosition == self.capacity():
            self._resizeMemory()
        self._shiftRight(self.lastPosition, position)
        self.array[position] = value

    def remove(self):
        if self.size() == 0:
            raise IndexError("Lista vazia")
        last = self.array[self.lastPosition - 1]
        self.lastPosition -= 1
        return last

    def removeAt(self, position: int):
        if position < 0 or position > self.size() - 1:
            raise IndexError("Index out of bounds exception")
        copy = self.array[position]
        self._shiftLeft(position, self.size() - 1)
        return copy

    def removeAll(self):
        self.lastPosition = 0

    def _shiftLeft(self, start: int, end: int):
        for i in range(start, end):
            self.array[i] = self.array[i + 1]
        self.lastPosition -= 1

    def _shiftRight(self, start: int, end: int):
        for i in range(start, end, -1):
            self.array[i] = self.array[i - 1]
        self.lastPosition += 1

    def _resizeMemory(self):
        print(f"  [ArrayList] Memoria cheia ({self.capacity()} slots) -> expandindo para {self.capacity() * 2}")
        newArray = [None] * (self.capacity() * 2)
        for i in range(self.capacity()):
            newArray[i] = self.array[i]
        self.array = newArray

    def print(self):
        print(f"  Lista ({self.size()} itens / {self.capacity()} slots): ", end="")
        print([self.array[i] for i in range(self.size())])


class Game:
    def __init__(self, title: str, genre: str, rating: float, platform: str):
        if not (0.0 <= rating <= 10.0):
            raise ValueError("Nota deve estar entre 0.0 e 10.0")
        self.title = title
        self.genre = genre
        self.rating = rating
        self.platform = platform

    def __repr__(self):
        return f"[{self.platform}] {self.title} ({self.genre}) - {self.rating}/10"


class GameShelf:
    def __init__(self, owner: str):
        self.owner = owner
        self._shelf = ArrayList()

    def addGame(self, game: Game):
        insertPos = self._shelf.size()
        for i in range(self._shelf.size()):
            if game.rating > self._shelf.get(i).rating:
                insertPos = i
                break
        self._shelf.insertAt(game, insertPos)
        print(f"  '{game.title}' adicionado na posicao {insertPos}")

    def removeByTitle(self, title: str):
        for i in range(self._shelf.size()):
            if self._shelf.get(i).title.lower() == title.lower():
                removed = self._shelf.removeAt(i)
                print(f"  '{removed.title}' removido da estante")
                return removed
        print(f"  Jogo '{title}' nao encontrado")
        return None

    def findByGenre(self, genre: str):
        results = ArrayList()
        for i in range(self._shelf.size()):
            g = self._shelf.get(i)
            if g.genre.lower() == genre.lower():
                results.add(g)
        return results

    def top(self, n: int = 3):
        result = ArrayList()
        limit = min(n, self._shelf.size())
        for i in range(limit):
            result.add(self._shelf.get(i))
        return result

    def display(self):
        print(f"\n  === Estante de {self.owner} ({self._shelf.size()} jogos) ===")
        if self._shelf.size() == 0:
            print("  (vazia)")
        for i in range(self._shelf.size()):
            print(f"  {i:2}. {self._shelf.get(i)}")
        print()

    def stats(self):
        if self._shelf.size() == 0:
            print("  Estante vazia")
            return
        total = sum(self._shelf.get(i).rating for i in range(self._shelf.size()))
        avg = total / self._shelf.size()
        best = self._shelf.get(0)
        worst = self._shelf.get(self._shelf.size() - 1)
        print(f"  Jogos catalogados : {self._shelf.size()}")
        print(f"  Nota media        : {avg:.1f}")
        print(f"  Melhor jogo       : {best.title} ({best.rating})")
        print(f"  Pior jogo         : {worst.title} ({worst.rating})\n")


shelf = GameShelf("Fulano")

print("\n=== Adicionando jogos ===")
shelf.addGame(Game("Hollow Knight",              "Metroidvania", 9.8, "PC"))
shelf.addGame(Game("Blasphemous",                    "Metroidvania",   9.9, "PC"))
shelf.addGame(Game("FIFA 25",                    "Sports",       5.0, "PS5"))
shelf.addGame(Game("Cyberpunk 2077",             "RPG",          9.5, "PC"))
shelf.addGame(Game("Stardew Valley",             "Simulation",   9.0, "PC"))


shelf.display()

print("=== Estatisticas ===")
shelf.stats()

print("=== Top 3 jogos ===")
top3 = shelf.top(3)
for i in range(top3.size()):
    print(f"  #{i+1}  {top3.get(i)}")

print("\n=== Jogos de RPG ===")
rpgs = shelf.findByGenre("RPG")
for i in range(rpgs.size()):
    print(f"  -> {rpgs.get(i)}")

print("\n=== Removendo FIFA 25 ===")
shelf.removeByTitle("FIFA 25")
shelf.display()

print("=== Estado final da ArrayList ===")
print(f"  Tamanho   : {shelf._shelf.size()}")
print(f"  Capacidade: {shelf._shelf.capacity()}")
shelf._shelf.print()