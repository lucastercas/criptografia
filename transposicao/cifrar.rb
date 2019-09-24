require "./utils"

def text_to_matrix(clear_txt, key)
  matrix = []

  line = 0
  matrix[line] = key.chars

  for i in 0..clear_txt.size-1 do
    if i % key.size == 0 then
      line += 1
      matrix[line] = []
    end
    matrix[line].append(clear_txt[i])
  end

  return matrix
end

def sort_matrix(matrix)
  sorted_key = matrix[0].sort
  sorted_matrix = Array.new(matrix.size){Array.new()}

  line = 0
  sorted_matrix[line] = sorted_key

  col_idx = 0
  sorted_key.each do |char|
    col = matrix[0].index(char)
    puts "#{char} => #{col} => #{col_idx}"

    for i in 1..matrix.size-1 do
      sorted_matrix[i].append(matrix[i][col])
    end
    col_idx += 1

  end

  return sorted_matrix
end

def cifrar(clear_txt, key)
  clear_txt = clear_txt.gsub(/\s+/, "")

  matrix = text_to_matrix(clear_txt, key)
  print_matrix(matrix)

  sorted_matrix = sort_matrix(matrix)
  print_matrix(sorted_matrix)
end
