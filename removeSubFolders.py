from typing import List
class Solution:
    class TrieNode:
        def __init__(self, val: str, is_folder:bool = False):
            self.val = val
            self.children = {}
            self.is_folder = is_folder
    def DFS(self, tnode:TrieNode, path_set:set, curr_path:str) -> None:
        if tnode.is_folder:
            path_set.remove(curr_path)
        for path in tnode.children.keys():
            self.DFS(tnode.children[path], path_set, curr_path + "/" + path)


    def removeSubfolders(self, folder: List[str]) -> List[str]:
        head_node = self.TrieNode('')
        ans = set()
        for f in folder:
            paths = f.split('/')
            curr_node = head_node
            for i in range(1, len(paths)):
                if paths[i] in curr_node.children.keys():
                    curr_node = curr_node.children[paths[i]]
                    if curr_node.is_folder:
                        break
                else:
                    trie_node = self.TrieNode(paths[i], i == len(paths)-1)
                    curr_node.children[paths[i]] = trie_node
                    curr_node = trie_node
            if i == len(paths) - 1:
                ans.add(f)
                curr_node.is_folder = True
            for path in curr_node.children.keys():
                self.DFS(curr_node.children[path], ans, f + "/" + path)
        return list(ans)

solution = Solution()
print(solution.removeSubfolders(["/a/bc/de/fg", "/ab","/a/bc", "/a/bc/de"]))