import sys
sys.setrecursionlimit(10**8)
class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.cnt_children = None

    def count_all_children(self):
        if not self.cnt_children:
            self.cnt_children = len(self.children)
            for child in self.children.values():
                self.cnt_children += child.count_all_children()
        return self.cnt_children
class Trie:
    def __init__(self):
        self.head = Node("")

    def push(self, string):
        now = self.head
        str_idx = 0
        while True:
            if string[str_idx] not in now.children.keys():
                now.children[string[str_idx]] = Node(string[str_idx])
            if len(string) - str_idx == 1:
                now.children[string[str_idx]].children['='] = Node('=')
                return
            else:
                now = now.children[string[str_idx]]
                str_idx += 1

    def count_all_children(self):
        self.head.count_all_children()

    def autocomplete(self, string):
        now = self.head
        cnt = 0
        str_idx = 0
        while True:
            if len(string) - str_idx == 0:
                return cnt
            elif len(string) - str_idx + 1 == now.cnt_children:
                return cnt
            else:
                now = now.children[string[str_idx]]
                str_idx += 1
                cnt += 1

def solution(words):
    root = Trie()
    for word in words:
        root.push(word)
    answer = 0
    root.count_all_children()
    for word in words:
        cnt = root.autocomplete(word)
        answer += cnt if cnt else 1
    return answer