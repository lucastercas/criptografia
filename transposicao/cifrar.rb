require "./utils"

# Fazer a transposicao da matrix,
# levando em conta a ordem alfabetica da primeira linha
def transform_matrix(matrix, key)
  sorted_key = key.sort
  copy_key = key
  result_matrix = Array.new(matrix[0].size){Array.new()}
  line_idx = 0

  sorted_key.each do |char|
    col = copy_key.index(char)
    copy_key[col] = -1
    for i in 0..matrix.size-1 do
      result_matrix[line_idx].append(matrix[i][col])
    end
    line_idx += 1
  end

  return result_matrix
end

def transposition(plaintxt, key)
  # Remover todos os espacos:
  plaintxt = plaintxt.gsub(/\s+/, "")
  # Transformar chave de string pra array de char:
  key = key.chars

  matrix = text_to_matrix(plaintxt, key)
  puts "-- Matriz --"
  print_matrix matrix

  result_matrix = transform_matrix(matrix, key)
  puts "-- Matriz Resultante --"
  print_matrix result_matrix

  return matrix_to_text(result_matrix)
end

def cipher(plaintxt, key)
  puts "=== Primeiro Estagio ==="
  first_stage = transposition(plaintxt, key)
  puts "Resultado: #{first_stage}"

  puts "=== Segundo Estagio ==="
  second_stage = transposition(first_stage, key)
  puts "Resultado: #{second_stage}"

  puts "=== Terceiro Estagio ==="
  third_stage = transposition(second_stage, key)
  puts "Resultado: #{third_stage}"

  return third_stage
end

