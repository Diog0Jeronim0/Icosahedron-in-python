Representation of an Icosahedron on FreeCAD using python and opencv

You need to run the code on FreeCAD console

To explain the determination of the vertices of the icosahedron in the code is based on the golden ratio, also known as phi, which is approximately 1.618. In the code, the value of phi is calculated using the mathematical expression (1 + sqrt(5)) / 2. With the vertex radius set to 10, the vertex coordinates are established using symmetric combinations of (-radius, radius, 0 , -phi*radius, and phi*radius) for the X, Y and Z coordinates.
The vertices of the icosahedron are calculated so that all its edges are the same length and the angles of the faces are uniform. This precision thus guarantees a regularity of the icosahedron as a platonic solid, where the vertices are positioned so that they have the same distance from each other, ensuring so that the polyhedron maintains a symmetrical shape with identical triangular faces.
