
def print_matrix(matrix)
  for i in 0..matrix.size-1 do

    # Imprimir index da coluna na primeira linha
    if i == 0 then
      print "      "
      for j in 0..matrix[0].size-1 do
        print "#{j} " 
      end
      puts
    end

    for j in 0..matrix[i].size-1 do
      # Imprimir index da linha na primeira coluna
      if j == 0 then
        print((i < 10 ? "#{i} " : "#{i}") + " ->")
      end
      # Se for a primeira linha, imprimir a "chave" destacada com |
      # Se nao for, imprimir matrix[i][j] normalmente
      print(i == 0 ? "|#{matrix[i][j]}" : " #{matrix[i][j]}")
    end
    puts
  end
end
