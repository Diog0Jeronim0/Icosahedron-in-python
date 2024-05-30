import FreeCAD, Part, Mesh
from math import sqrt  # Import the sqrt function to calculate the square root

# Function to create the icosahedron
def create_icosahedron():
    # Radius of the vertices of the icosahedron
    radius = 10
    phi = (1 + sqrt(5)) / 2
    
    # Vertices of the icosahedron
    vertices = [
        FreeCAD.Vector(-radius, phi*radius, 0),
        FreeCAD.Vector(radius, phi*radius, 0),
        FreeCAD.Vector(-radius, -phi*radius, 0),
        FreeCAD.Vector(radius, -phi*radius, 0),
        FreeCAD.Vector(0, -radius, phi*radius),
        FreeCAD.Vector(0, radius, phi*radius),
        FreeCAD.Vector(0, -radius, -phi*radius),
        FreeCAD.Vector(0, radius, -phi*radius),
        FreeCAD.Vector(phi*radius, 0, -radius),
        FreeCAD.Vector(phi*radius, 0, radius),
        FreeCAD.Vector(-phi*radius, 0, -radius),
        FreeCAD.Vector(-phi*radius, 0, radius),
    ]
    
    # Triangular faces that make up the 20 faces of the icosahedron
    faces = [
        [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
        [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
        [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1],
    ]

    # Creating the faces of the icosahedron
    face_array = []
    for face in faces:
        wire = Part.makePolygon([vertices[i] for i in face] + [vertices[face[0]]])
        face_array.append(Part.Face(wire))

    # Creating a solid object from the faces
    shell = Part.makeShell(face_array)
    solid = Part.Solid(shell)

    # Verify the validity of the solid and add it to the FreeCAD document
    if solid.isValid():
        Part.show(solid)
    else:
        print("The solid is not valid. Check the faces and wire construction.")

# Call the function to create the icosahedron
create_icosahedron()
