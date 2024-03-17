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
      self.start = v1
      self.end = v2
      self.length = v1.calculate_vertex_distance(v2)
      self.slope = (v2.y - v1.y) / (v2.x - v1.x)

class Shape:
   def __init__(self, *args) -> None:
      self.is_regular: bool = False
      self.n_sides: int = len(args)
      temporary_vertices: list = list(args)
      self.vertices: list = self.sort_vertices(temporary_vertices)
      self.edges: list = self.create_edges()
      self.print_shape_vertices()
      self.print_shape_edges()

   def print_shape_vertices(self) -> None:
      for i in self.vertices:
         print("(", i.x, ",", i.y, ")", end="; ")
      print()

   def print_shape_edges(self) -> None:
      for i in self.edges:
         print("(", i.start.x, ",", i.start.y, ")", "(", i.end.x, ",", i.end.y, ")", end="; ")
      print()

   def eliminate_repeated_vertices(self, vertices_giv):
      """Method to remove vertices with the same x and same y coordinates"""

      count = 0
      for k in vertices_giv:
         count = 0
         for j in vertices_giv:
               if (k.x == j.x) and (k.y == j.y):
                  count += 1
               if count > 1:
                  vertices_giv.remove(j)
                  count -= 1

      return vertices_giv
   
   def sort_not_passed_vertices(self, m: Vertex, vertices_giv: list) -> list:
      """Method to sort the vertices that have not been passed yet, that is, that have not been sorted yet. It will sort them in descending order of x coordinate. This is done to avoid positioning a vertex as the following of another vertex although is not the immediately following one."""

      m_pos = vertices_giv.index(m) # * Position of last min or max
      i = m_pos + 1
      while i < len(vertices_giv):
         j = i + 1
         while j < len(vertices_giv):
            if vertices_giv[i].x < vertices_giv[j].x:
               vertices_giv[i], vertices_giv[j] = vertices_giv[j], vertices_giv[i]
            j += 1
         i += 1
      return vertices_giv

   def sort_vertices(self, vertices_giv):
      vertices_giv = self.eliminate_repeated_vertices(vertices_giv)
      self.n_sides = len(vertices_giv)
      self.vertices = vertices_giv

      vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.y)
      min_y_candidates: list = []
      max_y_candidates: list = []
      min_y_candidates.append(vertices_giv[0])
      max_y_candidates.append(vertices_giv[self.n_sides - 1])
      self.print_shape_vertices()
      i = 0
      for i in vertices_giv:
         if (i.y == min_y_candidates[0].y) and (i.x != min_y_candidates[0].x):
            min_y_candidates.append(i)
         if (i.y == max_y_candidates[0].y) and (i.x != max_y_candidates[0].x):
            max_y_candidates.append(i)

      min_y_candidates = sorted(min_y_candidates, key = lambda vertex: vertex.x)
      max_y_candidates = sorted(max_y_candidates, key = lambda vertex: vertex.x)
      min_y: Vertex = min_y_candidates[len(min_y_candidates) - 1]
      max_y: Vertex = max_y_candidates[0]
      print("min_y:", min_y.x, min_y.y, "max_y:", max_y.x, max_y.y)

      vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.x)
      min_x_candidates: list = []
      max_x_candidates: list = []
      min_x_candidates.append(vertices_giv[0])
      max_x_candidates.append(vertices_giv[self.n_sides - 1])
      for i in vertices_giv:
         if (i.x == min_x_candidates[0].x) and (i.y != min_x_candidates[0].y):
            min_x_candidates.append(i)
         if (i.x == max_x_candidates[0].x) and (i.y != max_x_candidates[0].y):
            max_x_candidates.append(i)

      min_x_candidates = sorted(min_x_candidates, key = lambda vertex: vertex.y)
      max_x_candidates = sorted(max_x_candidates, key = lambda vertex: vertex.y)
      min_x: Vertex = min_x_candidates[0]
      max_x: Vertex = max_x_candidates[len(max_x_candidates) - 1]
      print("min_x: ", min_x.x, min_x.y, "max_x: ", max_x.x, max_x.y)

      vertices_giv = sorted(vertices_giv, key = lambda vertex: vertex.x)

      passed: int = 0 
      # * There will be four conditions to pass: top (max_y), right (max_x), bottom (min_y) and left (one vertex before min_x).
      i: int = 0
      j: int = 0
      following_found: bool = False
      # * The following vertex will be the one that fulfills certain conditions depending on the current vertex and the passed condition. That way, the vertices will be sorted in a clockwise manner.

      self.vertices = vertices_giv
      self.print_shape_vertices() 
      while passed != 4:
         if passed == 0:
               while (passed == 0):
                  if vertices_giv[i] == max_y:
                     passed += 1
                  else:
                     j = i + 1
                     following_found = False
                     while following_found == False:
                           if vertices_giv[j] == max_y:
                              following_found = True
                              vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                              i += 1
                           elif (vertices_giv[j].y >= vertices_giv[i].y) and (vertices_giv[j].x >= vertices_giv[i].x):
                              vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                              following_found = True
                              i += 1
                              j = i + 1                            
                           else:
                              j += 1

         elif passed == 1:
               vertices_giv = self.sort_not_passed_vertices(max_y, vertices_giv)
               while (passed == 1):
                  if vertices_giv[i] == max_x:
                     passed += 1
                  else:
                     j = i + 1
                     following_found = False
                     while following_found == False:
                        if vertices_giv[j] == max_x:
                           following_found = True
                           vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                           i += 1

                        elif (vertices_giv[j].x >= vertices_giv[i].x) and (vertices_giv[j].y <= vertices_giv[i].y):
                           vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                           i += 1
                           j += 1
                           following_found = True
                        else:
                           j += 1                            
         
         elif passed == 2:
               vertices_giv = self.sort_not_passed_vertices(max_x, vertices_giv)
               while (passed == 2):
                  if vertices_giv[i] == min_y:
                     passed += 1
                  else:
                     j = i + 1
                     following_found = False
                     while following_found == False:
                           if vertices_giv[j] == min_y:
                              following_found = True
                              vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                              i += 1
                           elif (vertices_giv[j].y <= vertices_giv[i].y) and (vertices_giv[j].x <= vertices_giv[i].x):
                              vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                              i += 1
                              j += 1
                              following_found = True
                           else:
                              j += 1

         elif passed == 3:
               vertices_giv = self.sort_not_passed_vertices(min_y, vertices_giv)
               while (passed == 3):
                  if i == self.n_sides - 1:
                     passed += 1
                  else:
                     j = i + 1
                     following_found = False
                     while following_found == False:
                           if i == self.n_sides - 1:
                              following_found = True
                              passed += 1
                           elif (vertices_giv[j].x <= vertices_giv[i].x) and (vertices_giv[j].y >= vertices_giv[i].y):
                              vertices_giv[i + 1], vertices_giv[j] = vertices_giv[j], vertices_giv[i + 1]
                              i += 1
                              j += 1
                              following_found = True
                           else:
                              j += 1
                           
      return vertices_giv
   
   def create_edges(self):
      edges: list = []
      i = 0
      while i < len(self.vertices) - 1:
         edges.append(Edge(self.vertices[i], self.vertices[i + 1]))
         if (i >= 1) and edges[i - 1].slope == edges[i].slope:
            self.vertices.remove(edges[i - 1].end) # vertices[i]
            print(len(edges), i)
            edges.remove(edges[i])
            edges.remove(edges[i - 1])
            i -= 1
            edges.append(Edge(self.vertices[i], self.vertices[i + 1]))
         i += 1
      
      self.n_sides = len(self.vertices)

      # ! Create first the last edge and then check if the previous one is inside it   
      edges.append(Edge(self.vertices[i], self.vertices[0]))
      if edges[i].slope == edges[i - 1].slope:
         self.vertices.remove(edges[i - 1].end)
         edges.remove(edges[i - 1])
         edges.remove(edges[i])
         i -= 1
         edges.append(Edge(self.vertices[i], self.vertices[i + 1]))
      
      if edges[i].slope == edges[0].slope:
         self.vertices.remove(edges[i].end)
         edges.remove(edges[i])
         edges.remove(edges[0])
         i -= 1
         edges.append(Edge(self.vertices[i], self.vertices[0]))

         
      return edges
         
   
if __name__ == "__main__":
   v1 = Vertex(2, -1)
   v2 = Vertex(3, -1)
   v3 = Vertex(3.5, -1)
   v4 = Vertex(9, 0)
   v5 = Vertex(7, -1.25)
   v6 = Vertex(10, 2)
   v7 = Vertex(1, 3)
   v8 = Vertex(2, 6)
   v9 = Vertex(12, 4)
   v10 = Vertex(10, 10)
   v11 = Vertex(10, 10)
   shape1 = Shape(v1, v2, v3, v4) # ! Triangle: error. Probably has to do with a vertex being max and max or min and min