CC=g++
RM=rm -f

SOURCES=main.cpp util.cpp decifrar.cpp cifrar.cpp
OBJECTS=$(subst .cpp,.o,$(SOURCES))

all: transposicao

transposicao: $(OBJECTS)
	$(CC) -o transposicao.exe $(OBJECTS)

clean:
	$(RM) $(OBJECTS)

distclean: clean
	$(RM) transposicao
