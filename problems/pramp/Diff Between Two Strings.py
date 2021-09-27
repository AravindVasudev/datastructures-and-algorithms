def diffBetweenTwoStrings(source, target):
  memo = [[None] * len(target) for _ in range(len(source))]
  return findEdits(source, target, 0, 0, memo)[0]

def findEdits(source, target, sourceIndex, targetIndex,memo):  
  # Base Condition: If source is done, add remaining target
  if len(source) == sourceIndex:
    remaining = ["+" + char for char in target[targetIndex:]]
    return remaining, len(remaining)
  
  # Base Condition: If target is done and not source, return infinity
  if len(target) == targetIndex:
    return [], float('inf')
  
  # if not already seen
  if memo[sourceIndex][targetIndex] == None:
    # If both matches, just add that char
    if source[sourceIndex] == target[targetIndex]:
      nextChain, edits = findEdits(source, target, sourceIndex+1, targetIndex+1, memo)
      memo[sourceIndex][targetIndex] = [source[sourceIndex]] + nextChain, edits
    else:
      # If not, try both adding and removing
      addPath, addEdits =  findEdits(source, target, sourceIndex, targetIndex+1, memo)
      addPath = ["+" + target[targetIndex]] + addPath

      deletePath, deleteEdits = findEdits(source, target, sourceIndex+1, targetIndex, memo)
      deletePath = ["-" + source[sourceIndex]] + deletePath

      # Pick smallest path, if equal, pick deletePath  
      memo[sourceIndex][targetIndex] = (deletePath, deleteEdits+1) \
        if deleteEdits <= addEdits else (addPath, addEdits+1)
      
  return memo[sourceIndex][targetIndex]
