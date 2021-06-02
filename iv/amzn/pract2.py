def cellComplete(states, days):
  if days == 1 or days == 0:
    return states 
  else:
    def _checkCell(sL,sM,sR):
      if sL == None or sR == None: 
        return False
      if sL == sR: 
        return True
      else: 
        return False
    
    def _reverseCellValue(cV):
      if cV == 0:
        return 1
      else:
        return 0

    def _evalCells(state):
      idx = 0
      n = (len(state) - 1)
      # prev, nex = None

      for j in range(len(state)):
        if idx == 0: 
          if state[idx+1] != j:
            state[idx] = _reverseCellValue(j)
          else: 
            idx += 1
            continue
        elif idx == n: 
          idx += 1
          continue
        else: 
          if j == 1: 
            if state[idx - 1] == state[idx + 1]:
              state[idx] = _reverseCellValue(j)
        idx += 1
    
    for day in range(days):
      _evalCells(states)

  return states







if __name__ == "__main__":

  tc = [1,1,1,0,1,1,1,1]

  print(cellComplete(tc, 2))
