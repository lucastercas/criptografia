require "./utils"

def decipher(cifertext, key)
  line_size = cifertext.size / key.size
  puts "Line Size: #{line_size}"

  sorted_key = key.chars.sort
  puts "Sorted Key: #{sorted_key}"

  index_key = 0
  key_char = sorted_key[index_key]
  print "#{key_char} => "
  for i in 0..cifertext.size-1 do
    char = cifertext[i]
    print char

    if (i+1) % line_size == 0 then
      puts
      index_key += 1
      key_char = sorted_key[index_key]
      print "#{key_char} => "
    end

  end
end
