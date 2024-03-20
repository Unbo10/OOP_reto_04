# OOP_reto_04

```mermaid

classDiagram
direction BT

    class Vertex {
        + x: int
        + y: int
        + compute_distance(self, Vertex)
    }

    class Edge {
        + start_vertex: Vertex
        + end_vertex: Vertex
        + length: float
        + associated_line: Vectors
        - compute_inner_angles(Edge): ~float~
    }
    Edge *-- Vertex

    class Shape {
        # is_regular: bool
        # n_sides: int
        # vertices: list(Vertex)
        # edges: list(Edge)
        # inner_angles: list(float)
        # perimeter: float-abstract
        # area: float-abstract
        + get_shape_vertices(self)
        + get_shape_edges(self)
        + get_inner_angles(self)
        + get_perimeter(self)
        + get_area(self)
        # eliminate_repeated_vertices(~Vertex~)
        # sort_not_passed_vertices(Vertex, ~Vertex~)
        # create_vertices(self)
        # create_edges(self)

        # is_shape_regular(self): bool
        # compute_area(self): void-abstract
        # compute_perimeter(self): void-abstract
        # compute_inner_angles(self) : ~float~
    }

    Shape *-- Edge
    Shape o-- Vertex
    Triangle --|> Shape
    Rectangle --|> Shape

    class Triangle {
        # compute_perimeter(self): void-abstract
        # compute_area(self): void-abstract
    }
    Isosceles --|> Triangle
    Equilateral --|> Triangle
    Scalene --|> Triangle
    RightTriangle --|> Triangle


    class Isosceles{
        # compute_perimeter(self): float
        # compute_area(self): float
    }

    class Equilateral{
        # compute_perimeter(self): float
        # compute_area(self): float
    }

    class Scalene{
        # compute_perimeter(self): float
        # compute_area(self): float
    }

    class RightTriangle{
        # compute_perimeter(self): float
        # compute_area(self): float
    }

    class Rectangle{
        # compute_perimeter(self): float
        # compute_area(self): float
    }
    Square --|> Rectangle

    class Square{
        # compute_perimeter(self): float
        # compute_area(self): float
    }
```