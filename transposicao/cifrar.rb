require "./utils"

def text_to_matrix(plaintxt, key)
  matrix = []

  line = 0
  matrix[line] = key.chars

  for i in 0..plaintxt.size-1 do
    if i % key.size == 0 then
      line += 1
      matrix[line] = []
    end
    matrix[line].append(plaintxt[i])
  end

  return matrix
end

# Fazer a transposicao da matrix, levando em conta a ordem alfabetica 
# da primeira linha
def transform_matrix(matrix)
  sorted_key = matrix[0].sort
  sorted_matrix = Array.new(matrix[0].size){Array.new()}

  line_idx = 0
  sorted_key.each do |char|
    col = matrix[0].index(char)
    for i in 0..matrix.size-1 do
      sorted_matrix[line_idx].append(matrix[i][col])
    end

    line_idx += 1
  end

  return sorted_matrix
end

def cifrar(plaintxt, key)
  plaintxt = plaintxt.gsub(/\s+/, "")

  puts "#{plaintxt} -> #{plaintxt.size}"

  matrix = text_to_matrix(plaintxt, key)
  print_matrix(matrix)

  sorted_matrix = transform_matrix(matrix)
  print_matrix(sorted_matrix)

  result = ""
  sorted_matrix.each do |line|
    line.each do |char|
      result += char
    end
  end
  return result
end
