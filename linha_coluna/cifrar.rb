
def transformar_matriz(txt_claro, chave)
  result = []
  result[0] = chave.chars

  linha = 1
  result[linha] = []
  for i in 0..txt_claro.size do
    if txt_claro[i] == " " then next end

    result[linha].append(txt_claro[i])

    if (i+1) % chave.size == 0 && i != 0 then
      linha += 1
      result[linha] = []
    end
  end

  print result

  return result
end

def cifrar(txt_claro, chave)
  txt_claro = txt_claro.gsub(/\s+/, "")
  matriz = transformar_matriz(txt_claro, chave)

  chave_ordenada = chave.chars.sort
  chave_ordenada.each do |letra|
    index = matriz[0].index(letra)
    print "Index: #{index}"
  end

end
