class Node:
    def __init__(self, value):
        self.content = value
        self.next: Node = None

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self._length: int = 0

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        return self._length
    
    def capacity(self):
        return "Infinita"
    
    def get(self, position: int):
        if position < 0 or position >= self._length:
            raise IndexError("Index out of bounds exception")
        aux = self.head
        for _ in range(position):
            aux = aux.next
        return aux.content

    def add(self, value):
        newNode = Node(value)
        self._length += 1
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insertAt(self, value, position: int):
        if position < 0 or position > self._length:
            raise IndexError("Index out of bounds exception")
    
        if position == self._length:
            self.add(value)
            return
    
        newNode = Node(value)

        if position == 0:
            newNode.next = self.head
            self.head = newNode
            self._length += 1
            return
    
        aux = self.head
        for _ in range(position - 1):
            aux = aux.next

        newNode.next = aux.next
        aux.next = newNode
        self._length += 1
    def removeAt(self, position: int):
        if position < 0 or position >= self._length:
            raise IndexError("Index out of bounds exception")
        
        if position == 0:
            copy = self.head
            self.head = self.head.next
            self._length -= 1
            if self._length == 0:
                self.tail = None
            return copy.content
        
        aux = self.head
        for _ in range(position - 1):
            aux = aux.next

        node_to_remove = aux.next

        if node_to_remove == self.tail:
            self.tail = aux

        aux.next = node_to_remove.next
        self._length -= 1

        return node_to_remove.content
    
    def print(self):
        aux = self.head
        elements = []
        while aux != None:
            elements.append(str(aux.content))
            aux = aux.next
        print("  [" + ", ".join(elements) + "]")

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
        self._shelf = LinkedList()

    def addGame(self, game: Game):
        insertPos = self._shelf.size()
        for current_index in range(self._shelf.size()):
            if game.rating > self._shelf.get(current_index).rating:
                insertPos = current_index
                break
        self._shelf.insertAt(game, insertPos)
        print(f"  '{game.title}' adicionado na posicao {insertPos}")

    def removeByTitle(self, title: str):
        for search_index in range(self._shelf.size()):
            if self._shelf.get(search_index).title.lower() == title.lower():
                removed = self._shelf.removeAt(search_index)
                print(f"  '{removed.title}' removido da estante")
                return removed
        print(f"  Jogo '{title}' nao encontrado")
        return None

    def findByGenre(self, genre: str):
        results = LinkedList()
        for search_index in range(self._shelf.size()):
            current_game = self._shelf.get(search_index)
            if current_game.genre.lower() == genre.lower():
                results.add(current_game)
        return results

    def top(self, maximum_quantity: int = 3):
        result = LinkedList()
        limit = min(maximum_quantity, self._shelf.size())
        for index in range(limit):
            result.add(self._shelf.get(index))
        return result

    def display(self):
        print(f"\n  === Estante de {self.owner} ({self._shelf.size()} jogos) ===")
        if self._shelf.size() == 0:
            print("  (vazia)")
        for index in range(self._shelf.size()):
            print(f"  {index:2}. {self._shelf.get(index)}")
        print()

    def stats(self):
        if self._shelf.size() == 0:
            print("  Estante vazia")
            return
        total = sum(self._shelf.get(index).rating for index in range(self._shelf.size()))
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
shelf.addGame(Game("Blasphemous",                "Metroidvania", 9.9, "PC"))
shelf.addGame(Game("FIFA 25",                    "Sports",       5.0, "PS5"))
shelf.addGame(Game("Cyberpunk 2077",             "RPG",          9.5, "PC"))
shelf.addGame(Game("Stardew Valley",             "Simulation",   9.0, "PC"))
shelf.addGame(Game("GTA",                        "Simulation",   10.0, "PC"))
shelf.addGame(Game("GTA",                        "Simulation",   10.0, "PC"))

shelf.display()

print("=== Estatisticas ===")
shelf.stats()

print("=== Top 3 jogos ===")
top3 = shelf.top(3)
for position in range(top3.size()):
    print(f"  #{position+1}  {top3.get(position)}")

print("\n=== Jogos de RPG ===")
rpgs = shelf.findByGenre("RPG")
for position in range(rpgs.size()):
    print(f"  -> {rpgs.get(position)}")

print("\n=== Removendo FIFA 25 ===")
shelf.removeByTitle("FIFA 25")
shelf.display()

print("=== Estado final da LinkedList ===")
print(f"  Tamanho   : {shelf._shelf.size()}")
print(f"  Capacidade: {shelf._shelf.capacity()}")
shelf._shelf.print()

import time
print("")
print("                            TESTE DE ESTRESSE")
print("")
inicio_tempo = time.time()


for i in range(1000):
    
    
    shelf._shelf.insertAt(Game(f"Jogo Clone {i}", "Ação", 7.0, "PC"), 0)

fim_tempo = time.time()

print(f"  Tamanho final da estante: {shelf._shelf.size()} jogos")
print(f"  Tempo gasto para processar: {fim_tempo - inicio_tempo:.4f} segundos")
