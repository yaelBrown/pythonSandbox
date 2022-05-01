# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root.val is None: 
            return []
        
        if root.left.val is None and root.right.val is None: 
            return [root.val]
        
        h = 0
        stk = [root]
        cur = root.left
        map = {0: [root.val]}
        
        while stk or cur: 
            while cur: 
                h += 1
                map[h] = []
                map[h].append(cur.val)
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            h -= 1
            cur = cur.right
            
        out = []
        for k in map.keys():
            out.append(map[k])
            
        return out
                


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root.val is None:
            return []

        if root.left.val is None and root.right.val is None:
            return [root.val]

        h = 0
        q = []
        nq = []
        cur = root 
        map = {}

        while q and cur: 
            try: 
                if map[h]:
                    pass
            except KeyError as e:
                map[h] = []
                    
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
            
            map[h].append(cur.val)
            cur = None

        # with breadth first search    
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if root.val is None: 
                return []
            
            if root.left.val is None and root.right.val is None: 
                return [root.val]
            
            q = [root] 
            out = []
            
            while q: 
                n = q.pop(0)
                out.append(n.val)
                if n.left: 
                    q.append(n.left)
                if n.right: 
                    q.append(n.right)
                
            return out

        # soln v1
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root: 
                return []
            
            if not root.left and not root.right: 
                return [[root.val]]
            
            q = [root] 
            temp = []
            out = []
            
            while q: 
                n = q.pop(0)
                temp.append(n.val)
                if len(q) == 0:
                    out.append(temp)
                    temp = []
                if n.left: 
                    q.append(n.left)
                if n.right: 
                    q.append(n.right)
                
            return out
        
        # soln v2
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root: 
                return []
            
            if not root.left and not root.right: 
                return [[root.val]]
            
            q = [root]
            nq = []
            temp = []
            out = []
            
            while q: 
                n = q.pop(0)
                temp.append(n.val)
                if len(q) == 0:
                    out.append(temp)
                    temp = []
                    q = nq
                    nq = []
                if n.left: 
                    nq.append(n.left)
                if n.right: 
                    nq.append(n.right)
                    
                if len(q) == 0:
                    q = nq
                    nq = []
            
                
            return out