CC=g++
RM=rm -f

SOURCES=main.cpp cifrar.cpp decifrar.cpp utils.cpp
OBJECTS=$(subst .cpp,.o,$(SOURCES))

all: rotacao

rotacao: $(OBJECTS)
	$(CC) -o transposicao $(OBJECTS)

clean:
	$(RM) $(OBJECTS)

distclean: clean
	$(RM) transposicao
