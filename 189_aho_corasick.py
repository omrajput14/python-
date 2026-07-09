from collections import deque

class AhoCorasick:
    def __init__(self):
        self.trie = [{}]
        self.output = [[]]
        self.fail = [-1]

    def add_word(self, word):
        state = 0
        for char in word:
            if char not in self.trie[state]:
                self.trie[state][char] = len(self.trie)
                self.trie.append({})
                self.output.append([])
                self.fail.append(-1)
            state = self.trie[state][char]
        self.output[state].append(word)

    def build(self):
        queue = deque()
        for char, state in self.trie[0].items():
            self.fail[state] = 0
            queue.append(state)

        while queue:
            current_state = queue.popleft()
            for char, next_state in self.trie[current_state].items():
                queue.append(next_state)
                fail_state = self.fail[current_state]
                while fail_state != -1 and char not in self.trie[fail_state]:
                    fail_state = self.fail[fail_state]
                if fail_state == -1:
                    self.fail[next_state] = 0
                else:
                    self.fail[next_state] = self.trie[fail_state][char]
                    self.output[next_state].extend(self.output[self.fail[next_state]])

    def search(self, text):
        state = 0
        results = []
        for i, char in enumerate(text):
            while state != -1 and char not in self.trie[state]:
                state = self.fail[state]
            if state == -1:
                state = 0
            else:
                state = self.trie[state][char]
                for word in self.output[state]:
                    results.append((i - len(word) + 1, word))
        return results

if __name__ == "__main__":
    ac = AhoCorasick()
    words = ["he", "she", "his", "hers"]
    for w in words:
        ac.add_word(w)
    ac.build()
    
    text = "ahishers"
    print(f"Searching in '{text}' for {words}")
    matches = ac.search(text)
    for index, word in matches:
        print(f"Found '{word}' at index {index}")
