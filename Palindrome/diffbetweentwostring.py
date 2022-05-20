def diffBetweenTwoStrings(source, target):
  diffArr=[]
  sourceArr=list(source)
  targetArr=list(target)

  for s in sourceArr:
    for t in targetArr:
      if s == t:
        diffArr.append(s)
      elif s != t:
        diffArr.append(f"-{s}")
      e