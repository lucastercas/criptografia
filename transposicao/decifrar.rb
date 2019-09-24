require "./utils"

def decipher(cifertext, key)
  matrix = text_to_matrix(cifertext, key)
  print_matrix(matrix)
end
