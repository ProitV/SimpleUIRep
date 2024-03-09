def sample1_on_create2(hashMap,_files=None,_data=None):
  if not hashMap.containsKey("a"):
      hashMap.put("a","1")
  if not hashMap.containsKey("b"):
      hashMap.put("b","2")
      
  return hashMap

def sample1_on_input2(hashMap,_files=None,_data=None):
  if hashMap.get("listener")=="btn_account":
      hashMap.put("result",str(int(hashMap.get("a"))-int(hashMap.get("b"))))

  return hashMap
