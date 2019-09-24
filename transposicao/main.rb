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

  txt_claro = File.read(options[:input_file])

  puts "Texto Claro: #{txt_claro}"
  puts "Chave: #{options[:key ]}"

  cifrar(txt_claro, options[:key])
end

main()
