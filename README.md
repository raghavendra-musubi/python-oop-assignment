# python-oop-assignment

Python OOP assignment and problem statement for pre-Django python learning

### Relevant OOP Topics 

- instantiating
- attributes
- methods
- inheritance 
- method overriding

***

## PART A 


### Problem Statement

- here, the goal is to build a OOP based system framework to manage school members
- two types of members can belong to the school    
    - students 
    - employees

- use OOP concepts to create the framework of this system


#### Parent Class

- create a parent class which is an more generic school member
    - make this parent class have attributes and methods common to all school members 

- attributes of the parent class `Person`
    - Full Name
    - Age
    - Gender
    - Email 
    - Phone Number
    - Roll Number


#### Children Classes

- `Staff`
    - additional child class attributes:
        - role
        - hours worked
        - hourly wage
    - method:
        - calculate pay
- `Student`
    - additional child class attributes:
        - level
        - test score
    - method:
        - check if student passes (test_score more than 5)
- `Teacher`
    - additional child class attributes:
        - subject
        - weekly salary
        - weeks worked
    - method:
        - calculate weekly salary 


***

## PART B

### Problem Statement

**polygons**

- a polygon is a plane figure that is described by a finite number of straight line segments connected to form a closed polygonal chain or polygonal circuit
    - the solid plane region, the bounding circuit, or the two together, may be called a polygon

- the segments of a polygonal circuit are called its edges or sides
- the points where two edges meet are the polygon's vertices (singular: vertex) or corners

**simple polygons**

- a simple polygon is one which does not intersect itself

- consider the following simple polygons 
    - `triangle`
    - `rhombus`
    - `pentagon`
    - `hexagon`

#### Parent Class

- polygon with three blank instance methods:
    - return number of sides 
    - compute area 
    - compute perimeter


#### Children Classes

- override the parent methods to: 
    - return number of sides 
    - compute area 
    - compute perimeter

