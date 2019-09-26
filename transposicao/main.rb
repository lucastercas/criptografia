#!/usr/bin/env ruby

require "optparse"
require "./cifrar"
require "./decifrar"

def get_options()
  options = {}

  OptionParser.new do |parser|
    parser.banner = "Uso: main.rb [options]"

    parser.on("-i", "--entrada FILE", "Arquivo que contem o texto claro") do |file|
      options[:input_file] = file
    end

    parser.on("-k", "--chave KEY", "Chave") do |key|
      options[:key] = key
    end

  end.parse!
  return options
end

def main()
  puts "\n===== Transposicao ====="
  options = get_options()

  plaintxt = File.read(options[:input_file])

  key = options[:key]

  puts "=== Texto Claro ==="
  puts "#{plaintxt} -> #{plaintxt.size}"
  puts "=== Chave ==="
  puts "#{key}"

  ciphertext = cipher(plaintxt, key)
  puts
  puts "=== Texto Cifrado ==="
  puts "#{ciphertext} -> #{ciphertext.size}"

  deciphered_text = decipher(ciphertext, key)
end

main()

