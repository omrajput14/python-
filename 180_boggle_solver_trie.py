class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class BoggleSolver:
    def __init__(self, dictionary):
        self.root = TrieNode()
        for word in dictionary:
            self.insert(word)
            
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        
    def find_words(self, boggle):
        M, N = len(boggle), len(boggle[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        found_words = set()
        
        def dfs(i, j, node, path):
            if node.is_word:
                found_words.add(path)
                
            if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                char = boggle[i][j]
                if char in node.children:
                    visited[i][j] = True
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx != 0 or dy != 0:
                                dfs(i + dx, j + dy, node.children[char], path + char)
                    visited[i][j] = False
                    
        for i in range(M):
            for j in range(N):
                dfs(i, j, self.root, "")
                
        return list(found_words)

if __name__ == '__main__':
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    boggle = [['G', 'I', 'Z'],
              ['U', 'E', 'K'],
              ['Q', 'S', 'E']]
              
    solver = BoggleSolver(dictionary)
    words = solver.find_words(boggle)
    print("Following words of dictionary are present:")
    print(words)
