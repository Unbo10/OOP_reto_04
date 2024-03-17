def swap(a, b):
   return b, a

class Vertex:
   def __init__(self, given_x, given_y) -> None:
      self.x = given_x
      self.y = given_y
   
   def calculate_vertex_distance (self, vert):
      return (((self.x - vert.x)**2) + ((self.y - vert.y)**2))**1/2
   
class Edge: 
   def __init__(self, v1: Vertex, v2: Vertex) -> None:
      if v1.x > v2.x:
         self.start = v2
         self.end = v1
      else:
         self.start = v1
         self.end = v2

class Shape:
    def __init__(self, *args) -> None:
        self.is_regular: bool = False
        self.n_sides: int = len(args)
        temporary_vertices: list = list(args)
        self.vertices: list = self.create_shape(temporary_vertices)

    def print_shape_vertices(self):
        for i in self.vertices:
            print("(", i.x, ",", i.y, ")", end="; ")
        print()

    def refine_vertices(self, vertices_giv):
        """Method to remove vertices with the same x and/or same y coordinates"""

        #It first removes any repeated vertices:
        count = 0
        for k in vertices_giv:
            count = 0
            for j in vertices_giv:
                if (k.x == j.x) and (k.y == j.y):
                    count += 1
                if count > 1:
                    vertices_giv.remove(j)
                    count -= 1
                
        #It then checks for same-y vertices and removes them if there are more than 2 (in this case, at least one is collinear; so it's not an actual vertex of the polygon)
        j = 0
        i = 0
        count = 0
        repeated_y: list = []
        vertex_to_remove: Vertex = Vertex(0, 0)
        vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.x)
        while i < len(vertices_giv):
            count = 1
            repeated_y.clear()
            repeated_y.append(vertices_giv[i])
            j = i + 1
            while j < len(vertices_giv):
                if j == i:
                    pass
                else:
                    if vertices_giv[i].y == vertices_giv[j].y:
                        repeated_y.append(vertices_giv[j])
                        count += 1
                    if count > 2:
                        vertex_to_remove = repeated_y.pop(1)
                        vertices_giv.remove(vertex_to_remove)
                        count -= 1
                j += 1
            i += 1

        #It then checks for same-x vertices and removes them if there are more than 2 (in this case, at least one is collinear; so same thing happens as with the same-y)
        i = 0
        j = 0
        count = 0
        repeated_x: list = []
        vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.y)
        while i < len(vertices_giv):
            count = 1
            repeated_x.clear()
            repeated_x.append(vertices_giv[i])
            j = i + 1
            while j < len(vertices_giv):
                if j == i:
                    pass
                else:
                    if vertices_giv[i].x == vertices_giv[j].x:
                        repeated_x.append(vertices_giv[j])
                        count += 1
                    if count > 2:
                        vertex_to_remove = repeated_x.pop(1)
                        vertices_giv.remove(vertex_to_remove)
                        count -= 1
                j += 1
            i += 1

        self.n_sides = len(vertices_giv)
        return vertices_giv
    
    def sort_not_passed_vertices(m: Vertex, vertices_giv: list) -> list:
        m_pos = vertices_giv.index(m) # Position of last min or max
        i = m_pos + 1
        while i < len(vertices_giv):
            j = i + 1
            while j < len(vertices_giv):
                if vertices_giv[i].x < vertices_giv[j].x:
                    vertices_giv[i], vertices_giv[j] = vertices_giv[i], vertices_giv[j]
                j += 1
            i += 1
        return vertices_giv
            

    def create_shape(self, vertices_giv):
        vertices_giv = self.refine_vertices(vertices_giv)
        vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.y)
        min_y: Vertex = vertices_giv[0]
        max_y: Vertex = vertices_giv[self.n_sides - 1]
        # print("min_y: ", min_y.x, min_y.y, "max_y: ", max_y.x, max_y.y)
        vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.x)
        min_x: Vertex = vertices_giv[0]
        max_x: Vertex = vertices_giv[self.n_sides - 1]
        # print("min_x: ", min_x.x, min_x.y, "max_x: ", max_x.x, max_x.y)

        passed: int = 0 
        # There will be four conditions to pass: top (max_y), right (max_x), bottom (min_y) and left (one vertex before min_x).
        i: int = 0
        j: int = 0
        following_found: bool = False
        # The following vertex will be the one that fulfills certain conditions depending on the current vertex and the passed condition. That way, the vertices will be sorted in a clockwise manner.

        self.vertices = vertices_giv
        print("AAAAAAAA")
        self.print_shape_vertices()
        print("SAAAAA")
        sorted_v = 0
        while passed != 4:
            if passed == 0:
                while (passed == 0):
                    if vertices_giv[i] == max_y:
                        passed += 1
                    else:
                        j = i + 1
                        following_found = False
                        while following_found == False:
                            if vertices_giv[i] == max_y:
                                following_found = True
                                passed += 1
                                sorted_v += 1

                            elif (vertices_giv[j].y > vertices_giv[i].y) and (vertices_giv[j].x >= vertices_giv[i].x):
                                vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                                following_found = True
                                i += 1
                                j = i + 1
                                sorted_v += 1
                            else:
                                j += 1
                            print(sorted_v)

            elif passed == 1:
                print("passed", passed)
                vertices_giv = self.sort_not_passed_vertices(max_y, vertices_giv)
                while (passed == 1):
                    if vertices_giv[i] == max_x:
                        passed += 1
                    else:
                        j = i + 1
                        following_found = False
                        while following_found == False:
                            if vertices_giv[i] == max_x:
                                following_found = True
                                passed += 1
                                sorted_v += 1


                            elif (vertices_giv[j].x > vertices_giv[i].x) and (vertices_giv[j].y <= vertices_giv[i].y):
                                vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                                i += 1
                                j += 1
                                following_found = True
                                sorted_v += 1

                            else:
                                j += 1
                            print(sorted_v)
                            
            
            elif passed == 2:
                print("passed", passed)
                vertices_giv = self.sort_not_passed_vertices(max_x, vertices_giv)
                while (passed == 2):

                    if vertices_giv[i] == min_y:
                        passed += 1
                    else:
                        j = i + 1
                        following_found = False
                        while following_found == False:
                            if vertices_giv[i] == min_y:
                                following_found = True
                                passed += 1
                                sorted_v += 1


                            elif (vertices_giv[j].y < vertices_giv[i].y) and (vertices_giv[j].x <= vertices_giv[i].x):
                                vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                                i += 1
                                j += 1
                                following_found = True
                                sorted_v += 1

                            else:
                                j += 1
                            self.print_shape_vertices()
                            print(sorted_v)
                            


            elif passed == 3:
                print("passed", passed)
                vertices_giv = self.sort_not_passed_vertices(min_y, vertices_giv)
                while (passed == 3):
                    if i == self.n_sides - 1:
                        passed += 1
                    else:
                        j = i + 1
                        following_found = False
                        while following_found == False:
                            if j == self.n_sides - 1:
                                following_found = True
                                passed += 1
                                sorted_v += 1


                            elif (vertices_giv[j].x < vertices_giv[i].x) and (vertices_giv[j].y >= vertices_giv[i].y):
                                vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                                i += 1
                                j += 1
                                following_found = True
                                sorted_v += 1

                            else:
                                j += 1
                        print(sorted_v)
                            
            self.print_shape_vertices()
            
        return vertices_giv
      
if __name__ == "__main__":
   v1 = Vertex(2, -1)
   v2 = Vertex(3, -1)
   v3 = Vertex(3.5, -1)
   v4 = Vertex(9, 0)
   v5 = Vertex(7, -0.75)
   v6 = Vertex(10, 2)
   v7 = Vertex(1, 3)
   v8 = Vertex(2, 6)
   v9 = Vertex(12, 4)
   v10 = Vertex(10, 10)
   v11 = Vertex(10, 10)
   shape1 = Shape(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11)