def print_matrix(matrix)
  for i in 0..matrix.size-1 do

    # Imprimir index da coluna na primeira linha
    if i == 0 then
      print "      "
      for j in 0..matrix[0].size-1 do
        print(j < 10 ? " #{j}  " : " #{j} ")
      end
      puts
    end

    for j in 0..matrix[i].size-1 do
      # Imprimir index da linha na primeira coluna
      if j == 0 then
        print((i < 10 ? "#{i} " : "#{i}") + " ->")
      end
      print("  #{matrix[i][j]} ")
    end
    puts
  end
end

def text_to_matrix(plaintxt, key)
  puts "=== Text To Matrix ==="
  matrix = []
  line = 0

  matrix[line] = []
  for i in 0..plaintxt.size-1 do
    if i % key.size == 0 && i != 0 then
      line += 1
      matrix[line] = []
    end
    matrix[line].append(plaintxt[i])
  end
  

  # Adicionar o numero de letras q faltam nos espacos
  # vazios da matriz
  while (i+1) % key.size != 0 do
    matrix[line].append("x")
    i += 1
  end

  return matrix
end

def matrix_to_text(matrix)
  result = ""
  matrix.each do |line|
    line.each do |char|
      result += char
    end
  end
  return result
end
