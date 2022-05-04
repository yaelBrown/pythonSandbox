def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root: 
        return 0
    
    if not root.left and not root.right:
        return 1
    
    depth = 1
    temp = []
    q = [root]
    
    while q: 
        n = q.pop(0)
        
        if len(q) == 0:
            depth += 1
            temp.append(depth)
            
        if n.left: 
            q.append(n.left)
        if n.right:
            q.append(n.right)
        
    return min(temp)