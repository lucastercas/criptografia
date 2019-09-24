require "./utils"

# Fazer a transposicao da matrix,
# levando em conta a ordem alfabetica da primeira linha
def transform_matrix(matrix, key)
  sorted_key = key.sort

  result_matrix = Array.new(matrix[0].size){Array.new()}

  line_idx = 0

  sorted_key.each do |char|
    col = key.index(char)
    for i in 0..matrix.size-1 do
      result_matrix[line_idx].append(matrix[i][col])
      # Caso a chave tenha letras repetidas, anular a coluna
      # que ja virou linha
      matrix[i][col] = -1
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
  first_stage = transposition(plaintxt, key)
  puts "=== Primeiro Estagio ==="
  puts "#{first_stage}"

  second_stage = transposition(first_stage, key)
  puts "=== Segundo Estagio ==="
  puts "#{second_stage}"

  third_stage = transposition(second_stage, key)
  puts "=== Terceiro Estagio ==="
  puts "#{third_stage}"

  return third_stage
end

