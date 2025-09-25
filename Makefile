# here we access the root configuration, include files, and libraries
ROOTCFLAGS = $(shell root-config --cflags)
ROOTLIBS   = $(shell root-config --libs) -lMathMore
ROOTGLIBS  = $(shell root-config --glibs)
ROOTFLAGS   = $(ROOTCFLAGS) $(ROOTLIBS) $(ROOTGLIBS) 
CXXFLAGS  = $(ROOTCFLAGS) -Wall -O3
LDFLAGS    = $(ROOTLIBS) $(ROOTGLIBS)
GXX	   = g++ $(CXXFLAGS)


a11: cpp_example cpp_example2


cpp_example: cpp_example.cpp
	$(GXX) $(CXXFLAGS) -o cpp_example cpp_example.cpp $(LDFLAGS)
cpp_example2: cpp_example2.cpp
	$(GXX) $(CXXFLAGS) -o cpp_example2 cpp_example2.cpp $(LDFLAGS)

clean:
	rm -f cpp_example
	rm -f *~ *.d *.so *.pcm rm 

cleanall: clean
	rm -f *pdf *png
