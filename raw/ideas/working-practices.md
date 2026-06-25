# Refactoring

#### Tips
1.	Evita el refactor, es la última instancia.
2.	El patrón de Façade es el que más te protege.
3.	Posterior a las fachadas crea micro-sistemas basados en eventos para que el impacto en el código viejo genere outputs en data en la nueva estructura.
4.	Haz todos los tests que te sean posibles para conocer lo que funciona bien y mal del sistema legacy.
5.	No arregles bugs legacy, hazlo bien a la primera en el sistema nuevo.
6.	Ninguna estrategia de migración que al final del día NO sea transparente para el cliente es buena.
7.	No te mates estimando, en cada paso te van a salir cosas inesperadas completamente por lo general.
8.	No hagas el refactor salvo que la vida del producto dependa de eso, no es joda. Casi ningún refactor vale la pena.

#### Pasos
1. hace un branch refactor-master
2. dividí el core en pequeñas partes, hace un branch por parte que vas tocando.
3. refactoriza una parte usando LLM, revisá. iterá de nuevo.
4. pedile al LLM que te haga tests de lo que necesites para que eso funcione
5. una vez que funciona, mergea eso a refactor-master.

Siendo un módulo core, con deuda que impide evolucionar y testear, la estrategia que me funcionó en escenarios así es un refactor incremental orientado a testeabilidad, con facade y “strangler pattern” para no exponer al cliente a riesgos.

Muchos de mis refactors en legacy los hice aplicando técnicas de "Working Effectively with Legacy Code" (Michael Feathers), con el objetivo principal de volver el código testeable. Una vez que la zona donde va la nueva feature es testeable, podés introducir el cambio con confianza.

Cómo priorizar y avanzar de a poco:

- Priorizar por impacto en el negocio y frecuencia de cambio
- Hacer una limpieza inicial en la zona objetivo siguiendo "Tidy First" de Kent Beck
- Recién ahí aplicar técnicas de Feathers para abrir seams y desacoplar (introducir interfaces, inyección de dependencias, expand/contract)

"Es como entrar a un baño público, querés tocar lo menos posible." My two cents hacete amigo del debugger y ejercitá en tu local los flujos más comunes. Fijate un commit que haya resuelto un P0 ó P1 y buscá los logs de esa ejecución y tratá de entender porque se dió esa situación y porqué el fix funcionó.

#### Libros
- Working Effectively with Legacy Code
- Refactoring: Improving the Design of Existing Code - Martin Fowler

# Codebases

- https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge
- https://deepwiki.com | chat with a repo
	- prompt: explain like i'm five this code using axioms towers where each block (theorems) is built upon something else until you reach the base axiom or cornerstone of the program
	- examples: 
		- https://deepwiki.com/facebook/react
		- https://deepwiki.com/nodejs/node

## Diagrams

- https://medium.com/@kanishks772/from-code-to-diagram-in-seconds-the-lazy-developers-guide-b48987837bd3
- https://medium.com/@kanishks772/auto-updating-diagrams-the-magic-behind-git-push-30d1c7d80b84

## Documentation

- https://www.breathe-doc.org/ | https://breathe.readthedocs.io/en/latest/
- https://passo.uno/docs-as-code-topologies/

# Systems Theory

**A good system:**
- Has reproducible builds
- Has simple deployment
- Has deterministic tests
- Has clear documentation

**When designing any system, ask:**
- What is the simplest version that works?
- Where will this break first under load?
- What can be async?
- What happens if X fails?
- Am I adding complexity or solving a real problem?

The best people aren’t thinking “I’m a software engineer.” They’re thinking like builders. They look at problems, understand users, and define solutions with clear judgment. The code is just the execution layer.

## Theory of Computation

### Axiom Towers

You can see a system like an axioms tower where blocks, or theorems, are built one upon another. The axiom is the cornerstone and then you theorize hypothesis (theorems) from that base axiom and try to build them keeping a supportive, loose, cohesive and coherent relationship between each one of them.

For example, multiplication is built upon addition. The same is for kinds of numbers (natural, rational, imaginary, etc, etc). Computers operate on binary (on, off, add, subtract) and everything else is built upon these two operations.

We can extrapolate this to every aspect of software engineering: micro services that work with each other, frontends, dependencies, components, classes, services and endpoints, etc, etc. We must see beyond the immediate impact and surface when creating and modifying pieces of our systems and make sure that what we are doing does not affect and is in sync with every other piece, otherwise we risk crumbling it all and, sometimes, silently, which is even worse.

### Rules & Constraints

When operating within a given system we do so by following certain rules and having in mind certain constraints. But how are these represented? With symbols, but these same symbols don't mean anything without the rules and the rules only make sense and can be represented in terms of symbols.

Think of computers that paint pixels (characters) in the screen while we are typing. They make sense because of the meaning we give them as symbols; language itself. But for a more down to earth analogy, think of programming languages, architecture and design patterns, software frameworks, that we use and implement while programming.

They make sense within a certain context, with a certain set of rules and under certain constraints. We call this function because of what it does in a given language or library. We implement this pattern because of what it might give us. We use this or that framework because it has certain features that fits our use-case.

But also we have to take into account what we can do, what we are allowed to do. We can't run modern programs in old computers, we can't expect to train an AI model of industrial scale on a CPU. This discernment usually paves the way for everything else.

We have to know where we are standing, what tools we have and what we want to do. Then we can make a decision.

Nevertheless, theorems (blocks) are discovered, not invented (specially for math), and for that we have to try things, new things. Experiment. That's how axiom towers are built, and new sets of rules and constraints come to life.

Question the common sense of things, strip everything down to its fundamentals, to what we know is undeniably true. This is tackling problems from first principles, to reduce complexity, to refuse anything that cannot be independently verified and rebuild our understanding from the ground up. This way we can build, create new things.

### Axiom Towers: Computation

Like the axioms proposed for math by Peano, computation had its own proposed by **Alan Turing**, **Alonzo Church** and **Kurt Gödel (recursive functions)**, circa 1930. We will focus on the first two: Turing Machines and Lambda Calculus.

They were proposed at roughly the same time and try to represent the same thing, the computation of an algorithm (a set of instructions to reach a desired result/state). They differ in how they do it, meaning, in the rules they apply:

#### Turing Machines
	
- it's like a tape with contiguous boxes one next to each other, starts blank with a list of 	instructions
- it has a HEAD (a box) that holds the initial value
- boxes can be marked and unmarked (X), i.e modifying the tape (state)
- depending on if the box is marked/unmarked (state), go to N (jump, goto), i.e state determines how the program jumps/runs
- the behavior of the program is changed with every tape/state modification
- to reason about the behavior of the program one must understand the state of the tape at every moment of modification
- HEAD can be moved to left and right
- you could think of it like a linked list
- created by Alan Turing

##### Turing Machines Tower

What we have today was mainly built upon Turing Machines, but Von Neumann model is considered the base axiom. Turing Machines are so popular because VN Instructions are easily implementable in hardware (efficient).

The tower would be something like this:

	C++ (1985) - Classes, Objects
	C (1972) - Functions, Structs, Malloc
	Fortran (1957) - If Statements, Loops
	Assembly (1949) - Human Readable, Primary Instructions (ADD, SUBTRACT, MULTIPLY, DIV)
	Von Neumann Model (1945) - VN Instructions
	Turing Machines (1936) - TM Instructions

#### Lambda Calculus
	
- minimal set of rules:
	- programs are expressions (aka lambda terms or λ-terms)
	- expressions can either be a named variable, a function (formally called an abstraction), 	or 	a function call (formally an application)
- a more functional approach, literally you just built everything with functions
- declare a function
- call a function
- modify the parameters/arguments of a function by currying to make it more modular and reusable (calling a function returned from another function)
- recursion not allowed, although the Y Combinator, a higher-order function (a function that takes a function and returns a function) in functional programming, enables recursion in anonymous functions
- can be used to represent minimal models of Turing Complete machines
- created by Alonzo Church

##### Lambda Calculus Tower

Lambda Calculus is the Assembly of functional programming, but it's hard to implement in hardware.

	React (2013) - View is Pure Function of State
	Elm (2012) - Flux/Redux Pattern
	Haskell (1985) - Pure
	ML/OCAML (1973) - Pattern Matching
	System F (1972) - Lambda Calculus with Types
	LISP (1958) - Meta-Circular, GC
	Lambda Calculus (1936)

You could say that React is to jQuery what Lambda Calculus is to Turing Machines:

- jQuery
	- the DOM is your state
	- anything can make modifications to the DOM
	- the DOM ends up in unexpected states because of unforeseen state modifications
- React
	- the state is explicitly defined
	- your view is a pure function of state
	- you don't modify state, you create new state

React's constraints make it easier to reason about state and the DOM. Functional programming's constraints make it easier to reason about programs.

If an algorithm can be encoded as any of these two, then is computable. With any of the two you can represent a (computable) program in a computer. 

It's said that a machine"is Turing Complete" when it can simulate a **Turing Machine** and represent any algorithm that is computable, for example **Conway's Game of Life**. The same can be said of programming languages, like general purpose languages. The opposite are DSL (Domain Specific Languages) that serve to a very specific endeavor, goal or domain.

**Lambda Calculus** has no tape (state), all you have are input arguments to functions. Functions are pure, like in math, i.e with the same input you always get the same output (deterministic). All values are immutable, though you can generate new values from existing ones. There are no loops (requires modifying counter variables), so recursion is used instead. And finally functions are your unit of composition, and because there is no global state, it's much easier to reason about (composition).

So, **Turing Machines** and **Lambda Calculus** are equivalent:

- Turing Machines can be rewritten as Lambda expressions
- Lambda expressions can be rewritten as Turing Machines
- they also are equivalent to recursive functions

### Resources

- https://medium.com/@tjspradling/what-the-heck-is-lambda-calculus-8e21466b87c6
- https://dev.to/marciofrayze/why-is-elm-such-a-delightful-programming-language-2em8

## Computer Architecture

### Von Neumann Architecture

This axiom came around 1945, designed by physicist **John Von Neumann**. It's a foundational computer design where program instructions and data are stored together in the same memory. It consists of a CPU (with an ALU and Control Unit), memory, and input/output devices, operating sequentially via a single bus. Despite being developed in the 1940s, this design remains the basis for most modern general-purpose computers (servers, desktop, laptop, mobile devices, microcontrollers).

**Instructions**

- load X from memory cell P
- store X to memory cell P
- add, subtract, multiply
- if memory cell P = 0, go to N
- if memory cell P != 0, go to N

The main characteristics are:

- **Shared Memory**: Both data and instructions are stored in the same main memory (RAM)
- **Central Processing Unit (CPU)**: Comprises an Arithmetic Logic Unit (ALU) for calculations, a Control Unit (CU) to manage instructions, and registers for temporary storage
- **Sequential Execution**: The CPU fetches, decodes, and executes instructions one at a time (the instruction cycle)
- **Input/Output (I/O)**: Mechanisms to connect the computer with external devices (keyboards, mouses, etc)

### The Von Neumann Bottleneck

A critical limitation is that the CPU can only perform one instruction or data fetch at a time because they share the same bus. This, known as the Von Neumann bottleneck, means that processing speed is often limited by memory access times, especially when data transfer is slower than computations, often limiting efficiency in modern applications.

Some solutions or workarounds are optimizing caching (closer to the CPU), designing processors with greater bandwidth and new architectures that process data within memory, avoiding data transfer.

Today, almost all modern computers utilize a multi-bus architecture. While early computers often used a single system bus, modern high-performance systems require multiple, specialized buses to prevent data bottlenecks and allow simultaneous operations between the CPU, memory, and peripheral devices.

### Multi-Bus Architecture

This is the standard today:

- **Performance Bottleneck Elimination**: A single bus creates a "bottleneck" because only one device can send data at a time. Separating memory, I/O, and peripheral traffic onto separate buses allows simultaneous communication, greatly increasing speed.
- **Separation of Speeds**: High-speed components like RAM (using a dedicated memory bus) need to communicate much faster than slow components like hard drives or USB ports (which use peripheral buses like PCIe or SATA).
- **Internal vs. External Buses**: Modern computers distinguish between an internal/local bus (for communication between the CPU and cache/memory) and external/peripheral buses (for connecting to peripherals).
- **Modern Interconnects**: Classic system buses have been replaced in modern computers by high-performance technologies like PCI Express (PCIe) and Intel QuickPath Interconnect (QPI) or similar technologies that facilitate multiple parallel communication paths

**Key Takeaways**:

- **Multi-bus is standard**: Even small embedded systems or smartphones often use multiple bus structures internally (e.g., AHB/APB buses in ARM architecture).
- **Specialized Buses**: Computers use specialized, high-speed buses for data-intensive tasks (memory bus) and different buses for input/output.
- **Von Neumann remains**: Despite using multiple buses for speed, most computers still follow the general [Von Neumann architecture], where data and instructions share the same memory, but this memory is accessed through optimized, complex bus structures

### Resources

- https://www.youtube.com/watch?v=ziMRjDlLEwo&list=PL5Q2soXY2Zi-LfDdGgWyLcTSqzm6a26wD&index=3
- https://medium.com/@ckekula/computer-architecture-for-beginners-interconnection-structures-d4c851c655f2
- https://medium.com/@ckekula/computer-architecture-for-beginners-interconnection-structures-part-2-d12ebf7c2806

## Interfaces Define System Throughput

**A system is only as fast as:**
- how quickly it accepts input
- how efficiently it produces output

**You don’t scale systems — you scale interfaces.**

- Every request must pass through an interface
- Every response must pass back through it

**Examples:**
- APIs
- UI interactions
- message queues
- DB queries
- service boundaries

**A good interface minimizes what needs to be said**


### Anti-patterns

- Overloaded endpoints
- Huge payloads
- "Do-everything" APIs

**Better:**
- Precise contracts
- Small, purpose-built inputs
- Predictable outputs

**This reduces:**
- serialization/deserialization cost
- validation complexity
- mental overhead for developers

## Data Transfer

**Moving data is often more expensive than computing it**

**Interfaces should:**
- minimize data transfer
- avoid unnecessary hops
- compress or aggregate when possible

**Problems:**
- latency accumulation
- network overhead
- failure amplification

**Fix:**
- batch operations
- coarse-grained endpoints
- server-side aggregation

**Stop thinking “how do I optimize my code?”**
**Start thinking “how do I design better boundaries?”**
**“How can I reduce round trips?”**

## Testing as a first-class design constraint

Testing isn’t something you add later.

**Good systems:**
- Are designed to be testable
- Use deterministic inputs/outputs

**Patterns:**
- Pure functions where possible
- Replayable logs
- Property-based testing

## Determinism > “eventual consistency magic”

Deterministic systems are easier to test and reason about

**Non-determinism (timing, concurrency, retries) introduces chaos:**
- Async retries
- Distributed race conditions

**Better:**
- Ordered logs
- State machines
- Explicit sequencing

## Explicit Failure

**Simple Systems:**
- Fail in predictable ways
- Are easy to debug
- Define invariants
- Handle errors explicitly
- Avoid implicit retries / hidden async behavior

**Complex systems:**
- Fail in emergent, non-obvious ways

## Big O

We should aim to consume the least memory possible and perform our operations in the least time possible. Big O measures these things. Basically best to worst:

- O(1) - constant time
- 0(log n) - logarithmic
- O(n) - polynomial
- O(2^n) - exponential

So every time we are designing an algorithm we should aim to do it at O(1). Of course, often times this is not possible due to certain constraints, such as some operations are predetermined to be at this or that. But we must always avoid exponential and polynomial when we can. Logarithmic is like divide and conquer, usually implemented in sorting algorithms (binary searches).

## Resources

- https://blog.juliobiason.me/thoughts/things-i-learnt-the-hard-way/
- https://github.com/lambdaclass/lambdaclass_hacking_learning_path | tools, good practices
- https://matklad.github.io/2024/03/22/basic-things.html
- https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods
- https://ferd.ca/a-distributed-systems-reading-list.html
- https://ferd.ca/lessons-learned-while-working-on-large-scale-server-software.html
- https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing
- https://lawsofsoftwareengineering.com



# Object-Oriented Programming

- https://blog.sigma-star.io/2024/01/people-dont-understand-oop/

## Abstractions

Yo creo que deberías usar firmemente "es-un" cuando es un subtipo del mundo físico, y "tiene-un" cuando es un compuesto del mundo físico. Así que no, no estoy de acuerdo con que la herencia apeste la mayor parte del tiempo o que tenga que haber una "muy buena razón" para usarla. Creo que son enfoques equivalentes sin nada especial en ninguno de los casos, y deberías usar la herramienta correcta para el caso específico.
Dicho esto, resulta que nuestro mundo tiene naturalmente mucha más composición que herencia, por lo que una regla tonta como "prefiere la composición a la herencia" funciona la mayor parte del tiempo y la herencia parece ser la "excepción". Así que sí, el resultado final es que la herencia es rara y la composición es la predeterminada, pero esa no es una propiedad inherente del modelo de diseño.
Así que para la gente que no entiende las relaciones es-un/tiene-un correctamente desde un punto de vista físico, sí, es mejor simplemente usar la composición siempre que sea posible para cometer la menor cantidad de errores posible. Pero eso se basa solo en estadísticas para reducir las posibilidades de cometer un error, y desde el punto de vista de la física no hay nada especial en ninguno de los casos.
Ahora, esto a menudo es exagerado y te das cuenta de que en realidad no quieres modelar el mundo real con demasiada precisión porque llevaría a mucho trabajo y código extra (porque el mundo real tiene alta complejidad), pero en ese punto necesitas dibujar los límites de dominio adecuados y no culpar a la POO por tus malas decisiones.
Por ejemplo, desde una perspectiva contable, en realidad no te importa si los trabajadores son humanos en primer lugar, para lo que te importa podrían ser extraterrestres o robots. Lo que realmente te importa son los contratos y la identificación (como el número de la seguridad social) y los roles dentro de la empresa. En este punto, no hay ninguna razón para tratar de modelar un Humano biológico en tu código, y por lo tanto, una vez más te deshaces del problema de la herencia.
TL;DR: No es la herramienta la que está rota, son los usuarios.


## Arch & Design Patterns

- https://www.youtube.com/watch?v=sSpULGNHyoI | architecting large software projects
- https://refactoring.guru/design-patterns
- https://third-bit.com/sdxjs | software design by showing how to build the tools that programmers use every day using JavaScript

### Patterns

Most used: strategy pattern, builder pattern, observer pattern, DI pattern. 95% of software development is the first two and then you add a little bit of last two, more often DI.

Basically you prototype something, simple, and then you see where it could and/or went wrong. Interface most things for external interaction and create factories, then do strategy pattern for implementing those interfaces and factories in different classes and objects respectively. All loosely-coupled.

Program to abstractions, i.e to interfaces, which are high-level control layers for certain entities. This layer is not supposed to do anything but delegate the work to the implementation layer, AKA, the platform.
Note that we’re not talking about interfaces or abstract classes for a programming language. When talking about applications the abstraction can be represented by a GUI (on desktop, browser) and the implementation could be the underlying OS code or an external API, which the GUI layer calls in response to user interactions.

All these patterns help us to separate the code, make it more readable and extendable. Also, in this process, we incur in less errors for changing large classes, i.e breaking existing working code, having merge conflicts, etc.

#### Creational Patterns

##### Factory

Allows us to create different objects from a super class using a sub classes, e.x: Logistics -> RoadLogistics, SeaLogistics.

It comes handy when having to work with different but adjacent abstractions (objects) and we want to have the creation logic in one place. It can also serve to return existing objects in store (memory, database, cache).

Could implement builder pattern instead of factory pattern too, depending on the use case: e.x a highly composable object (let client choose what to add), which also is more loosely-coupled: It helps to avoid the rigid coupling and potential side effects that can arise from complex inheritance trees, which often leads to more brittle and difficult-to-manage systems as they scale. 

##### Abstract Factory

Allows us to create related objects without knowing their exact class, e.x UI components (buttons, modals, etc) corresponding to a certain OS.

Given a certain configuration we choose this or that factory, which uses the methods of the abstract factory, which in turn return abstract object interfaces (Button, Modal, etc) and that’s all the client code sees. Each concrete factory creates its concrete objects. Then we can easily extend this with more factories without breaking client code.

This pattern can be implemented as a Singleton, as also can the configuration object. Use it when a factory is doing more than a single thing (SRP), or you could just create another standalone factory.

##### Builder

Allows us to create highly composable objects and avoid the abuse of sub classes and inheritance resulting in simple hierarchies and loose coupling. It’s often used when multiple representations of an object are needed by client code, e.x a house, a hamburger, a car. Also to avoid “telescopic constructors” and ugly client code function calls to builder classes. On the other hand, it can increment the code’s complexity by adding builder interface, director classes and concrete product builder classes.

Usually one evolves from simpler patterns such as factory and abstract factory to this one. In the building process one can omit build steps and even create composite trees by calling recursively specific builder methods. The director class lets us take a specific builder and execute a sequence of predefined steps (usually for common products), although the result type to return it’s defined by concrete builders as we can have different types that not match a unique interface. 

It can be complex but once we have it adding more products/variants of the same object it’s pretty easy, following the Open/Closed principle for extending what it’s already working without breaking client code. This pattern can be easily implemented with the Bridge pattern by having to separate hierarchies, abstraction and implementation, being independent from each other. This saves us from having to implement several sub classes by splitting large classes.

##### Singleton 

Can be a good thing, but most of the time you don’t need it. Use cases can be when you need your app/system to behave in certain ways/have a certain role/have certain features, and you mix it up with the strategy pattern. For example, it could work with a database configuration instance: it’s always the same, unique and global; on the other hand it could not work with shopping carts as there can be several of them (for each user) and they need to be isolated. Bottomline it lets you create an object with a unique instance that is globally accessible, but not editable (constructor method is private).

#### Structural Patterns

##### Adapter

It’s just strategy pattern. You choose to use something else (interface) to fit your use case, e.x you have data in XML format but using a library for analytics that takes in data in JSON format, so you implement an adapter to transform the data format. Use it when you want to use an existing (service) class but its interface it’s not compatible with the rest of your code (client classes), or when you want to reuse several existing sub classes that lack some common functionality that can’t be added to the super class. In this cases the service class are usually 3rd party, legacy or has lots of dependencies. Note that sometimes it’s easier to just change the service class to match the other classes.

- Object Adapter: client code and service code through the implementation of an adapter interface: client -> adapter (wraps object to match the service) -> service. This is easily extensible by creating new adapters while not breaking the client code.

- Class Adapter: the adapter inherits interfaces from both objects at the same time. This is only possible in languages that support multiple inheritance such as C++. Here the object is not wrapped and the adaptation happens within the overridden methods

##### Bridge

Lets us develop two or more related classes independently, i.e, we won’t end up growing exponentially our hierarchies through inheritance. This pattern favors composition over inheritance.
For example, if we have `Shape` and then sub classes `Circle` and `Square`, and then we add color classes, we will end up having `RedCircle`, `RedSquare`, `BlueCircle`, `BlueSquare` and so on growing exponentially.

So this pattern helps us with that by developing “abstractions” and “implementations”, each by their own side (classes), splitting large-would-be classes into separate hierarchies/dimensions. This works by linking a reference object in the abstraction to the implementation’s interface, in this case a color, avoiding inheritance and a consequential large hierarchy. This way we can have red and blue circles and squares, with shapes and colors each by their own side.

Use it when you want to divide and organize a monolithic class that has several variants of some functionality, when you need to extend a class in several orthogonal, independent dimensions, when you need to be able to switch implementations at runtime. It lets us create cross-platform apps and the client code works with high-level abstractions and is not exposed to platform details. But have in mind that you could make more complicated an already highly cohesive class.

You can combine this pattern with Builder: the director class plays the role of the abstraction while different builders act as implementations. This pattern it’s also designed upfront usually.

##### Facade 

Not really a pattern, more like just good programming; e.x: a http request to a server that returns a json, you just see the response but lots of things got done to deliver it. A method that does a cool thing, a system, an app. It’s more like an abstract concept for coding better. Defines a new, simpler interface for an existing object.

#### Behavioral Patterns

##### Strategy

A behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class and make their objects interchangeable. Basically it lets you take a big class that does something specific in a lot of different ways and extract all of these algorithms into separate classes called strategies.

The original class must have a field for storing a reference to one of the strategies, through which delegates the work to a linked strategy object instead of executing it on its own. But note that this class is not responsible for choosing an appropriate strategy, instead, the client passes the desired strategy to it. In fact this class does not know much about strategies, it works with them all through the same generic interface, which only exposes a single method for triggering the algorithm encapsulated within the selected strategy. This way you can easily add new strategies or modify existing ones without changing an entire class.

It allows picking and choosing components for your architecture and DI pattern enables it; it’s making the thing into an interface: program below the interface, program at an interface level.
This pattern defines a family of interchangeable algorithms (strategies’ methods) and allows selecting one at runtime (specific methods implementations), eliminating conditional logic blocks.

Strategy Interface/Abstract Class: Defines a common contract (method signatures) that all concrete strategies must follow. TypeScript interfaces are ideal for this.

Concrete Strategies: Classes that implement the strategy interface, each providing a unique implementation of the algorithm or behavior. These are often injectable services in NestJS.

Use it when: 
- you have a big class that has a lot of conditional logic, that does the same thing in different forms
- you want to switch between algorithms/flows at runtime
- when you have several similar classes that only differ in the way the execute some (the same) behavior
- to isolate business logic of a class from the implementation details of strategies that may not be as important in the context of that logic

Do not use if you only have a few algorithms that rarely change, since it overcomplicates the code with new classes and interfaces.

This pattern is very similar to Bridge, State and to some degree to Adapter since all of them are based on composition, which is delegating work to another object.

##### State 

Can be considered as an extension of this pattern; both are based on composition: they change the behavior of the context by delegating some work to helper objects. Strategy makes these objects completely independent and unaware of each other. However, State does not restrict dependencies between concrete states, letting them alter the state of the context at will.

##### Observer 

Lets us “monitor” the state of a given object, AKA publisher, and let other objects, AKA subscribers, know about it. This is common for event-driven architectures and this pattern is the core of event-sourcing (tracing sequences of immutable events/state changes that composes the complete history of the system). This way we can know where, how and when objects modified their state, making it useful for highly-audited data (finance, transactions, inventory, etc). 

It’s useful when we want to let some classes know about the state of another class and maybe perform some kind of operation. For this usually we create a “publisher” class and have it communicate with “subscriber” classes through a common Subscriber interface which usually has an “update” abstract method. This way we can add more (concrete) subscribers and they will all work if using the common interface. This pattern is similar to Command, Mediator.

This usually goes hand in hand with CQRS architecture pattern where command (writes) are segregated from queries (reads), this we can easily scale up one or the other, depending on our app’s needs. It also allows us to emit a “write” event when we have writes so our reads database gets updated with the new data (there specific databases for writes and reads).

Tip: with event-driven we can count how much writes and reads we have on our app and make a (scale) decision based on that data.

##### Decorator 

Lets us add new behaviors to objects, it enhances them without changing their interface. 

##### Proxy 

Allows us to perform certain actions before or after client code has any contact with a given object.

##### Iterator 

You can traverse different collections (data structures) in different fitting ways. Also you hide the collection itself from the client.

### Tips

- A class should do one thing, just like functions, no god-methods or god-classes. Here come interfaces and strategies.
- Check design and architecture patterns on learn.txt


## Code Reuse

According to Erich Gamma, three levels of reusability: 

- low-level: classes, interfaces, containers, iterators
- mid-level: patterns
- high-level: frameworks

Patterns are the sweet spot because they are solutions to common problems but adaptable and extensible enough to implement in almost any language or context
Classes are too small and would not adapt to many scenarios. On the other hand, frameworks are a high-investment endeavor.

### Semantic Compression

According to Casey Muratori one should program with a compression-oriented approach:

Semantic Compression - https://caseymuratori.com/blog_0015

The author defines efficiency not as code performance, but as the minimization of total human effort across a code’s entire lifetime—from typing and debugging to modifying and adapting.
To achieve this, they advocate for compression-oriented programming, a bottom-up methodology where code is treated like a semantic compressor (e.g., PKZip). The goal is to make code semantically smaller by eliminating duplication and similarity, rather than merely reducing text length, although these two tend to go hand in hand.
The Methodology
	1	Start Concrete, Not Abstract: Instead of designing architectures or abstractions upfront, the programmer begins by writing specific, working code for each individual case without worrying about correctness or reuse.
	2	The "Two Instances" Rule: Reusability is only introduced when a pattern appears at least twice. The mantra is: “make your code usable before you try to make it reusable.”
	3	Avoid Premature Reusability: Attempting to write reusable code before having concrete examples (or with zero examples) leads to incorrect abstractions, wasted effort, and cumbersome modifications.

Why It Works
By waiting for two real-world examples, the programmer ensures the abstraction is grounded in actual needs, preventing architectural mistakes. This approach results in code that is:
	•	Easy to read (minimal content mirrors the problem’s language).
	•	Easy to maintain (identical operations share the same path).
	•	Easy to extend (common operations are already composed and available).

Unlike traditional methodologies that rely on upfront diagrams or class hierarchies, compression-oriented programming starts with details and compresses them into architecture, avoiding the pitfalls of predicting requirements prematurely.

In his own words:

I look at programming as having essentially two parts: figuring out what the processor actually needs to do to get something done, and then figuring out the most efficient way to express that in the language I’m using. Increasingly, it is the latter that accounts for what programmers actually spend their time on: wrangling all those algorithms and all that math into a coherent whole that doesn’t collapse under its own weight.

So any experienced programmer who’s any good has had to come up with some way  —  if even just by intuition  —  of thinking about what it means to program efficiently. By “efficiently”, this doesn’t just mean that the code is optimized. Rather, it means that the development of the code is optimized  —  that the code is structured in such a way so as to minimize the amount of human effort necessary to type it, get it working, modify it, and debug it enough for it to be shippable.

### Clean Code VS SC

- https://www.computerenhance.com/p/clean-code-horrible-performance

Casey Muratori's article argues that several popular "clean code" principles—specifically preferring polymorphism to switches, hiding implementation details, and forcing tiny single-purpose functions—have a severe, measurable negative impact on runtime performance.
Using a shape area calculation example, he demonstrates progressive performance degradation:
	•	Polymorphic (virtual) approach: ~35 cycles/shape
	•	Switch-based approach: ~24 cycles/shape (1.5x faster)
	•	Table-driven approach: ~3 cycles/shape (over 10x faster)

He's criticizing:
	◦	Virtual/Dynamic dispatch overhead in tight loops (virtual functions resolved at runtime through vtables, mapping addresses, return values in stack), you could use inline/anonymous functions, though this does not matter much in JavaScript/React since this is already optimized by V8 (or whatever browser engine): the JIT compiler decides at runtime whether to replace a function call with the actual function body to reduce call overhead
	◦	Pointer indirection from arrays of polymorphic objects (destroying cache locality)
	◦	Forcing every operation into a separate translation unit (preventing optimization)

He concludes that these "clean" rules can erase a decade or more of hardware gains, and that organizing code by operation (functions that act on plain data) rather than by type (class hierarchies) enables both better performance and often simpler, more maintainable code.
The article is a powerful demonstration that if performance matters, certain "clean" rules are actively harmful in low-level environments like game engines, high-frequency trading, storage engines, embedded systems, data processing pipelines, etc. But for many business applications, CRUDs, web apps, the performance difference doesn't matter and is irrelevant compared to database latency, network I/O, or developer productivity. In those domains, encapsulation and polymorphism are perfectly reasonable choices, and the organizational benefits of abstractions, encapsulation and polymorphism outweigh the costs. Some things to have in mind:
	◦	Persistence and schema constraints: If you're building against a database, your data layout is heavily constrained by ORM patterns, migration costs, and existing schemas. You can't always "flatten" your types the way Muratori does.

	◦	Collaboration: Semantic compression relies on one person (or a tightly aligned team) recognizing duplication across the codebase. In large teams, localized "compression" in one area may conflict with needs in another, leading to brittle shared code.

	◦	Emergent patterns: Sometimes you genuinely don't know the right abstraction until you have 5 or 6 instances, not just 2. The "wait for two" rule can lead to a sprawling mess that's harder to compress later because the duplication is now spread across dozens of files with minor variations.

	◦	Business reality: Most business software is built top-down—requirements, architecture design, then implementation. Pure bottom-up is often not feasible given deadlines, fixed budgets, and the need for predictable outcomes

The most practical synthesis is to apply semantic compression and data-oriented design in performance-critical layers, while using OOP and encapsulation for boundaries, interfaces, and areas where flexibility and team coordination matter more than raw speed. They are not mutually exclusive—they are tools for different contexts.


## Extensibility

Programs will change. So if we see some parts of the program that could grow over time, it’s better to build with this in mind and program to interfaces and isolate what’s likely to change. Have classes that do one thing so the code is searchable and readable, also if a class grows too big divide it into sub classes, same for interfaces.

## Basic Design Principles

- encapsulate what varies: if something is likely to change over time, isolate it, could be method-wise, class-wise. Encapsulation: binding state and methods together (classes), only object itself has access to internal state
- program to an interface,  not to an implementation: this way you have loosely-coupled components and weaker dependencies between objects. Tip: look for what is used in two or more objects/classes, then build an interface.
- favor composition over inheritance: this gives us more flexibility and extensibility, and more options for clients during runtime, also we don’t have to implement all the superclass’ methods (possibly we don’t need all)
- implement polymorphism when you can, static (compile-time) or dynamic (runtime) binding as you see fit. This have a lot to do with interfaces and abstractions as an object can behave differently depending the scenario (methods)

## SOLID

### SRP (Single Responsibility Principle)

A class/method should do one thing

### Open/Closed Classes

Open for extension, closed for modifications: extend a functionality, fix a bug. but don’t break working code for existing clients

### Liskov Substitution Principle

In most statically typed languages these are built-in.

- a sub class methods and their parameters should work with all existing clients of the superclass. Tip: sub class parameters should be the same or more generic than those of the superclass. This is specially important for libraries/apis because you don’t know what object a user /client will pass as argument
- a sub class return type should be an exact match to the super class or a sub type. E.x: if a client expects a Cat object, the sub class should return a) Cat object or b) BengalCat (sub type, still a Cat so it’s OK)
- a sub class should not strengthen pre-conditions as it could break previously working objects of the super class
- a sub class should not weaken post-conditions as it could lead to unknown and unexpected behavior for an existing client
- invariants of a super class must be preserved
- a sub class should not change values of private fields of the super class

### Interface Segregation

Interfaces should be brief, concrete, not bloated with many methods. Unlike classes, multiple interfaces can be implemented by a class. This is specially true if some class implementing an interface just have no use for many of its methods, this is a clear sign that you should segregate/divide into more than one interface and/or modify the class hierarchy.

### Dependency Inversion Principle 

High-level classes should not depend on low-level classes, they should depend on abstractions (interfaces) and low-level classes should depend on them too. Early on in a project low-level classes are usually developed first, so then high-level classes tend to depend on them. E.x: database related high-level classes implement low-level class MySqlDB, which can be limiting in the future; instead you should implement a Database interface which MySqlDB and, for example, MongoDB, can extend. This way low-level classes depend on high-level abstractions/interfaces

## DRY

The key insight is that DRY should be applied thoughtfully, not religiously. Sometimes duplication is actually cheaper than the wrong abstraction (WET). It's often easier to extract common patterns later when you have 2-4 similar implementations than to guess what the abstraction should look like upfront. 


# Memory & Performance

- https://notes.takashiidobe.com/courses/performance-engineering-of-software-systems/bentley-rules-for-optimizing-work
- https://medium.com/@ckekula/understanding-computer-memory-6d025056a253
- https://medium.com/@ckekula/understanding-computer-internal-memory-ad894025dce0
- https://medium.com/@ckekula/understanding-cache-memory-df5c4003d99f
- https://medium.com/@ckekula/understanding-cache-memory-part-2-e3fb8b0f1c41

The article presents a modified set called the “New Bentley” Rules, organized into four categories (Data Structures, Logic, Loops, Functions).

The original “Bentley Rules for Optimizing Work” from Programming Pearls (and the associated MIT course) typically include these additional rules not found in the article:

- Pipeline:	Overlap operations to keep execution units busy (e.g., using assembly pipelines or modern CPU instruction-level parallelism).

- Parallelism: 	Use multiple processors, cores, or SIMD instructions to perform work concurrently.

- Caching (more broadly): The article mentions caching but limits it to memoization. The original rule more broadly includes using memory hierarchy effectively (e.g., optimizing for L1/L2 cache locality).

- Hashing:	Use hash tables for O(1) lookups instead of O(n) or O(log n) structures where appropriate.

## Applicability to High-Level Languages (JS/TS with React, Next.js, Nest.js)

### Data Structures Rules

1. Packing and Encoding

```typescript
// ❌ Verbose object with full property names
const user = { isActive: true, accountType: 'premium' };
```

```typescript
// ✅ Packed encoding using bit flags
enum UserFlags {
  Active = 1 << 0,   // 1
  Premium = 1 << 1,  // 2
}
const userFlags = UserFlags.Active | UserFlags.Premium; // Single number
```

2. Augmentation
```typescript
// ❌ O(n) lookup in array for common operations
const users = [{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }];
const getUser = (id) => users.find(u => u.id === id);
```

```typescript
// ✅ Augment with Map for O(1) lookups (like adding a tail pointer)
const userMap = new Map(users.map(u => [u.id, u]));
const getUserFast = (id) => userMap.get(id);
```

3. Precomputation & Caching

```typescript
// ❌ Recalculating expensive data on each render (React)
function ExpensiveComponent({ data }) {
  const processed = heavyComputation(data); // Runs on every render
  return <div>{processed}</div>;
}
```

```typescript
// ✅ Precompute with useMemo
function ExpensiveComponent({ data }) {
  const processed = useMemo(() => heavyComputation(data), [data]);
  return <div>{processed}</div>;
}
```

```typescript
// ✅ Caching function results (Next.js/Nest.js)
const expensiveQuery = cache(async (id) => {
  return await db.user.findUnique({ where: { id } });
});
```

4. Sparsity

```typescript
// ❌ Dense array for sparse data (wasted memory/iteration)
const matrix = Array(10000).fill(0);
matrix[0] = 1;
matrix[9999] = 1;
```

```typescript
// ✅ Sparse representation using Map
const sparseMatrix = new Map();
sparseMatrix.set(0, 1);
sparseMatrix.set(9999, 1);
```

### Logic Rules

1. Short-Circuiting & Test Ordering

```typescript
// ❌ Expensive call always happens
if (user && user.address && validateAddressWithAPI(user.address)) { }

// ✅ Cheap checks first, expensive API call last
if (user?.address && await validateAddressWithAPI(user.address)) { }
```

2. Creating a Fast Path

```typescript
// ✅ Fast path for common case in Nest.js guard/Next.js middleware
@Injectable()
export class AuthGuard {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    
    // Fast path: public routes skip all auth logic
    if (this.isPublicRoute(request)) return true;
    
    // Slow path: full authentication check
    return this.authenticate(request);
  }
}
```

3. Common Subexpression Elimination

```typescript
// ❌ Computed twice
const area = width * height;
const perimeter = 2 * (width + height);

// ✅ Computed once (compiler may optimize, but explicit helps readability)
const widthHeight = width + height;
const area = width * height;
const perimeter = 2 * widthHeight;
```

### Loops Rules

1. Hoisting

```typescript
// ❌ Array length accessed each iteration
for (let i = 0; i < array.length; i++) { }

// ✅ Length hoisted
const len = array.length;
for (let i = 0; i < len; i++) { }

// ✅ Modern for-of hoists internally
for (const item of array) { }
```

2. Loop Fusion (React/Next.js)

```typescript
// ❌ Two separate loops over same data
users.forEach(user => updateCache(user));
users.forEach(user => notifySubscribers(user));

// ✅ Single loop
users.forEach(user => {
  updateCache(user);
  notifySubscribers(user);
});
```

### Functions Rules

1. Inlining (Nest.js)

```typescript
// ❌ Tiny function with overhead
const isAdult = (age) => age >= 18;
if (isAdult(user.age)) { }

// ✅ Inline simple logic (V8 may inline automatically, but helps readability)
if (user.age >= 18) { }
```

2. Coarsening Recursion

```typescript
// ❌ Recursion for every small chunk
function processChunk(data, index) {
  if (index >= data.length) return;
  doWork(data[index]);
  processChunk(data, index + 1);
}

// ✅ Coarsened: process in batches to reduce call overhead
function processBatch(data, start) {
  const end = Math.min(start + 100, data.length);
  for (let i = start; i < end; i++) doWork(data[i]);
  if (end < data.length) processBatch(data, end);
}
```

### Framework-Specific Notes

React:	useMemo, useCallback, React.memo implement caching and precomputation. Component tree structure affects pipeline/parallelism via concurrent rendering.

Next.js:	Static generation (SSG) is compile-time precomputation. Middleware allows request fast-paths. Caching headers implement broader caching rules.

Nest.js:	Guards and interceptors enable test ordering and fast-path patterns. Dependency injection supports augmentation (caching instances).


## Local Memory

### Caching

#### Memory Hierarchy

Modern CPUs have a memory hierarchy that JavaScript developers rarely consider, but understanding it helps write faster code:

|Level|Size	|Access Time|Location|
| -------|------------------|-------------|------------------ |
| L1 Cache |	32-64KB per core |	~1ns	|	 On CPU core |
| L2 Cache |	256KB-1MB per core |	~4ns	| On CPU chip |
| L3 Cache |	8-64MB shared	|	~12ns		|    On CPU chip |
| RAM		 |	GBs				|	~100ns		|Physical memory |

The key insight: cache misses are expensive. When the CPU needs data not in L1/L2, it stalls while fetching from RAM or worse, disk.

#### Cache Locality in JavaScript

Spatial Locality: Access Data Contiguously

```typescript
// ❌ Bad spatial locality - objects scattered in memory
class User {
  constructor(public id: number, public name: string, public age: number) {}
}

const users = Array(100000).fill(null).map((_, i) => new User(i, `User${i}`, 20 + i % 50));

// Access pattern: jumping between objects destroys cache efficiency
function calculateAverageAge(users: User[]) {
  let total = 0;
  for (const user of users) {
    total += user.age;  // Each user object may be in different memory location
  }
  return total / users.length;
}

// ✅ Good spatial locality - parallel arrays (Structure of Arrays pattern)
class UserData {
  ids: Int32Array;
  names: string[];
  ages: Int8Array;  // Age fits in 1 byte
  
  constructor(size: number) {
    this.ids = new Int32Array(size);
    this.names = new Array(size);
    this.ages = new Int8Array(size);
  }
}

const userData = new UserData(100000);
// Initialize...

function calculateAverageAgeOptimized(userData: UserData) {
  let total = 0;
  const ages = userData.ages;  // Get typed array reference
  for (let i = 0; i < ages.length; i++) {
    total += ages[i];  // Sequential access in contiguous memory
  }
  return total / ages.length;
}
```

Why this matters in React/Next.js:

```tsx
// ❌ Bad: Component re-renders cause scattered object recreation
function UserList({ users }) {
  // Each user object recreated on every render
  const processedUsers = users.map(u => ({
    ...u,
    displayName: `${u.firstName} ${u.lastName}`.toUpperCase()
  }));
  
  return <div>{processedUsers.map(u => <UserCard key={u.id} user={u} />)}</div>;
}

// ✅ Better: Memoize derived data with spatial locality
function UserList({ users }) {
  // useMemo ensures stable reference, but also consider data structure
  const processedUsers = useMemo(() => {
    // Create parallel arrays for hot paths
    const names = new Array(users.length);
    const ages = new Uint8Array(users.length);
    
    for (let i = 0; i < users.length; i++) {
      names[i] = `${users[i].firstName} ${users[i].lastName}`.toUpperCase();
      ages[i] = users[i].age;
    }
    
    return { names, ages };
  }, [users]);
  
  return (
    <div>
      {users.map((user, i) => (
        <UserCard 
          key={user.id}
          name={processedUsers.names[i]}
          age={processedUsers.ages[i]}
        />
      ))}
    </div>
  );
}
```

#### Temporal Locality: Reuse Recently Accessed Data

```typescript
// ❌ Poor temporal locality - reprocessing same data multiple times
class DataProcessor {
  async processItems(items: Item[]) {
    // Pass 1: validation
    const valid = items.filter(i => this.validate(i));
    
    // Pass 2: enrichment (loses cache from pass 1)
    const enriched = valid.map(i => this.enrich(i));
    
    // Pass 3: transformation (loses cache from pass 2)
    const transformed = enriched.map(i => this.transform(i));
    
    return transformed;
  }
}

// ✅ Good temporal locality - single pass with local variables
class DataProcessorOptimized {
  async processItems(items: Item[]) {
    const results = [];
    
    for (let i = 0; i < items.length; i++) {
      const item = items[i];  // Load once, keep in register/L1
      
      if (!this.validate(item)) continue;
      
      const enriched = this.enrich(item);
      const transformed = this.transform(enriched);
      
      results.push(transformed);
    }
    
    return results;
  }
}
```

#### Advanced Cache Optimization Techniques

1. Blocking/Tiling for Large Datasets

```typescript
// Process data in blocks that fit in L2 cache
class MatrixProcessor {
  static multiplyBlocked(A: number[][], B: number[][]): number[][] {
    const n = A.length;
    const BLOCK_SIZE = 64;  // Tune based on L2 cache size
    
    const C = Array(n).fill(null).map(() => Array(n).fill(0));
    
    // Process in blocks that fit in L2 cache
    for (let i0 = 0; i0 < n; i0 += BLOCK_SIZE) {
      for (let j0 = 0; j0 < n; j0 += BLOCK_SIZE) {
        for (let k0 = 0; k0 < n; k0 += BLOCK_SIZE) {
          // Process one block at a time
          for (let i = i0; i < Math.min(i0 + BLOCK_SIZE, n); i++) {
            for (let j = j0; j < Math.min(j0 + BLOCK_SIZE, n); j++) {
              let sum = 0;
              for (let k = k0; k < Math.min(k0 + BLOCK_SIZE, n); k++) {
                sum += A[i][k] * B[k][j];
              }
              C[i][j] += sum;
            }
          }
        }
      }
    }
    
    return C;
  }
}
```

2. Cache-Aware Data Structures in Nest.js

```typescript
@Injectable()
export class CacheOptimizedService {
  private hotData: Map<number, HotData> = new Map();  // L1/L2 friendly
  private coldData: WeakMap<object, ColdData> = new WeakMap();  // GC-friendly
  
  // Store frequently accessed data in compact form
  private recentAccesses: {
    ids: Int32Array;
    timestamps: Float64Array;
    index: number;
  } = {
    ids: new Int32Array(1000),
    timestamps: new Float64Array(1000),
    index: 0
  };
  
  async getData(id: number): Promise<CombinedData> {
    // Check hot cache first (O(1) Map access)
    if (this.hotData.has(id)) {
      this.recordAccess(id);  // Track temporal locality
      return this.hotData.get(id)!;
    }
    
    // Fetch from DB (slow path)
    const data = await this.fetchFromDB(id);
    this.hotData.set(id, data);
    
    // Maintain cache size bound to L2 cache-like size
    if (this.hotData.size > 10000) {
      this.evictLeastRecent();
    }
    
    return data;
  }
  
  private recordAccess(id: number) {
    // Circular buffer for access patterns
    const idx = this.recentAccesses.index % 1000;
    this.recentAccesses.ids[idx] = id;
    this.recentAccesses.timestamps[idx] = performance.now();
    this.recentAccesses.index++;
  }
}
```

### Hash Tables and Fast Lookups

Understanding Hash Table Internals

JavaScript objects and Maps are hash tables, but their performance characteristics differ:

```typescript
// Object vs Map performance characteristics
const obj: Record<string, any> = {};
const map = new Map();

// ❌ Objects have hidden class chains and prototype lookups
console.log(obj.toString());  // Actually looks up prototype chain

// ✅ Maps are pure hash tables with no prototype
console.log(map.get('key'));  // Direct hash lookup

// Performance comparison (typical operations per second)
// Object (string keys): ~50M ops/sec
// Map (any keys): ~40M ops/sec but better for mixed types
// Array.find(): ~1M ops/sec
```

#### Advanced Patterns

##### Perfect Hashing for Known Keysets

```typescript
// When keys are known at compile time, create perfect hash
class PerfectHashMap<K extends string, V> {
  private hashTable: V[];
  private hashFunction: (key: K) => number;
  
  constructor(keys: K[], values: V[]) {
    // Find minimal perfect hash function
    const { hash, table } = this.createPerfectHash(keys);
    this.hashFunction = hash;
    this.hashTable = table;
    
    // Store values at hashed positions
    for (let i = 0; i < keys.length; i++) {
      const pos = this.hashFunction(keys[i]);
      this.hashTable[pos] = values[i];
    }
  }
  
  get(key: K): V | undefined {
    const pos = this.hashFunction(key);
    return this.hashTable[pos];
  }
  
  private createPerfectHash(keys: K[]): { hash: (key: K) => number; table: V[] } {
    // Simplified: In practice, use algorithm like gperf or CHD
    const size = keys.length * 2;
    const hash = (key: K) => {
      let h = 0;
      for (let i = 0; i < key.length; i++) {
        h = ((h << 5) - h) + key.charCodeAt(i);
        h = h & h;
      }
      return Math.abs(h) % size;
    };
    
    return { hash, table: new Array(size) };
  }
}

// Usage in Next.js API route
const HTTP_STATUS_CODES = new PerfectHashMap(
  ['OK', 'NOT_FOUND', 'INTERNAL_ERROR'],
  [200, 404, 500]
);
```

##### Robin Hood Hashing for Cache-Friendly Lookups

```typescript
// Robin Hood hashing reduces worst-case lookups by balancing probe lengths
class RobinHoodMap<K, V> {
  private keys: (K | undefined)[];
  private values: (V | undefined)[];
  private distances: Uint8Array;  // Distance from ideal position
  private size: number;
  
  constructor(capacity: number = 1024) {
    this.size = capacity;
    this.keys = new Array(capacity);
    this.values = new Array(capacity);
    this.distances = new Uint8Array(capacity);
  }
  
  set(key: K, value: V): void {
    let hash = this.hash(key);
    let distance = 0;
    let currentKey = key;
    let currentValue = value;
    let currentDistance = 0;
    
    while (true) {
      const pos = (hash + distance) % this.size;
      
      if (this.keys[pos] === undefined) {
        // Found empty slot
        this.keys[pos] = currentKey;
        this.values[pos] = currentValue;
        this.distances[pos] = currentDistance;
        return;
      }
      
      // Robin Hood: steal from richer (lower distance) elements
      if (this.distances[pos] < currentDistance) {
        // Swap with existing element
        [currentKey, this.keys[pos]] = [this.keys[pos]!, currentKey];
        [currentValue, this.values[pos]] = [this.values[pos]!, currentValue];
        [currentDistance, this.distances[pos]] = [this.distances[pos], currentDistance];
      }
      
      distance++;
      currentDistance++;
    }
  }
  
  get(key: K): V | undefined {
    let hash = this.hash(key);
    let distance = 0;
    
    while (distance < this.size) {
      const pos = (hash + distance) % this.size;
      
      if (this.keys[pos] === undefined) return undefined;
      if (this.keys[pos] === key) return this.values[pos];
      
      // Early termination: if distance > stored distance, key can't exist
      if (distance > this.distances[pos]) return undefined;
      
      distance++;
    }
    
    return undefined;
  }
  
  private hash(key: K): number {
    // MurmurHash3 style mixing for better distribution
    let h = 0;
    const str = String(key);
    for (let i = 0; i < str.length; i++) {
      h = Math.imul(h ^ str.charCodeAt(i), 0x9e3779b9);
      h = (h << 13) | (h >>> 19);
    }
    return Math.abs(h);
  }
}
```

### Framework Optimizations

#### React: Memoization with Custom Hash Functions

```tsx
import { useMemo } from 'react';
import hash from 'object-hash';

// Custom memoization with hash table for complex objects
function useDeepMemo<T>(factory: () => T, deps: any[]): T {
  const depsHash = useMemo(() => hash(deps), [deps]);
  
  return useMemo(() => {
    return factory();
  }, [depsHash]);
}

// Usage in component
function DataTable({ filters, sortConfig, pagination }) {
  // Deep comparison with hash table optimization
  const queryResult = useDeepMemo(
    () => fetchData({ filters, sortConfig, pagination }),
    [filters, sortConfig, pagination]
  );
  
  return <Table data={queryResult} />;
}
```

#### Next.js Route Cache with Hash-Based Invalidation

```typescript
// lib/cache.ts
interface CacheEntry<T> {
  data: T;
  timestamp: number;
  tags: string[];
}

class RouteCache {
  private cache = new Map<string, CacheEntry<any>>();
  private tagIndex = new Map<string, Set<string>>();  // tag -> keys
  
  async getOrFetch<T>(
    key: string,
    fetcher: () => Promise<T>,
    tags: string[] = []
  ): Promise<T> {
    const cached = this.cache.get(key);
    
    // Check if valid (TTL-based or tag-based invalidation)
    if (cached && !this.isInvalidated(cached, tags)) {
      return cached.data;
    }
    
    // Fetch and cache
    const data = await fetcher();
    this.set(key, data, tags);
    return data;
  }
  
  invalidateByTag(tag: string): void {
    const keys = this.tagIndex.get(tag);
    if (keys) {
      for (const key of keys) {
        this.cache.delete(key);
      }
      this.tagIndex.delete(tag);
    }
  }
  
  private set<T>(key: string, data: T, tags: string[]): void {
    this.cache.set(key, {
      data,
      timestamp: Date.now(),
      tags
    });
    
    // Update tag index for fast invalidation
    for (const tag of tags) {
      if (!this.tagIndex.has(tag)) {
        this.tagIndex.set(tag, new Set());
      }
      this.tagIndex.get(tag)!.add(key);
    }
  }
  
  private isInvalidated(entry: CacheEntry<any>, tags: string[]): boolean {
    // Check TTL (5 minutes)
    if (Date.now() - entry.timestamp > 300000) return true;
    
    // Check if any of the requested tags are invalidated
    return tags.some(tag => this.tagIndex.has(tag) && 
                           !entry.tags.includes(tag));
  }
}

export const routeCache = new RouteCache();
```

#### Nest.js DB Query Cache with Hash-Based Deduplication

``` typescript
@Injectable()
export class QueryCacheService {
  private queryCache = new Map<string, Promise<any>>();
  private lruCache = new Map<string, any>();
  private maxSize = 1000;
  
  async deduplicate<T>(
    queryKey: string,
    fetcher: () => Promise<T>
  ): Promise<T> {
    // Check for in-flight request first (request coalescing)
    const inFlight = this.queryCache.get(queryKey);
    if (inFlight) {
      return inFlight;
    }
    
    // Create promise and cache it
    const promise = fetcher().finally(() => {
      this.queryCache.delete(queryKey);
    });
    
    this.queryCache.set(queryKey, promise);
    return promise;
  }
  
  async withLruCache<T>(
    key: string,
    fetcher: () => Promise<T>,
    ttl: number = 60000
  ): Promise<T> {
    // Check LRU cache
    const cached = this.lruCache.get(key);
    if (cached && Date.now() - cached.timestamp < ttl) {
      // Move to front (LRU behavior)
      this.lruCache.delete(key);
      this.lruCache.set(key, cached);
      return cached.data;
    }
    
    // Fetch and cache
    const data = await fetcher();
    
    // LRU eviction
    if (this.lruCache.size >= this.maxSize) {
      const firstKey = this.lruCache.keys().next().value;
      this.lruCache.delete(firstKey);
    }
    
    this.lruCache.set(key, { data, timestamp: Date.now() });
    return data;
  }
}

// Usage in repository
@Injectable()
export class UserRepository {
  constructor(private cache: QueryCacheService) {}
  
  async findById(id: number): Promise<User> {
    const queryKey = `user:${id}`;
    
    return this.cache.deduplicate(queryKey, async () => {
      return this.prisma.user.findUnique({ where: { id } });
    });
  }
}
```

### Practical Benchmarking

``` typescript
// Benchmark different lookup strategies
class LookupBenchmark {
  static run() {
    const size = 100000;
    const data = Array(size).fill(null).map((_, i) => ({ id: i, value: Math.random() }));
    
    // 1. Array.find() - O(n)
    console.time('Array.find');
    for (let i = 0; i < 1000; i++) {
      const target = Math.floor(Math.random() * size);
      data.find(item => item.id === target);
    }
    console.timeEnd('Array.find');
    
    // 2. Object hash table
    const objMap: Record<number, any> = {};
    data.forEach(item => { objMap[item.id] = item; });
    console.time('Object lookup');
    for (let i = 0; i < 1000; i++) {
      const target = Math.floor(Math.random() * size);
      objMap[target];
    }
    console.timeEnd('Object lookup');
    
    // 3. Map
    const map = new Map(data.map(item => [item.id, item]));
    console.time('Map lookup');
    for (let i = 0; i < 1000; i++) {
      const target = Math.floor(Math.random() * size);
      map.get(target);
    }
    console.timeEnd('Map lookup');
  }
}
```

### Key Takeaways

- Cache locality matters even in JavaScript - V8 optimizes for sequential access patterns
- Structure of Arrays (SoA) beats Array of Structures (AoS) for numeric data processing
- Maps are faster than objects for dynamic key sets and frequent additions/deletions
- Perfect hashing can achieve O(1) with minimal memory when keys are known
- Cache invalidation is hard - design tag-based systems for efficient purging
- Request deduplication with hash tables prevents thundering herd problems

## Distributed Memory

What we just saw (local memory) and Redis serve different layers of the caching hierarchy:

|Layer	|Examples|	Access Time|	Scope|
|-------|--------|------------|-------------|
|L1/L2 CPU Cache| 	Hardware caches|	~1-4ns|	Per CPU core|
|In-Memory Cache|	Map, WeakMap|	~100ns-1μs| Single process|
|Distributed Cache|	Redis, Memcached|	~100μs-1ms| Across servers|
|Database	|PostgreSQL, MongoDB	|~1-100ms	|Persistent storage|

### Local Memory vs. Redis

```typescript
// This is LOCAL to a single process
class RouteCache {
  private cache = new Map<string, CacheEntry<any>>();  // Lives in this Node.js process only
  private tagIndex = new Map<string, Set<string>>();
  
  async getOrFetch<T>(key: string, fetcher: () => Promise<T>): Promise<T> {
    const cached = this.cache.get(key);
    if (cached) return cached.data;  // Super fast: just memory access
    
    const data = await fetcher();
    this.cache.set(key, data);
    return data;
  }
}
```

- Speed: Microsecond-level access (pure memory)
- Scope: Only this Node.js process
- Persistence: Lost on process restart
- Memory: Uses application memory (limited)
- Coherence: No cross-server consistency
- Redis: Distributed Caching Layer

```typescript
// This is DISTRIBUTED across servers
import Redis from 'ioredis';

class DistributedCache {
  private redis: Redis;
  
  async getOrFetch<T>(key: string, fetcher: () => Promise<T>): Promise<T> {
    // Network call to Redis server
    const cached = await this.redis.get(key);
    if (cached) return JSON.parse(cached);
    
    const data = await fetcher();
    await this.redis.set(key, JSON.stringify(data), 'EX', 3600);
    return data;
  }
}
```

- Speed: Millisecond-level access (network + memory)
- Scope: Shared across all servers
- Persistence: Optional persistence to disk
- Memory: Dedicated memory (doesn't compete with app)
- Coherence: Consistent across instances

### When to Use Each

#### Local In-Memory Cache:

```typescript
// ✅ Perfect for: Request deduplication within same process
@Injectable()
class UserService {
  private pendingRequests = new Map<string, Promise<User>>();
  
  async getUser(id: string): Promise<User> {
    // Deduplicate concurrent requests for same user
    if (this.pendingRequests.has(id)) {
      return this.pendingRequests.get(id)!;
    }
    
    const promise = this.prisma.user.findUnique({ where: { id } });
    this.pendingRequests.set(id, promise);
    
    return promise.finally(() => {
      this.pendingRequests.delete(id);
    });
  }
}
```

```typescript
// ✅ Perfect for: React component memoization
function ExpensiveComponent({ data }: Props) {
  // This cache lives per component instance, not across users
  const result = useMemo(() => heavyComputation(data), [data]);
  return <div>{result}</div>;
}
```

```typescript
// ✅ Perfect for: Session data (already tied to a server)
import session from 'express-session';
app.use(session({
  store: new MemoryStore(),  // Local session storage
  secret: 'keyboard cat'
}));
```

#### Redis Cache

```typescript
// ✅ Perfect for: Shared across multiple server instances
@Injectable()
class ProductCatalogService {
  constructor(private redis: Redis) {}
  
  async getProduct(id: string): Promise<Product> {
    // Cache shared across all instances of your Next.js/Nest.js app
    const cached = await this.redis.get(`product:${id}`);
    if (cached) {
      return JSON.parse(cached);
    }
    
    const product = await this.database.product.findUnique({ where: { id } });
    
    // All server instances see this cache
    await this.redis.set(`product:${id}`, JSON.stringify(product), 'EX', 3600);
    return product;
  }
}
```

```typescript
// ✅ Perfect for: Rate limiting across servers
class RateLimiter {
  async checkLimit(userId: string): Promise<boolean> {
    // Need to track across all servers to enforce global limit
    const key = `ratelimit:${userId}`;
    const current = await this.redis.incr(key);
    
    if (current === 1) {
      await this.redis.expire(key, 60);  // 1 minute window
    }
    
    return current <= 100;  // 100 requests per minute globally
  }
}
```
```typescript
// ✅ Perfect for: Session store with serverless deployments
// (where servers come and go)
import RedisStore from 'connect-redis';

app.use(session({
  store: new RedisStore({ client: redis }),
  secret: 'your-secret'
}));
```

### Combined: Multi-Level Caching

The real power comes from combining both:

```typescript
class MultiLevelCache {
  private localCache = new Map<string, { data: any; timestamp: number }>();
  private redis: Redis;
  
  async get<T>(key: string): Promise<T | null> {
    // Level 1: Local memory (fastest)
    const local = this.localCache.get(key);
    if (local && Date.now() - local.timestamp < 60000) {
      return local.data;
    }
    
    // Level 2: Redis (shared across servers)
    const redisData = await this.redis.get(key);
    if (redisData) {
      const parsed = JSON.parse(redisData);
      // Backfill local cache
      this.localCache.set(key, { data: parsed, timestamp: Date.now() });
      return parsed;
    }
    
    // Level 3: Database (slowest)
    return null;
  }
  
  async set(key: string, data: any, ttl: number = 3600): Promise<void> {
    // Write to both layers
    this.localCache.set(key, { data, timestamp: Date.now() });
    await this.redis.set(key, JSON.stringify(data), 'EX', ttl);
  }
}
```

```typescript
// Real-world example in Nest.js
@Injectable()
class UserService {
  private localCache = new Map<string, User>();
  
  async findById(id: string): Promise<User> {
    // L1: Check local process cache
    if (this.localCache.has(id)) {
      return this.localCache.get(id)!;
    }
    
    // L2: Check Redis (shared cache)
    const redisKey = `user:${id}`;
    const cached = await this.redis.get(redisKey);
    
    if (cached) {
      const user = JSON.parse(cached);
      // Backfill L1
      this.localCache.set(id, user);
      return user;
    }
    
    // L3: Database query
    const user = await this.prisma.user.findUnique({ where: { id } });
    
    // Populate both caches
    await this.redis.set(redisKey, JSON.stringify(user), 'EX', 3600);
    this.localCache.set(id, user);
    
    return user;
  }
}
```

### Framework Examples

#### Next.js: Hybrid Caching Strategy

```typescript
// app/api/products/[id]/route.ts
import { LRUCache } from 'lru-cache';
import { Redis } from '@upstash/redis';

// L1: In-memory LRU cache for hot items
const l1Cache = new LRUCache<string, any>({
  max: 100,  // Keep only 100 items in memory
  ttl: 1000 * 60  // 1 minute
});

// L2: Upstash Redis (serverless Redis)
const l2Cache = Redis.fromEnv();

export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  const productId = params.id;
  
  // L1: Check memory cache
  let product = l1Cache.get(productId);
  if (product) {
    return Response.json(product);
  }
  
  // L2: Check Redis (shared across all serverless functions)
  product = await l2Cache.get(`product:${productId}`);
  if (product) {
    l1Cache.set(productId, product);  // Backfill L1
    return Response.json(product);
  }
  
  // L3: Database (or origin)
  product = await db.product.findUnique({ where: { id: productId } });
  
  // Populate caches
  await l2Cache.set(`product:${productId}`, product, { ex: 3600 });
  l1Cache.set(productId, product);
  
  return Response.json(product);
}
```

#### Nest.js: Advanced Caching Module

```typescript
// cache.module.ts
import { Module, Global } from '@nestjs/common';
import { CacheModule as NestCacheModule } from '@nestjs/cache-manager';
import { redisStore } from 'cache-manager-redis-yet';

@Global()
@Module({
  imports: [
    NestCacheModule.registerAsync({
      useFactory: async () => ({
        stores: [
          // L1: In-memory store
          {
            store: 'memory',
            max: 100,
            ttl: 60,  // seconds
          },
          // L2: Redis store
          {
            store: await redisStore({
              url: process.env.REDIS_URL,
              ttl: 3600,  // seconds
            }),
          },
        ],
      }),
    }),
  ],
  exports: [NestCacheModule],
})
export class CustomCacheModule {}
```

```typescript
// usage.service.ts
@Injectable()
class ProductService {
  constructor(@Inject(CACHE_MANAGER) private cacheManager: Cache) {}
  
  async getProduct(id: string): Promise<Product> {
    // Multi-level caching automatically handled by cache-manager
    return this.cacheManager.get(`product:${id}`);
  }
}
```

### Key Differences

|Aspect	|Local|Redis|
|-------|-----|-----|
|Implementation	| Simple Map/WeakMap|	Sophisticated in-memory DB|
|Speed|	~100ns-1μs|	~100μs-1ms (network)|
|Persistence	|None (process dies = cache lost) |Optional (RDB/AOF snapshots)|
|Memory	|Uses app memory	|Dedicated memory server|
|Distribution	|Single process |Multiple servers/clients|
|Features	|Basic get/set	|Pub/sub, streams, Lua scripting, geospatial|
|Use Case	|Request dedup, component memo	| Shared sessions, rate limiting, global state|

### Conclusion

#### Local memory

- Request deduplication (millisecond-scale)
- Hot data that's expensive to serialize
- Per-request state

#### Redis

- Session stores (especially in serverless)
- Rate limiting across instances
- Global configuration
- Pub/sub between services
- Persistent cache with eviction policies

#### Both together

- L1: Local memory (fastest, least capacity)
- L2: Redis (fast, shared capacity)
- L3: Database (slowest, infinite capacity)


# AI

## Tips 

1. Pi was built because Claude Code became unpredictable. Mario was a big fan of Claude Code at first. But as the team behind it pushed velocity and added features, he found that bugs multiplied and the tool’s behavior started to change. Mario wanted an AI harness that behaves in a stable, consistent way. He observed that the addition of new features caused Claude Code to act unpredictably, so resolved to add as few features as possible to Pi.

2. It should be MUCH easier to build specialized tools for specific tasks. Different projects need different harness types because, as Mario points out, the same hammer is not ideal for every single construction job. As such, Pi is built with the goal of allowing the creation of specialized harnesses. It can modify itself so that a user can create the bespoke harness needed for any task. Mario believes it’s a preview of how self-modifiable software might look in the future.

3. Automation bias is one of the biggest risks of working with AI agents. Once devs confirm that an AI agent can produce acceptable code, they start to review its output less often, even though agents can – and do! – produce slop. Mario advises being far more sceptical with agents, and cautions that the quality of their output isn’t guaranteed, however well they performed previously.

4. AI agents decrease code quality, but this is not on purpose. From talking with 30+ engineering teams, Armin found that code quality is down everywhere, and serious projects are shipping with “vibe slop.” A potential cause of this is that keeping agentic output clean and of high quality takes deliberate effort, but it’s not clear to many devs exactly how to do this. There’s also PR review fatigue and automation bias (the assumption that AI agents invariably generate good code).

5. New trend: AI makes it harder for senior engineers to reject pointless complexity. Historically, senior engineers kept software complexity at bay simply by saying “no” a lot. But Armin observes that these days, more junior engineers and product managers deploy agent-scripted counterarguments when a senior colleague kicks an idea to the curb. This makes decision-making exhausting, and more bad ideas make it into production as a result.

6. Junior engineers > AI agents. Mario points out that, unlike humans, agents don’t retain lessons in the same way, nor feel the pain of bad code. Junior engineers do, and the pain of maintenance teaches them to simplify interfaces and avoid bad abstractions – which are both qualities of an effective senior engineer. In this way, a junior engineer is more valuable than an AI agent!

7. Agents refactor less because they feel no “pain.” Humans rewrite bad interfaces because maintaining them hurts, whereas agents will obliviously churn out and extend a terrible structure, ad infinitum. This is a big reason why AI agents keep adding more tech debt.

8. Frictionless shipping can actually be harmful. Armin notes that some friction is desirable; for example, multi-reviewer approvals on critical services, SLO gates (different gates based on the service level objective offered), and migration checklists. The good thing about friction is that it makes humans stop and think.

## Scenarios, Flows

- como es tu flujo con IA?
- como iteras el plan?
- usas algún framework? (spec driven development)
- como desarrollarias una feature end to end para que fuera agentica? 
- que haces si el agente se te queda colgado haciendo algo?
- usas los hooks? para que?
- Deel, afuera y BruBank acá en Argentina, están fomentando internamente no user IDE, trabajar todo en la terminal y crear la estructura de hooks y CI para tests y code reviews automáticos

## Resources

- https://martinfowler.com/articles/structured-prompt-driven/ | tratar los prompts como artefactos de ingeniería, no como conversaciones de chat
- https://github.com/mattpocock/sandcastle | build custom workflows for agents
- https://github.com/subramanya1997/markdownfs | high-performance, in-memory virtual file system for Markdown files
- https://skills.sh/browserbase/skills/browser-trace | give full browser access to agent for observability: dump network requests, DOM content, screenshots, and CDP logs into a searchable filesystem
- https://github.com/sentrux/sentrux | evaluate and improve codebase architecture
- https://github.com/adbar/trafilatura | crawl and scrape the web, output as CSV, JSON, HTML, MD, TXT, XML
- https://github.com/Unstructured-IO/unstructured | open-source ETL solution for transforming documents to structured data

# Frontend

## Code Performance

Two fixes that usually move real-world metrics first:

1.	Eliminate waterfalls
2.	Reduce bundle size

Then move on to server-side performance, client-side fetching, and re-render optimization.

- https://zeroheight.com/blog/using-composability-over-inheritance-to-scale-design-systems/  | designing composable components 
- https://www.syncfusion.com/blogs/post/react-design-patterns
- https://reactpatterns.com
- https://fettblog.eu/typescript-react/
- https://react-typescript-cheatsheet.netlify.app/docs/basic/setup
- https://fettblog.eu/jsx-syntactic-sugar/
- https://react.dev/blog/2025/02/14/sunsetting-create-react-app#why-we-recommend-frameworks | routing, data fetching and code splitting anti patterns (e.x don’t use `fetch` and `useEffect` because leads to network waterfalls)
- https://www.patterns.dev/react/react-server-components/
- https://www.patterns.dev/react/react-2026/
- https://www.perssondennis.com/articles/21-fantastic-react-design-patterns-and-when-to-use-them
- https://www.perssondennis.com/articles/write-solid-react-hooks
- https://www.perssondennis.com/articles/why-server-components-a-brief-history-of-web
- https://feature-sliced.design/docs/get-started/overview
- https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/How_browsers_work | very important and insightful
- https://developer.chrome.com/blog/inside-browser-part1
- https://vercel.com/blog/introducing-react-best-practices

## SoC (Separation of Concerns)
Different types of concerns (data, business logic, presentation) should be in separate layers with clear boundaries. This separation makes the code much easier to understand, test, and maintain. You can test business logic without worrying about API calls or rendering. You can change the API structure without touching business logic. And you can redesign the UI without affecting data handling. The key insight is that different types of logic change for different reasons and at different rates. By keeping them separate, you minimize the ripple effects when changes are needed.
	⁃	Presentation layer - only rendering
	⁃	State management layer
	⁃	Business logic layer - data transformations
	⁃	Data layer - API communication


## SDP (Stable Dependency Principle)

There's always components and hooks in a React app which are stable and well tested - SDP says that those should form the foundation of our app. Volatile components will of course exist, which are often updated or replaced. The point with SDP is to avoid having other components being dependent on these risky and unstable components to avoid having the whole app to crash for a small change in a seemingly unimportant component.

For instance, browser's built-in functionality rarely changes - that is safe to depend on. A useLocalStorage hook in React which uses local storage should rarely change and can also be considered stable. On the other hand, the `useStoreAnythingYouWant` hook my colleague Brad implemented might be more likely to change - consider it unstable.

The point is, avoid using stuff that you know might change. For example, private variables in libraries often start with an underscore. They are marked that way because they might change without any notice. If you see it, don't use it! In e2e tests with Cypress or similar, use data-test-id attributes, don't use CSS selectors to grab HTML elements or class names. CSS classes disappears just as quickly as Brad when he sees people walking towards the table tennis room.

## React

### Hooks

- Hooks Pattern: changed the way React code is written, now functional components can be stateful, not just class components. They help to write cleaner, more concise code and avoid the classes’ more verbose syntax. Aside from accessing state, they provide access to lifecycle methods, refs and context. (useState, useEffect, useRef, useContext, useCallback, useMemo, etc)

- Custom Hooks: lift out and encapsulate logic such as useEffects and useStates into custom hooks to abstract away the React logic in favor of readable hooks

- https://github.com/streamich/react-use

#### Tips

1. Based on requirements, write clearly what you want the hook to do. Otherwise, then, it will be hard to read and debug.
2. Understand when to use a `useRef` or a `useEffect`: 

- ref: when you want to persist a certain state through renders but not show it to the end-user. also when you don't want to generate a re-render
- effect: when you want a certain behavior after a render, using the base react hook to build upon it

### Design Patterns

- HOC (Higher Order Components): function components that take a component as argument and return a new component. E.x: pass a bare component and return a new styled component. This can be used for an app’s styling standard and can be very convenient if multiple components need access to the same data, or contain the same logic

- Provider Pattern: used for sharing state across components and avoid the prop-drilling anti pattern. It can be implemented with Context API, Redux, depending on your needs and the app’s size/scale

- Container/Presentational Pattern: serves the purpose of segregating business logic and views; container component for fetching and operating on data, presentation component for displaying data. It’s often implemented with a parent container component and a child presentation component

- Compound Pattern: advanced pattern that lets us build functions to accomplish tasks collaboratively, meaning operating on state, context, refs, among others, in multiple components, and providing a final result/state

- State Hoisting: pass/share state from a child component to a parent component/first common ancestor. This is done by passing a callback to the child, e.x an `onChange` event handler that sends data from the stateless child component back to the stateful parent component, where it is used to update local state

- Portal Pattern: useful for dropdown, tooltips, modals. Solves z-index issues and ensures your component stays on top of its parent

- Headless Components Pattern: is used in some UI component libraries like Radix UI and Ark UI, they provide complex logic without any styling, leaving the visual presentation completely up to you

- Atomic Design Pattern: inspired by chemistry, it aims to organize components into atoms, molecules, organisms, templates and pages. Used to build large design systems but also a general good practice

- Render Props Pattern: share state between multiple children components from a stateful parent component. This can be passing `render` as a prop (function) or directly passing a function as children so we don’t have to even name it as a property. It mainly solves the same issues as HOC but avoiding properties naming collisions

Note (React 18+): The render props pattern is now largely supplanted by Hooks in React’s best practices. Render props often resulted in deeply nested JSX “callback hell”—for example, nesting multiple <Mutation> components to get multiple pieces of data. Modern libraries like Apollo Client now provide Hooks (e.g., useMutation, useQuery) that allow you to fetch or compute needed data inside the component, eliminating the need for wrapper components. Hooks don’t create new component boundaries, so state can be shared more directly and the React Compiler can statically analyze the code more easily. While render props are still possible, if you find yourself writing a component whose sole purpose is to call props.render() or use children-as-a-function, ask if a custom Hook could achieve the same result more directly.

### Rendering Patterns

- React Server Components: Unlike classic SSR, RSCs allow you to render part of your UI on the server ahead of time without sending the associated JS to the client—dramatically shrinking client bundles (early reports show 20%+ reductions). The Container/Presentational pattern is a great candidate for RSC: the “container” (data-fetching logic) can be a Server Component that fetches data and passes it as props to a presentational Client Component, meaning the fetching logic never ships to the browser. They introduce automatic code-splitting treating all normal imports in Client components as possible code-split points. They also allow developers to select which component to use much earlier (on the server), allowing the client to fetch it earlier in the rendering process. However it can lead to higher server expenses, so choose wisely

- CSR (Client Side Rendering): only barebones HTML are rendered by the server, all the logic, data fetching, templating and routing are done client-side

- SSR (Server Side Rendering): the server generates the whole HTML in response to a client’s request

- Static Rendering or SSG: deliver pre-rendered HTML generated when the site was built. Works for static content content/pages

- Incremental Static Generation: introduced as an upgrade to SSG, to help solve the dynamic data problem and help static sites scale for large amounts of frequently changing data. iSSG allows you to update existing pages and add new ones by pre-rendering a subset of pages in the background even while fresh requests for pages are coming in

- Progressive Hydration: introduced as an upgrade to SSG, to help solve the dynamic data problem and help static sites scale for large amounts of frequently changing data. iSSG allows you to update existing pages and add new ones by pre-rendering a subset of pages in the background even while fresh requests for pages are coming in

- Streaming Server Side Rendering: split HTML up into smaller chunks! Node streams allow us to stream data into the response object, which means that we can continuously send data down to the client

- Selective Hydration: makes it possible to start streaming HTML without having to wait for the larger components to be ready. This means that we can lazy-load components when using SSR, which wasn’t (really) possible before


### Components

- proxy component: a “base” component that has base properties/styles that cannot miss, e.x a button should always have a prop `type = button`, so we wrap that in a proxy component `Button` and use it for every button on our app
- layout component: a component that renders other components with a certain layout, e.x rendering two components horizontally. Rarely 
- container component: fetches data and pass it onto a children component to render it (presentational). Stateful
- presentational component: the view that presents data. Usually stateless
- HOC component: takes a component as argument and returns another component (new, modified); could be for styling, certain domain properties, etc
- headless component: a component with pure logic only, styling is left to the user/presentational component. Used for logically complex components
- portal component: part of the portal pattern, these components allow us to create child components that don’t need to worry about z-index issues regarding their parent components

### Development Checklist
- Phase 1: Design & Structure
	- Start with mockup & data: Analyze the design and JSON API structure.
	- Break UI into components: Draw boxes, name components, and arrange them into a parent-child hierarchy. Match the component structure to the data model.
	- Build a static version: Use components and props only (no state yet). Pass data from top to bottom. Build top-down or bottom-up.

- Phase 2: State & Interactivity
	- Identify minimal state: Determine the minimal, changing data needed. Avoid redundant state (compute values where possible). State should not be: unchanged data, props, or computed values.
	- Place state correctly: Find the closest common parent component to all components that need the state. Put state there (or above). Use useState().
	- Add inverse data flow: Pass state setters down to child components. In children, use event handlers (e.g., onChange) to call setters and update state upward.

- Phase 3: Follow Core Rules (Purity & Correct Usage)
	- Keep components & hooks pure:
	- Idempotent output: Same inputs (props, state, context) must return the same output.
	- No side effects in render: Move effects (e.g., data fetching) into useEffect or event handlers.
	- Never mutate: Do not directly mutate props, state, or values passed to Hooks or JSX. Treat them as immutable snapshots.
	- Let React manage components & hooks:
		- Use components in JSX only: Never call component functions directly (e.g., MyComponent() is incorrect; use <MyComponent />).
		- Never pass hooks as regular values: Only call hooks inside components at the top level.
	- Follow Rules of Hooks:
		- Call hooks only at the top level: Not inside loops, conditions, or nested functions.
		- Call hooks only from React functions: Not from regular JavaScript functions.

- Tooling Recommendation
	- Use Strict Mode and the React ESLint plugin to automatically enforce these rules and catch bugs early.

- Key Principle
  - Think in terms of declarative, one-way data flow: Build a static structure first, introduce state as needed, place it correctly, and enable updates via inverse data flow—all while ensuring purity and following the Rules of Hooks for predictable, bug-free behavior.

## Resources

- https://claritydev.net/blog/the-most-common-mistakes-when-using-react


# Backend

## API Design

Think of it like "Ordering From a Restaurant Menu." The core metaphor is powerful: **your API is a menu**. Resources are the dishes (nouns identified by URLs), and HTTP methods are the limited set of actions a waiter can take (order, change, remove). Clients don't need a tour of your kitchen (internals)—they just work the menu.

### 1. The Mental Model: Request-Response Cycle

Every REST interaction follows this fundamental pattern:

| Component | Description | Example |
| :--- | :--- | :--- |
| **Method** | The action (HTTP verb) | `GET`, `POST`, `PUT` |
| **URL** | The resource identifier | `/users/42/orders` |
| **Body (Optional)** | Data payload | JSON representation |
| **Status Code** | Outcome of the request | `200`, `404`, `500` |
| **Headers** | Metadata about the response | `Content-Type`, `ETag` |
| **Response Body** | The resource representation | JSON data |

### 2. Resources, Not Actions: The Cardinal Rule

The single most common and damaging mistake is **stuffing verbs into URLs**. The URL is the noun; the method is the verb.

#### Anti-Patterns vs. Correct Patterns

| ❌ Anti-Pattern (Verbs in URL) | ✅ Correct Pattern (Nouns in URL) |
| :--- | :--- |
| `GET /getUser?id=42` | `GET /users/42` |
| `POST /createOrder` | `POST /orders` |
| `POST /orders/42/delete` | `DELETE /orders/42` |
| `POST /users/update` | `PATCH /users/42` |

#### URL Design Rules That Hold Up

| Rule | Good Practice | Anti-Pattern / Avoid |
| :--- | :--- | :--- |
| **Plural Collections** | `/users`, `/orders` | `/user`, `/order` (singular breaks collection expectation) |
| **Nesting Depth** | Max 1 level: `/users/42/orders` | `/users/42/orders/7/items/3/reviews` (object graph abuse) |
| **Parameters** | Path for identity (`/users/42`)<br>Query for filter/sort/page (`?role=admin`) | Confusing identity with filtering |
| **Case & Separators** | `kebab-case`: `/user-profiles` | `/UserProfiles`, `/user_profiles` |
| **Abstraction** | Contract-based URLs | Leaking DB columns into URLs |

### 3. HTTP Methods: Semantics That Matter

| Method | Intent | Safe | Idempotent | Typical Response |
| :--- | :--- | :---: | :---: | :--- |
| **GET** | Read a resource | ✅ Yes | ✅ Yes | `200 OK` + body |
| **POST** | Create a new resource or trigger action | ❌ No | ❌ No | `201 Created` + `Location` header |
| **PUT** | Replace the entire resource at known URL | ❌ No | ✅ Yes | `200 OK` or `204 No Content` |
| **PATCH** | Partially update fields | ❌ No | ⚠️ Sometimes | `200 OK` |
| **DELETE** | Remove a resource | ❌ No | ✅ Yes | `204 No Content` |
| **HEAD** | Like GET but headers only | ✅ Yes | ✅ Yes | `200 OK`, no body |

#### Understanding Safety and Idempotency

- **Safe:** Does not change server state. `GET` is safe; `DELETE` is not.
- **Idempotent:** Calling twice has the same effect as once. `DELETE /orders/42` is idempotent (gone stays gone). `POST /orders` is **neither**—each call creates a new resource.

These properties are what enable proxies to cache, retries to work safely, and users to refresh without fear.

### 4. Status Codes: Tell the Truth

Never return `200 OK` with an error body. This hides failures from caches, retry libraries, monitoring tools, and SDKs.

#### Essential Status Codes

| Range | Category | Key Codes | When to Use |
| :--- | :--- | :--- | :--- |
| **2xx** | Success | `200 OK` | Default success for GET/PUT/PATCH |
| | | `201 Created` | Successful POST; include `Location` header |
| | | `202 Accepted` | Async processing started |
| | | `204 No Content` | Success with nothing to return (DELETE) |
| **4xx** | Client Error | `400 Bad Request` | Validation failed, malformed JSON |
| | | `401 Unauthorized` | Not authenticated (who are you?) |
| | | `403 Forbidden` | Authenticated but not allowed (I know you; answer is no) |
| | | `404 Not Found` | Resource doesn't exist |
| | | `409 Conflict` | Stale state, duplicate key |
| | | `422 Unprocessable` | Syntactically valid, semantically wrong |
| | | `429 Too Many Requests` | Rate limited; include `Retry-After` |
| **5xx** | Server Error | `500 Internal Error` | Generic blowup (avoid shipping this) |
| | | `502 Bad Gateway` | Upstream failure |
| | | `503 Service Unavailable` | Overloaded/maintenance |
| | | `504 Gateway Timeout` | Upstream didn't respond |

### 5. Query Patterns: Filtering, Sorting, Pagination

#### Standard Query Parameter Conventions

```http
GET /users?role=admin&status=active          # Filtering
GET /users?sort=-createdAt,email              # Sorting (- = desc)
GET /users?limit=50&cursor=eyJpZCI6MjA0fQ==  # Cursor pagination (preferred)
GET /users?page=3&pageSize=50                # Offset pagination (fallback)
```

#### Pagination Strategy Comparison

| Approach | Pros | Cons | Recommendation |
| :--- | :--- | :--- | :--- |
| **Offset** (`?page=3&pageSize=50`) | Easy to implement, jump to any page | Slow on large tables (`OFFSET 500000`), inconsistent under insert/deletion | Small, static datasets only |
| **Cursor** (`?limit=50&cursor=...`) | Stable under inserts/deletes, O(1) performance regardless of size | Can't jump to arbitrary page | **Default choice for production APIs** |


### 6. Versioning Strategy

| Method | Example | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Path-based** | `GET /v1/users/42` | Dead simple, visible in logs, obvious in `curl` | Treats versions as completely separate APIs |
| **Header-based** | `Accept: application/vnd.example.v2+json` | Clean URLs, used by Stripe/GitHub/Shopify | Harder to `curl`, easier to get wrong |

#### The Simplest Rule: Never Make Breaking Changes

- **Safe:** Adding new fields to responses
- **Breaking:** Removing or renaming existing fields

A well-behaved API keeps growing; explicit versions are only needed for rare breaking cuts.


### 7. Error Responses: One Shape Everywhere

Use RFC 7807 "Problem Details" or a consistent custom shape. Clients should only need to know one error schema.

```json
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/problem+json

{
  "type": "https://errors.example.com/validation",
  "title": "Validation failed",
  "status": 422,
  "detail": "email must be a valid address",
  "instance": "/users",
  "errors": [
    { "field": "email", "code": "invalid_format" },
    { "field": "password", "code": "too_short", "min": 8 }
  ]
}
```

**Why this shape works:**
- `type`: Machine-readable identifier for client branching
- `title`/`detail`: Human-readable messages
- `errors` array: Field-specific details for form highlighting


### 8. Critical Pattern: Idempotency for POST

`POST` is not idempotent by design, but your handler **can be**. This is essential for payments, inventory, or any operation where double-submission is catastrophic.

#### The Idempotency Key Pattern (Popularized by Stripe)

```http
POST /orders HTTP/1.1
Idempotency-Key: 9f8e7d6c-5a4b-4321-aaaa-111122223333
Content-Type: application/json

{ "item": "coffee", "amount": 499 }
```

**Implementation:**
1. Server stores `{key: created_resource_id}` for 24+ hours
2. If the same key arrives again, return the original resource instead of creating a duplicate
3. This pattern is now standard for any API handling money, inventory, or destructive operations


### 9. Authentication & Authorization

| Method | Description | Use Case |
| :--- | :--- | :--- |
| **API Keys** | Long random string in `Authorization: Bearer sk_live_...` header | Machine-to-machine APIs |
| **Bearer Tokens (OAuth/JWT)** | Short-lived token carrying identity and scopes | User-facing APIs needing horizontal scale |

#### Critical Security Rule

> **Never put secrets in query parameters.** Query strings appear in browser history, server logs, CDN logs, referrer headers, and analytics. Tokens and API keys belong exclusively in the `Authorization` header.


### 10. Code Example: Minimal REST API (Express)

```javascript
import express from "express";

const app = express();
app.use(express.json());

const users = new Map();

app.get("/users/:id", (req, res) => {
  const user = users.get(req.params.id);
  if (!user) return res.status(404).json({ error: "not found" });
  res.json(user);
});

app.post("/users", (req, res) => {
  const id = String(users.size + 1);
  const user = { id, ...req.body };
  users.set(id, user);
  res.status(201).location(`/users/${id}`).json(user);
});

app.delete("/users/:id", (req, res) => {
  users.delete(req.params.id);
  res.status(204).end();
});

app.listen(3000);
```

**Calling it:**
```bash
$ curl -X POST http://localhost:3000/users \
       -H "Content-Type: application/json" \
       -d '{"name":"Ada","role":"admin"}'

HTTP/1.1 201 Created
Location: /users/1
Content-Type: application/json

{"id":"1","name":"Ada","role":"admin"}
```

### 11. Real-World Examples in the Wild

| Company | REST Implementation Highlights |
| :--- | :--- |
| **GitHub** | Textbook REST: `GET /repos/:owner/:repo/issues`. Plural nouns, consistent nesting, predictable—new devs guess endpoints before reading docs. |
| **Stripe** | REST with idempotency keys and date-based versions (`2024-06-20` in headers). Every old version works forever. |
| **Kubernetes** | REST all the way down: `GET /api/v1/namespaces/default/pods`. `kubectl` is essentially a thin client over this API. |


### 12. Interview Question Cheat Sheet

| Question | The 30-Second Answer |
| :--- | :--- |
| **What is REST in one sentence?** | An architectural style for HTTP APIs where you model your domain as resources identified by URLs, act on them with standard HTTP methods, and let HTTP carry caching, status, and content negotiation. |
| **Why is REST stateless?** | So any server can answer any request, enabling horizontal scaling behind a load balancer. No session affinity required. |
| **PUT vs PATCH?** | `PUT` replaces the whole resource (missing fields get unset). `PATCH` updates only sent fields. `PUT` is always idempotent; `PATCH` usually is. |
| **POST vs PUT for creation?** | `POST` when server assigns the ID (responds with `201` and `Location`). `PUT` when client chooses the URL. |
| **What is idempotency?** | Doing an operation twice has the same effect as once. Critical because networks are unreliable and clients retry. |
| **How to paginate large collections?** | Cursor pagination is stable and O(1). Offset pagination breaks on large tables and shifting data. Default to cursor. |
| **401 vs 403?** | `401 Unauthorized`: "Who are you?" (not authenticated). `403 Forbidden`: "I know who you are; the answer is still no." |
| **REST vs GraphQL?** | Choose REST when data is resource-shaped, caching is critical, and you want standard tooling to "just work." Choose GraphQL when clients need wildly different shapes or over-fetching hurts mobile clients. |


### 13. The Five Things to Walk Away With

**Five Sentences That Capture REST:**

1. **REST is "name your things, then act on them with a fixed set of HTTP verbs"** — nothing more and nothing less.
2. **URLs are nouns; methods are the verbs.** Never put verbs in the URL.
3. **Status codes must tell the truth** — 2xx for success, 4xx when the client is wrong, 5xx when the server is wrong.
4. **Statelessness is what lets you scale horizontally** — keep session state in Redis or a token, not in memory on one server.
5. **Adopt one error shape, use cursor pagination, and add an idempotency key** the first time a retry could double-submit.

### Resources

- https://theskilledcoder.com/posts/system-design/restful-api-design

## Observability

### Resources

- https://theskilledcoder.com/posts/system-design/observability-pillars
- https://theskilledcoder.com/posts/dbms-sql/data-observability-freshness-schema-drift

## Deployment

### 1. Big Bang

The original pattern. Take everything down, deploy new version, bring everything back up.

Old Version V1 -> New Version V2

- Users: Offline
- Risk: Maximum
- When it works: Small apps with maintenance windows. Internal tools. Legacy systems.
- The nightmare: 3 AM deployment. Migration fails halfway. Can’t roll back. CTO is calling. You’re updating your resume.

### 2. Rolling

Deploy to servers gradually. Update a few instances at a time while others serve traffic.

| |  |  |  |  |
|-------|----|----|----|----|
|Time 0|  V1|  V1|  V1|  V1|
|Time 1| [V2]| V1|  V1|  V1|
|Time 2|  V2| [V2]| V1|  V1|
|Time 3|  V2|  V2| [V2]| V1|
|Time 4|  V2|  V2|  V2| [V2]|

- Users: Always available
- Risk:  Both versions running simultaneously
- Implementation:
```python
class RollingDeployment:
    def __init__(self, servers, batch_size=2):
        self.servers = servers
        self.batch_size = batch_size
    
    def deploy(self, version):
        for i in range(0, len(self.servers), self.batch_size):
            batch = self.servers[i:i + self.batch_size]
            
            print(f"Deploying to batch: {batch}")
            for server in batch:
                # Remove from load balancer
                self.load_balancer.remove(server)
                
                # Deploy new version
                self.deploy_to_server(server, version)
                
                # Health check
                if not self.health_check(server):
                    print(f"Health check failed on {server}")
                    self.rollback(server)
                    raise DeploymentError(f"Failed on {server}")
                
                # Add back to load balancer
                self.load_balancer.add(server)
                
            # Wait between batches
            time.sleep(30)
        
        print("Rolling deployment complete!")
    
    def health_check(self, server):
        for attempt in range(5):
            response = requests.get(f"http://{server}/health")
            if response.status_code == 200:
                return True
            time.sleep(5)
        return False
```
- When it works: Stateless applications. When V1 and V2 can coexist.
- The gotcha: User makes request to V1, refreshes, hits V2. Customer reports “the app is broken” but you can’t reproduce it.

### 3. Blue-Green

Maintain two identical environments. Switch traffic atomically from blue to green.

Step 1: Deploy V2 to Green (offline)
- Blue (V1) ← 100% traffic
- Green (V2) ← 0% traffic

Step 2: Switch traffic
- Blue (V1) ← 0% traffic
- Green (V2) ← 100% traffic

- Implementation:
#### Deploy to green environment
```bash
kubectl apply -f green-deployment.yaml
kubectl wait --for=condition=available deployment/app-green
```

#### Run smoke tests
```bash
command_to_run_smoke_tests http://green-internal.example.com
```

#### Switch traffic
```bash
kubectl patch service app-service -p '{"spec":{"selector":{"version":"green"}}}'
```

#### Monitor, then scale down blue
```bash
kubectl scale deployment app-blue --replicas=0
```
- When it works: When instant rollback is critical. Zero-downtime deployments needed.
- The surprise cost: Your cloud bill just doubled during every deployment.

### 4. Canary

Release to a small percentage of users first. Gradually increase if metrics look good.

#### Step 1: V2 gets 5% traffic

V1: ████████████████████ 95%

V2: █ 5%

#### Step 2: V2 gets 50% traffic  

V1: ██████████ 50%

V2: ██████████ 50%

#### Step 3: V2 gets 100% traffic

V1: 0%

V2: ████████████████████ 100%

- Implementation:
```python
class CanaryDeployment:
    def __init__(self, metrics_client):
        self.metrics = metrics_client
        self.canary_percentage = 5
    
    def deploy_canary(self):
        # Deploy V2 to canary instances
        self.deploy_version_2()
        
        # Route 5% traffic to canary
        self.update_traffic_split(canary=5, stable=95)
        
        # Monitor for 10 minutes
        time.sleep(600)
        
        if self.canary_is_healthy():
            return self.proceed_with_rollout()
        else:
            return self.rollback_canary()
    
    def canary_is_healthy(self):
        # Compare metrics between canary and stable
        canary_error_rate = self.metrics.get_error_rate('canary')
        stable_error_rate = self.metrics.get_error_rate('stable')
        
        canary_latency = self.metrics.get_p95_latency('canary')
        stable_latency = self.metrics.get_p95_latency('stable')
        
        # Canary should not be significantly worse
        if canary_error_rate > stable_error_rate * 1.5:
            print("Canary error rate too high")
            return False
        
        if canary_latency > stable_latency * 1.3:
            print("Canary latency too high")
            return False
        
        return True
    
    def proceed_with_rollout(self):
        for percentage in [10, 25, 50, 75, 100]:
            self.update_traffic_split(canary=percentage, 
                                     stable=100-percentage)
            time.sleep(300)  # 5 min between stages
            
            if not self.canary_is_healthy():
                self.rollback_canary()
                return False
        
        print("Canary deployment successful!")
        return True
```
- When it works: High-traffic applications where 5% is meaningful. When you have good metrics. When you can afford gradual rollout.
- When it fails: Low traffic means 5% is 3 users. Metrics don’t catch edge case bugs. The bug only appears at 100% traffic.
- The irony: You carefully canary test with 5% of users for a week. Deploy to 100%. Different bug appears because now the load is high enough to trigger race condition.

### 5. Feature Toggle

Deploy code with features turned off. Enable features gradually via configuration.

- Deploy V2 everywhere (features disabled). Enable for 10% of users:
	- V2 (Feature A: ON) 10%
	- V2 (Feature A: OFF) 90%

- Implementation:
```javascript
class FeatureToggleManager {
    constructor(configService) {
        this.config = configService;
        this.flags = {};
    }
    
    async isEnabled(featureName, userId) {
        // Get feature config
        const feature = await this.config.getFeature(featureName);
        
        if (!feature) return false;
        
        // Global kill switch
        if (feature.disabled) return false;
        
        // Percentage rollout
        if (feature.rolloutPercentage) {
            const userBucket = this.getUserBucket(userId);
            return userBucket < feature.rolloutPercentage;
        }
        
        // Whitelist
        if (feature.whitelist) {
            return feature.whitelist.includes(userId);
        }
        
        return feature.enabled;
    }
    
    getUserBucket(userId) {
        // Consistent hash to assign user to bucket 0-100
        const hash = crypto.createHash('md5')
            .update(userId.toString())
            .digest('hex');
        return parseInt(hash.substring(0, 8), 16) % 100;
    }
}

// Usage in application code
async function renderDashboard(userId) {
    const features = new FeatureToggleManager(configService);
    
    const newDashboardEnabled = await features.isEnabled(
        'new_dashboard_v2', 
        userId
    );
    
    if (newDashboardEnabled) {
        return renderNewDashboard();
    } else {
        return renderOldDashboard();
    }
}
```
- When it works: Large refactors shipped incrementally. A/B testing new features. Instant rollback without redeployment.
- When it fails: Feature flag code accumulates. Forgot to remove old code path. Combinatorial explosion of flag states.
- The technical debt: Three years later, the codebase has 47 feature flags. Nobody knows which ones are still needed. The code has paths that were never executed in production.

### The Reality

Most production systems use a combination:

- Feature toggles to control risk
- Blue-green for critical services
- Canary for high-traffic endpoints
- Rolling for everything else
- Big bang only when forced by legacy constraints

The best deployment pattern is the one that lets you sleep at night.

### Resources

- https://medium.com/@kanishks772/five-deployment-patterns-every-engineer-should-know-and-fear-72985f4383d0

## Databases

### The Core Philosophy: Performance is Designed, Not Tuned

A recurring theme across the materials is that database performance issues are often symptoms of deeper, foundational problems. As noted in *Performance Doesn't Start at SELECT; It Starts at CREATE*, "Most of the time, slow queries are symptoms, not causes. The disease starts with schema design." This philosophy shifts the focus from late-stage query rewriting to early-stage architectural decisions.

---

### Before Query Execution (Design-Time Optimization)

Performance and scalability are primarily determined by decisions made during the schema design and data modeling phase.

#### 1. Schema Design: The Foundation of Efficiency

A well-structured schema is the first line of defense against future performance bottlenecks.

- **Normalize First, Then Denormalize with Evidence**: Begin with a normalized schema (e.g., Third Normal Form) to eliminate data redundancy and ensure data integrity. This creates a disciplined structure where updates happen in one place. However, excessive normalization can lead to performance-sapping `JOIN`s on read-heavy queries. **Denormalization should be a measured, evidence-based trade-off**—applied only when specific high-traffic queries are proven to suffer from join overhead. It is a calculated sacrifice of consistency for speed.
- **Choose Correct Data Types**: Data types are not arbitrary labels; they are performance contracts with the database engine.
    - **Use the smallest type that fits** (e.g., `SMALLINT` instead of `INT` for bounded values). Smaller types mean smaller indexes, less I/O, and better cache efficiency.
    - **Match semantics to type**: Never store dates as strings or numbers as `VARCHAR`. This prevents expensive implicit casts in queries.
    - **Prefer fixed-width types** (`INT`, `DATE`, `CHAR`) where possible, as they make row access predictable. Variable-width types (`VARCHAR`, `TEXT`) require extra bookkeeping.
    - **Use JSON types intentionally**: `JSONB` in PostgreSQL is powerful for flexible metadata but shouldn't replace a well-defined schema. Treat it as an extension, not a shortcut to bypass design.

#### 2. Indexing with Intent, Not by Accident

Indexes are a trade-off: they accelerate reads but penalize writes. An intentional strategy is required to avoid "index bloat."

- **Index What Filters, Joins, or Sorts**: Focus on columns used in `WHERE`, `JOIN`, and `ORDER BY` clauses.
- **Leverage Composite Indexes**: For queries filtering on multiple columns `(A, B)`, a composite index is more efficient than two single-column indexes. **Order matters**: the "leftmost prefix" rule dictates the index can only be used if the query filters on the leading column(s).
- **Utilize Covering Indexes**: An index that contains *all* columns needed for a query allows the database to answer the query directly from the index, avoiding a costly trip to the main table heap.
- **Understand Specialized Index Types**:
    - **B-Tree**: The default, good for equality and range queries.
    - **Hash**: Optimized for simple equality lookups.
    - **GIN/GiST**: Essential for indexing complex types like `JSONB`, arrays, and full-text search vectors in PostgreSQL.
    - **BRIN**: Highly efficient for very large, sequentially stored data (e.g., time-series logs).

#### 3. Enforcing Integrity with Constraints

Constraints are not just about correctness; they provide the optimizer with critical information to generate faster plans.

- **`PRIMARY KEY`**: Guarantees identity and provides a clustered index (in many engines), optimizing range scans.
- **`FOREIGN KEY`**: When indexed, these improve join performance by guaranteeing referential integrity.
- **`NOT NULL`**: Allows the optimizer to skip null-checking branches in query plans, simplifying execution.
- **`UNIQUE` & `CHECK`**: Enforce business rules at the database level, preventing invalid data from ever being written and reducing the need for defensive application logic.

#### 4. Architectural Foresight: Scaling Strategies

Design for growth from the outset by understanding common patterns for scaling.

- **Read-Heavy Workloads (e.g., E-commerce Catalog)**:
    - **Scenario**: An e-commerce platform where millions browse products (reads) but relatively few place orders (writes).
    - **Strategy**: **Read Replicas**. Offload all read traffic to one or more read-only replicas of the primary database. A load balancer routes `SELECT` queries to replicas and `INSERT/UPDATE/DELETE` statements to the primary. A caching layer (e.g., Redis) in front of the database further reduces load.
- **Write-Heavy Workloads (e.g., Ride-Hailing App)**:
    - **Scenario**: Drivers in a ride-sharing app update their GPS location every few seconds.
    - **Strategy**: **Horizontal Partitioning (Sharding)**. Distribute write load by splitting data across multiple database instances based on a shard key (e.g., `DriverID` or `City`). This prevents any single database from becoming a write bottleneck. **Time-based partitioning** is also critical here for managing high-velocity time-series data.

---

### During Query Execution (Runtime Efficiency)

When a query runs, the goal is to minimize the work the database must do to produce the result. This is where the database's internal query engine comes into play.

#### The Life of a SQL Query: From Text to Results

Understanding the pipeline is crucial for writing efficient queries.

1.  **Parsing**: The SQL text is parsed into an Abstract Syntax Tree (AST) representing the query's structure.
2.  **Logical Planning & Optimization**: The AST is converted into a logical plan—a high-level algebra tree of operations (`Scan`, `Filter`, `Join`, `Project`). The optimizer then rewrites this plan to be more efficient, using techniques like:
    - **Predicate Pushdown**: Moving `Filter` operations as close to the data source (`TableScan`) as possible to reduce the number of rows processed early on.
    - **Projection Pushdown**: Only reading the columns needed for the final result, a huge advantage of **columnar storage**.
3.  **Physical Planning**: The optimized logical plan is translated into a physical plan, which specifies the exact algorithms to use (e.g., `Hash Join` vs. `Nested Loop Join`, `Index Scan` vs. `Sequential Scan`).
4.  **Execution**: The physical plan is executed, often using a pull-based Volcano-style model where each operator requests data from its children.

#### Key Runtime Performance Mechanisms

Many of these techniques are automatically handled by a good query optimizer, but understanding them helps in writing optimizer-friendly queries.

| Technique | Description | Real-World Benefit |
| :--- | :--- | :--- |
| **Static Pruning** | Uses pre-computed metadata (e.g., min/max values per data chunk, Zone Maps, Bloom Filters) to skip entire blocks of data. | Query for `sales_2025` skips all chunks where `max_year < 2025` without reading them. |
| **Dynamic Pruning** | Uses information gathered *during* query execution to prune data. | A filter on `orders.date` finds 10 keys. A subsequent join to `lineitems` only needs to fetch line items for those 10 specific keys. |
| **Compression** | Reduces I/O by storing data in a more compact form. This is more effective on low-entropy, sorted data. | **Dictionary Encoding**: Storing repeating strings (e.g., `"USA"`) as small integers. **Run-Length Encoding**: Storing `"AAAAAAAA"` as `"A", 8`. |
| **Vectorized Execution** | Processes data in batches (e.g., 1024 rows at a time) instead of row-by-row. This leverages modern CPU cache hierarchies and SIMD instructions. | Calculating `price * quantity` for a million rows is done in tight, CPU-friendly loops. |

#### Columnar vs. Row-Based Storage: A Critical Trade-off

The choice of storage format has a profound impact on analytical query performance.

| Feature | Row Store (e.g., PostgreSQL, MySQL/InnoDB) | Column Store (e.g., Parquet, ORC, DuckDB) |
| :--- | :--- | :--- |
| **Data Layout** | Stores all columns of a single row together. | Stores all values for a single column together. |
| **Write-Optimized** | Excellent. Adding a new row is a single write operation. | Poor. Adding a row requires writing to multiple column files. |
| **Read-Optimized** | Poor for analytical queries that read few columns. The entire row must be read ("read amplification"). | Excellent. Reads *only* the columns specified in the query, minimizing I/O. |
| **Compression** | Less effective due to mixed data types in a row. | Highly effective due to homogeneous data types within a column. |
| **Use Case** | **OLTP**: Transactional applications (e.g., order entry, user profile updates). | **OLAP**: Analytical applications (e.g., reporting, business intelligence). |

> **Example**: Query `SELECT AVG(grade) FROM students;`
> - **Row Store**: Must read the entire dataset (ID, Name, Grade, Subject...) from disk.
> - **Column Store**: Reads *only* the `Grade` column, leading to orders-of-magnitude less I/O.

---

### After Query Execution (Observability & Profiling)

Even with perfect design, bugs and unexpected performance cliffs occur. A robust observability strategy is essential for understanding and fixing issues in production.

#### Identifying Performance Anti-Patterns

Research into ORM-based applications has identified common "performance bugs" that degrade system behavior. Many stem from **ORM API Misuses**.

| Anti-Pattern | Description | Impact & Fix |
| :--- | :--- | :--- |
| **Inefficient Query (e.g., `any?` vs `exists?`)** | Using `Model.where(...).any?` loads all matching records to count them. | `exists?` generates a `LIMIT 1` subquery that stops at the first match, reducing work from O(N) to O(1). **Fix**: Replace `any?` with `exists?` for existence checks. |
| **Unintentional Ordering** | Using `Model.where(...).first` often triggers an unnecessary `ORDER BY primary_key` before applying `LIMIT 1`. | Causes a full index scan instead of a quick lookup. **Fix**: Use `Model.find_by(...)` which avoids the implicit order. |
| **N+1 Queries (Lazy Loading)** | Fetching a list of parent objects, then iterating over them to fetch their associated children. | A list of 100 `Authors` results in 1 query for authors + 100 queries for their books. **Fix**: Use **eager loading** (`includes` in Rails, `prefetch_related` in Django) to fetch all authors and books in 1-2 queries. |
| **Unbounded Data Retrieval** | Calling `.all` on a large table without pagination or filtering. | Loads millions of objects into application memory, crashing the server. **Fix**: Always use pagination (`LIMIT`/`OFFSET` or keyset pagination) for large result sets. |

#### Profiling and Monitoring Tools

A strong toolchain is necessary for catching these issues before users do.

- **Database-Side Monitoring**:
    - **Slow Query Logs**: Enable and analyze slow query logs (e.g., `log_min_duration_statement` in PostgreSQL, `slow_query_log` in MySQL) to find queries taking excessive time.
    - **Index Usage Stats**: Use system views like `pg_stat_user_indexes` (PostgreSQL) or `sys.dm_db_index_usage_stats` (SQL Server) to find **unused indexes** that are wasting write performance and disk space.
    - **`EXPLAIN (ANALYZE, BUFFERS)`**: This is the single most important tool for understanding a query's execution. It shows the plan chosen by the optimizer, the actual time spent in each node, and how many data blocks were read from disk vs. cache.

- **Application-Side Profiling (APM)**:
    - **Application Performance Monitoring (APM)** tools (e.g., DataDog, New Relic, Scout) can trace a slow web request all the way down to individual database queries, pinpointing the exact line of code causing an N+1 query or a slow scan.

- **ORM-Specific Tooling**:
    - **Bullet Gem (Rails)**: Detects N+1 queries and unused eager loading during development and testing.
    - **Django Debug Toolbar**: Provides a panel showing all SQL queries run for a request, including their time and a quick `EXPLAIN` link.


### SQL

Short for Structured Query Language. It is used to access data in Relational Database Management Systems (RDBMS), which use a rigid schema to store data generally in tables:

- no duplicate data (normalized)
- rigid and schema-enforced structure by design
- optimized to minimize data storage footprint
- often use a single server by design; vertical scaling (expensive)

### NoSQL

Non-relational databases: key-value, graph, document, multi-column, among others

- built to change and adapt at scale, low schema enforcement, flexible, fields may vary per document
- high throughput with low latency; multiple servers by design (horizontal scaling)
- lower cost storage
- duplicated data requires additional quality checks (denormalized)
- apps need to adapt with evolving data structures
- optimized for data use

### Resources
- https://newsletter.systemdesignclassroom.com/p/performance-doesnt-start-at-select
- https://planetscale.com/blog/the-principles-of-extreme-fault-tolerance
- https://pthorpe92.dev/databasemaxxing/
- https://pthorpe92.dev/wal-checkpoint-performance/
- https://github.com/session-replay-tools/mysql-replay-module | a tcpcopy module for MySQL session replay | can use tools like tcpdump to capture the complete session, and then use tcpcopy for replay
- https://github.com/mayfer/dbpill | PostgreSQL proxy that intercepts all queries & provides a web interface to profile them
- check database section on learn.txt

# Logging

Key Terms: wide event logging, canonical log lines, sampling, tail sampling, indexing

For instance, if you have large distributed systems and many micro services you could have an “observability service” that takes the logs of all of them, i.e a collector that splits the data into three streams: traces, logs, and metrics. Each stream is sent to a Receive & Process unit that prepares it for storage and analysis.
So you have them in one place in one format for processing, indexing, sampling, querying (instead of searching), insights, debugging, crossing data, etc. This helps to keep costs under control and ordered too.

- always store errors
- always store low requests
- always store specific users (VIPs)
- sample the rest: store only 5% of the “happy path” requests and flows (or whatever suits you)

## Resources
- https://loggingsucks.com
- https://www.evlog.dev
- https://newsletter.theskilledcoder.com/p/how-to-log-1m-eventssec-without-slowing
- https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
- https://github.com/Dicklesworthstone/automatic_log_collector_and_analyzer | replace Splunk in your small company with this one weird trick; collect and analyze logs from remote machines hosted on AWS

Migrar la metadata de los logs a atributos de OpenTelemetry en los Spans es de las mejores decisiones que se pueden tomar. Si a eso lo combinas con una buena estrategia de sampleo e indexación y generas metricas desde esos atributos mejoras la observabilidad y bajas costos.
Usar JSON y coordinar el significado de campos entre los servicios soluciona mucho (el ElasticSearch por ej tira logs al suelo si dos servicios tienen campos con el mismo nombre con tipos distintos, incluso si un tipo abarca al otro). Con Event Driven lo mejor es gestionar trazas. Grafana Tempo es una muy buena opción

# Testing

## Resources

- https://theskilledcoder.com/posts/fundamental-concepts/testing-concepts
- https://theskilledcoder.com/posts/low-level-design/unit-testing
- https://theskilledcoder.com/posts/low-level-design/integration-testing
- https://theskilledcoder.com/posts/low-level-design/testing-patterns


# SLOs, SLAs, SLIs

## Service Level Objectives

This is what you aim for, your goal. You try to reach this objective. You can know if you are near or far by your indicators. Usually is tighter than what you agreed on. For example, a restaurant tells you that you will have your food in 30 minutes, but internally they are aiming to have it in 20 minutes. This way you have margin to test strategies, processes and see what sticks and what does not.

## Service Level Agreements

This is what you agree with the client/s on. Anything below this has potential contractual penalties. Usually you provide the client an estimate with a certain margin for you to operate and have room. This also establishes your error budget, i.e, the total maximum failures allowed. Anything beyond this budget incurs in penalties.

## Service Level Indicators

This is what helps you measure your processes and lets you define an objective. Thus is very important to document, log and monitor.


# Cloud & On-Prem

## 1. Code-Level Best Practices

- **Choose the right deployment model per component**
  - Core business logic or differentiators → build and run in‑house (full control).
  - Standard infrastructure (databases, queues, object storage) → prefer managed cloud services unless your team has deep ops skills and predictable load.

- **Design cloud‑native, not just “lift and shift”**
  - Treat local VM disks as ephemeral caches, never as durable storage.
  - Persist state in object storage (S3, Blob Storage) or a managed database; avoid file‑based persistence on virtual disks (EBS).
  - Decouple storage and compute so each can scale independently – assume data lives over the network.

- **Mitigate vendor lock‑in with abstraction**
  - Wrap cloud‑specific APIs behind your own interfaces (e.g., a `BlobStore` interface that can be backed by S3, Azure Blob, or MinIO).
  - Prefer standard protocols (S3‑compatible, SQL) over proprietary extensions unless the unique feature gives a decisive advantage.

- **Expect and handle partial failures**
  - Every I/O call to cloud services needs retries with exponential backoff, idempotency keys, and circuit breakers.
  - Instrument extensively – when you can’t see the provider’s internals, your own telemetry is the only debugging tool.

- **Embrace multi‑tenancy awareness**
  - Even if you’re the only tenant today, code defensively: add namespaces, rate limiting, and quotas to prevent noisy‑neighbour problems.

### Examples

**Wrap a cloud‑specific storage API behind an interface so you can swap implementations later**

```typescript
// file-storage.interface.ts
export interface FileStorage {
  upload(bucket: string, key: string, body: Buffer): Promise<void>;
  download(bucket: string, key: string): Promise<Buffer>;
}

// s3-file-storage.service.ts
import { Injectable } from '@nestjs/common';
import { S3Client, PutObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3';
import { FileStorage } from './file-storage.interface';

@Injectable()
export class S3FileStorage implements FileStorage {
  private s3 = new S3Client({ region: process.env.AWS_REGION });

  async upload(bucket: string, key: string, body: Buffer) {
    await this.s3.send(new PutObjectCommand({ Bucket: bucket, Key: key, Body: body }));
  }

  async download(bucket: string, key: string): Promise<Buffer> {
    const resp = await this.s3.send(new GetObjectCommand({ Bucket: bucket, Key: key }));
    return Buffer.from(await resp.Body!.transformToByteArray());
  }
}

// file-storage.module.ts
import { Module } from '@nestjs/common';
import { S3FileStorage } from './s3-file-storage.service';

@Module({
  providers: [{ provide: 'FileStorage', useClass: S3FileStorage }],
  exports: ['FileStorage'],
})
export class FileStorageModule {}
```

**Resilience: Retries, Idempotency & Circuit Breakers: automatically retry outbound calls to external services, and enforce idempotency**

```typescript
// external-api.service.ts
import { HttpService } from '@nestjs/axios';
import { Injectable, Logger } from '@nestjs/common';
import { retry, catchError, timer, throwError } from 'rxjs';
import { v4 as uuidv4 } from 'uuid';

@Injectable()
export class ExternalApiService {
  private readonly logger = new Logger(ExternalApiService.name);
  constructor(private readonly httpService: HttpService) {}

  async callWithResilience(url: string, payload: any) {
    const idempotencyKey = uuidv4(); // unique per request

    return this.httpService
      .post(url, payload, {
        headers: { 'Idempotency-Key': idempotencyKey },
      })
      .pipe(
        retry({
          count: 3,
          delay: (error, retryCount) => {
            this.logger.warn(`Retry ${retryCount} for ${url}: ${error.message}`);
            return timer(1000 * retryCount);
          },
        }),
        catchError((err) => {
          this.logger.error(`All retries exhausted for ${url}`, err.stack);
          return throwError(() => err);
        }),
      )
      .toPromise();
  }
}
```

**Expect Partial Failures – Log & Monitor Extensively: add correlation IDs and detailed logging so you can debug when you lack access to the provider’s internals.**

```typescript
// logging.interceptor.ts
import { Injectable, NestInterceptor, ExecutionContext, CallHandler } from '@nestjs/common';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Logger } from '@nestjs/common';
import { v4 as uuidv4 } from 'uuid';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const req = context.switchToHttp().getRequest();
    req.correlationId = req.headers['x-correlation-id'] || uuidv4();
    const logger = new Logger('HTTP');
    const now = Date.now();
    return next.handle().pipe(
      tap(() =>
        logger.log({
          message: 'Request completed',
          correlationId: req.correlationId,
          path: req.url,
          duration: `${Date.now() - now}ms`,
        }),
      ),
    );
  }
}
```

## 2. Cost‑Wise Decisions You Can Influence Daily

- **Match infrastructure to workload shape**
  - Predictable, steady load → self‑hosting or reserved instances often cheaper.
  - Spiky, unpredictable load → managed services with autoscaling or serverless save money by releasing idle resources.
  - Avoid provisioning for theoretical peak; use autoscaling groups or scale‑to‑zero options.

- **Treat performance optimisation as cost optimisation**
  - Faster queries = less billed compute time. Profile hot paths, eliminate polling, add indexes, and reduce data transfers.
  - Use per‑call or per‑user cost visibility to let engineers see the financial impact of design choices.

- **Plan capacity financially, not just technically**
  - Set budgets and alerts for cloud spend.
  - Know the service limits (max processes, API rate limits, storage caps) and design around them from day one.
  - Prefer services that bill on actual usage (serverless functions, pay‑per‑query databases) when workloads vary.

- **Value your team’s time**
  - A $500/month service that saves a senior engineer 20 hours a month is usually the right choice.
  - If your team already runs a well‑tuned self‑hosted system with low toil, moving to the cloud may not pay off.

### Examples

**Offload Spiky Load to Queues (Pay Only for What You Use): use Bull queues and run worker processes that can be scaled independently, possibly down to zero when idle.**

```typescript
// report.controller.ts
@Controller('reports')
export class ReportController {
  constructor(@InjectQueue('analytics') private readonly analyticsQueue: Queue) {}

  @Post()
  async requestReport(@Body() body: { userId: string }) {
    await this.analyticsQueue.add('generate-report', body);
    return { message: 'Report generation queued – worker will process it' };
  }
}

// analytics.processor.ts
import { Processor, Process } from '@nestjs/bull';
import { Job } from 'bull';

@Processor('analytics')
export class AnalyticsProcessor {
  @Process('generate-report')
  async handleReport(job: Job<{ userId: string }>) {
    // heavy computation (e.g., aggregate data, generate PDF)
    // ... only billing for the time this worker runs
  }
}
```

**Make Cost Visible Per Request: add a middleware that estimates the compute cost of each request – turning performance into a financial metric.**

```typescript
// cost-estimation.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

const INSTANCE_COST_PER_SECOND = 0.0000056; // hypothetical $0.02 per hour
let requestCount = 0;

@Injectable()
export class CostEstimationMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    const start = process.hrtime.bigint();
    res.on('finish', () => {
      const durationSec = Number(process.hrtime.bigint() - start) / 1e9;
      const cost = durationSec * INSTANCE_COST_PER_SECOND + 0.000001; // plus tiny I/O overhead
      requestCount++;
      console.log(
        `[COST] ${req.method} ${req.originalUrl} ~ $${cost.toFixed(6)} | total requests: ${requestCount}`,
      );
    });
    next();
  }
}
```

**Leverage Metered Billing: Prefer On‑Demand Resources: use a database in on‑demand capacity mode to pay only for actual reads/writes**

```typescript
// dynamodb-options.factory.ts
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocument } from '@aws-sdk/lib-dynamodb';

export const createDynamoDBClient = () => {
  const client = new DynamoDBClient({ region: 'us-east-1' });
  return DynamoDBDocument.from(client);
};

// When creating tables via IaC (CDK, Terraform) set BillingMode: PAY_PER_REQUEST
// This avoids provisioned capacity waste and automatically handles variable traffic
```


## 3. Scale‑Wise Architecture Rules of Thumb

- **Separate storage and compute from the start**
  - Keep data in scalable managed stores, compute in stateless containers or functions.
  - This lets you scale read replicas, add workers, or burst for large jobs without moving data.

- **Use elastic, ephemeral resources for variable loads**
  - For periodic analytics, spin up a large cluster, run the job, tear it down – no idling.
  - Design batch jobs as horizontally scalable units (queue‑based workers) so the system can add/remove compute dynamically.

- **Design data layouts for cloud storage APIs**
  - Object storage prefers larger immutables; pack rows into columnar formats (Parquet, ORC) and use predicate pushdown.
  - Filter and aggregate close to storage to minimise network transfer costs and latency.

- **Avoid virtual‑disk‑based scaling illusions**
  - EBS volumes look like local disks but introduce network I/O latency and single‑instance limits.
  - Use cloud‑native stores unless you absolutely require low‑latency block storage – and if you do, size it carefully.

- **Plan for multi‑service integration complexity**
  - Every cloud service you add increases the integration tax (auth, error handling, monitoring).
  - Standardise on a few well‑known services and document their interactions.
  - Invest in repeatable, automated deployments; manual steps don’t scale with people or traffic.

### Examples

**Separate Storage and Compute from Day One: treat compute as stateless and storage as a remote service – never write to local disk as a durable store**

```typescript
// image-processing.service.ts
import { Injectable, Inject } from '@nestjs/common';
import { FileStorage } from './file-storage.interface';
import { ImageProcessor } from './image-processor';

@Injectable()
export class ImageService {
  constructor(
    @Inject('FileStorage') private readonly storage: FileStorage,
    private readonly processor: ImageProcessor,
  ) {}

  async resizeAndStore(bucket: string, inputKey: string, outputKey: string, width: number) {
    const imageBuffer = await this.storage.download(bucket, inputKey);
    const resized = await this.processor.resize(imageBuffer, width);
    await this.storage.upload(bucket, outputKey, resized);
    return { outputKey };
  }
}
// The service has no disk footprint; it can be scaled horizontally without worrying about local state.
```

**Elastic, Ephemeral Resources for Variable Workloads: configure queue consumers with adjustable concurrency; pair with an auto‑scaler to add/remove worker instances based on job volume**

```typescript
// image-resize.processor.ts
import { Processor, Process } from '@nestjs/bull';
import { Job } from 'bull';

@Processor('image-resize')
export class ImageResizeProcessor {
  @Process({
    name: 'resize',
    concurrency: parseInt(process.env.RESIZE_CONCURRENCY ?? '5', 10), // adjust via env
  })
  async handleResize(job: Job<{ bucket: string; key: string; width: number }>) {
    // stateless resize logic, pulling from S3 and pushing back
  }
}
//Coupled with a metric‑based autoscaler (KEDA), the number of worker pods can drop to zero when the queue is empty.
```

**Prefer Cloud‑Native Data Layouts (Large Immutable Files): write data in columnar or append‑only formats that work well with object storage, not small random‑access files.**

```typescript
// event-log.service.ts
import { Injectable, Inject } from '@nestjs/common';
import { FileStorage } from './file-storage.interface';
import { TransformableInfo } from './appender.interface';

@Injectable()
export class EventLogService {
  constructor(@Inject('FileStorage') private readonly storage: FileStorage) {}

  async appendEvent(bucket: string, key: string, event: Record<string, any>) {
    // Read existing file (a newline-delimited JSON file, for example)
    let logBuffer: Buffer;
    try {
      logBuffer = await this.storage.download(bucket, key);
    } catch {
      logBuffer = Buffer.from('');
    }
    const line = JSON.stringify(event) + '\n';
    const newBuffer = Buffer.concat([logBuffer, Buffer.from(line)]);
    await this.storage.upload(bucket, key, newBuffer);
  }
}
//Later, query these files directly via Athena or load them into a columnar database – no costly block storage.
```

**Handle Multi‑Service Integration Complexity: use message‑based communication between services to reduce tight coupling and enable independent scaling.**

```typescript
// order.module.ts
import { Module } from '@nestjs/common';
import { ClientsModule, Transport } from '@nestjs/microservices';

@Module({
  imports: [
    ClientsModule.register([
      {
        name: 'INVENTORY_SERVICE',
        transport: Transport.RMQ,
        options: {
          urls: [process.env.RABBITMQ_URL],
          queue: 'inventory_queue',
          queueOptions: { durable: true },
        },
      },
    ]),
  ],
  // ...
})
export class OrderModule {}

// order.service.ts
import { Inject, Injectable } from '@nestjs/common';
import { ClientProxy } from '@nestjs/microservices';

@Injectable()
export class OrderService {
  constructor(@Inject('INVENTORY_SERVICE') private readonly inventoryClient: ClientProxy) {}

  async placeOrder(order: any) {
    // ... save order locally
    await this.inventoryClient.emit('order_placed', order).toPromise();
    return { status: 'Order submitted' };
  }
}
//This pattern enables each service to evolve independently, and makes it easier to replace or scale components without a monolith rewrite.
```


---

**Bottom line:** In your daily work, favour managed services for undifferentiated heavy lifting, build applications stateless and storage‑disaggregated from day one, tie performance to cost constantly, and design to scale out (and back in) on demand – all while keeping a clean abstraction layer to avoid lock‑in pain later.

# System Design

## Dean's Principles

- https://www.cs.cornell.edu/projects/ladis2009/talks/dean-keynote-ladis2009.pdf

### Memory and Storage	

Dean's talk emphasizes the immense value of memory (DRAM) due to its speed and the "bumpy ride" of access times across the storage hierarchy. The "Numbers Everyone Should Know" slide provides a critical intuition: accessing data from main memory is 100,000 times faster than a disk seek (100 ns vs. 10 ms).

#### Scenarios

##### E-commerce Product Recommendations

A site like Amazon can't afford to query a disk-based database for every user click. The solution is a distributed in-memory cache (e.g., using Memcached or Redis). User profiles and recently viewed items are stored across a cluster's DRAM. When a user clicks, the recommendation service can fetch this data from memory in ~100 ns, enabling near-instant personalization without touching slower disks.

##### Financial Fraud Detection

A bank's fraud detection system must analyze transactions in real-time. It uses a stream processing system (like Apache Flink) where the last 24 hours of transactions for millions of accounts are held in a distributed in-memory store. This allows the system to check a new transaction against recent patterns and known fraudulent markers with sub-second latency, making an approve/deny decision before the transaction completes.

##### Multiplayer Online Game State

In a game like Fortnite, the state of the world for each match is kept entirely in the RAM of a cluster of game servers. Player positions, health, and actions are read and updated millions of times per second. Storing this data on disk would introduce unacceptable 10 ms delays, making real-time gameplay impossible.

### Uptime and Downtime

Dean's most powerful lesson is his insistence on planning for constant, varied failures: "Things will crash. Deal with it!". He provides a detailed list of expected failures in a new cluster's first year, from thousands of hard drive failures to less frequent but more impactful PDU or rack failures.

#### Scenarios

##### Global SaaS Platform (e.g., Salesforce)

Their mantra is "fault-tolerant software is inevitable". They design their system around the expectation that individual servers and entire racks will fail. Data is replicated across multiple availability zones (AZs), and application servers are stateless behind load balancers. When a server inevitably crashes, the load balancer simply stops sending it traffic, and a new instance is automatically spun up elsewhere. From the user's perspective, the service is uninterrupted.

##### Online Payment Gateway (e.g., Stripe)

They must anticipate "network maintenances" and "router reloads" that cause "30-minute random connectivity losses". To handle this, their system uses asynchronous processing and persistent retry mechanisms. If a payment request to a bank fails due to a network blip, it's not immediately rejected. It's stored in a durable queue and retried later with exponential backoff. This ensures high reliability despite an unreliable network.

##### Social Media Feed (e.g., Twitter/X)

To handle "20 rack failures" a year, the service is sharded and replicated across thousands of servers. The timeline service doesn't rely on any single machine. Your data is stored on multiple servers in a cluster. If a rack of servers goes down, the system continues serving the feed from its replicas, and the user might only experience slightly higher latency while the load balancer avoids the failed rack.

### Netflix's Global Architecture

Netflix's architecture is a masterclass in applying these distributed systems principles. The platform is split into two main parts: the Control Plane (running on AWS) and the Data Plane (its custom Open Connect CDN).

#### Distributed Web Servers Across Regional Data Centers

This design directly addresses the latency problem highlighted by Dean's numbers: a packet from California to the Netherlands and back takes 150,000,000 ns (150 ms), which is 300x slower than a round trip within a single datacenter.

**Problem:** A user in Tokyo can't stream a 4K video from an origin server in Virginia. The latency would be over 100ms, causing constant buffering and a terrible user experience.

**Solution (Data Plane):** Netflix built Open Connect, its own global CDN. They physically place Open Connect Appliances (OCAs)—custom-built caching servers—inside thousands of Internet Service Providers (ISPs) and at internet exchange points around the world.
How Netflix Applies Dean's Principles

#### Memory: Cache Hierarchy

Netflix leverages the memory hierarchy as a core component of its streaming platform, from the origin to the user's device.

##### Global CDN Edge Caching (Open Connect):

**The Strategy:** Popular content is "pre-positioned" on the OCAs, which are equipped with large amounts of RAM and high-speed NVMe SSDs. During off-peak hours (e.g., overnight), Netflix uses predictive algorithms to push the most popular content to these edge servers.

**The Dean Principle:** This is the application of a multi-tier cache. It ensures that when a user hits "play," the initial video chunks are served from the blazing-fast DRAM or SSD of a server that is often within their own ISP's network. The result is that 95% of Netflix's traffic is delivered with less than 100ms latency. This is a massive optimization over a 150 ms cross-continental trip.

##### In-Memory Caching for the Control Plane (EVCache):

**The Strategy:** For the millions of operations happening before you press play—browsing titles, getting recommendations, loading your profile—Netflix uses EVCache, a distributed in-memory data store. EVCache is optimized for sub-millisecond response times.

**The Dean Principle:** This aligns perfectly with Dean's "Numbers Everyone Should Know." EVCache stores user preferences, viewing history, and popular metadata in the 100 ns main memory tier, avoiding the 10 ms disk seek penalty. This makes the entire browsing experience feel snappy and responsive.

#### Uptime & Downtime: Resilience by Design

Netflix's approach to reliability is a direct implementation of Dean's "Deal with it!" philosophy, famously embodied in their practice of Chaos Engineering.

##### Embracing Failure with Chaos Monkey

**The Strategy:** Netflix built a suite of tools to proactively inject failure into their production environment. The most famous is Chaos Monkey, which randomly terminates virtual machine instances during business hours. This forces engineers to build services that can withstand the expected "1000 individual machine failures" per year without impacting users.

**The Dean Principle:** This is the ultimate test of fault-tolerant software. By constantly causing failures, Netflix ensures that its service discovery (Eureka), load balancing, and failover mechanisms work automatically. If a server hosting a user's profile data crashes, the request is instantly routed to another replica, and the user doesn't notice.

##### Designing for Regional Outages (The Spanner Influence):

**The Strategy:** While Netflix's video streaming is mostly a cache-consistency problem, its control plane requires strong consistency for operations like billing, account management, and view-state persistence. To survive a major regional outage (like a PDU failure taking down an entire AWS availability zone), they use multi-region database strategies. The principles from Google's Spanner—a globally distributed database with strong consistency across datacenters—are highly relevant here.

**The Dean Principle:** This anticipates the "~1 PDU failure (~500-1000 machines suddenly disappear)" scenario. By replicating critical user data synchronously across multiple, geographically distinct data centers (e.g., US-East and EU-West), Netflix ensures that a complete regional failure does not cause data loss or a prolonged outage. A user could potentially be seamlessly routed to a different region and continue watching with their place in the show saved.

#### The Result: A Resilient Global Platform

By applying these core principles, Netflix has built a platform that can:

- Serve over 270 million users with a highly personalized experience.
- Deliver video content from 17,000+ Open Connect servers located inside ISPs worldwide, drastically reducing latency.
- Remain available through constant, small-scale failures and even major regional outages, ensuring high user satisfaction and retention.

#### A Blueprint for Global Systems

Jeff Dean's LADIS 2009 keynote provides a timeless blueprint for designing distributed systems at scale. The principles he outlines—understanding the storage hierarchy, designing for inevitable failure, and optimizing for latency—are not abstract concepts but practical necessities.

|Dean's Principle	|Real-World Scenario (Memory) |Real-World Scenario (Uptime/Downtime) |Netflix Application|
|------------------|-----------------------------|--------------------------------------|-------------------|
|Storage Hierarchy & Latency	|E-commerce product recs from in-memory cache (100 ns) vs. disk (10 ms).|Multiplayer game state held in RAM for real-time updates.|	Open Connect CDN caches video on edge servers' SSD/RAM for sub-100ms streaming. EVCache stores user data in memory for fast browsing.|
|Fault Tolerance is Inevitable	 |Financial fraud detection uses distributed in-memory stores for real-time analysis.	|SaaS platforms replicate data across AZs to survive server/rack failures.	|Chaos Monkey randomly terminates production servers to test and ensure automatic failover.|
|Plan for Failures & Graceful Degradation	|Video game state servers use RAM for low latency, with periodic snapshots to disk for recovery.	|Payment gateways use async queues and retries to handle network blips.	|Multi-region database replication (like Spanner) ensures the platform survives a complete regional data center outage.|
|Parallelism & Caching	|Social media feeds use sharded, replicated in-memory stores for high throughput.	|Real-time fraud detection uses parallel in-memory analysis of recent transactions.	|Open Connect's overnight content pre-positioning pushes popular videos to the edge during off-peak hours, reducing strain on the core network.|

In conclusion, the keynote's wisdom transcends its 2009 origin. For any engineer tasked with building a global, always-on service, the lessons are clear: know your numbers, embrace failure as a design constraint, and build systems that are resilient by default. Netflix's success is a testament to the power of these enduring principles.

## CAP Theorem

- https://ferd.ca/beating-the-cap-theorem-checklist.html

Use the CAP theorem to critique systems. The CAP theorem isn’t something you can build a system out of. It’s not a theorem you can take as a first principle and derive a working system from. It’s much too general in its purview, and the space of possible solutions too broad.

However, it is well-suited for critiquing a distributed system design, and understanding what trade-offs need to be made. Taking a system design and iterating through the constraints CAP puts on its subsystems will leave you with a better design at the end. For homework, apply the CAP theorem’s constraints to a real world implementation of Russian-doll caching.

## Resources

- https://github.com/jwasham/coding-interview-university?tab=readme-ov-file#system-design-scalability-data-handling
- https://github.com/donnemartin/system-design-primer
- https://builddistributedsystem.com
- https://theskilledcoder.com/system-design
- https://www.cs.cornell.edu/projects/ladis2009/talks/dean-keynote-ladis2009.pdf
- check system design in interview section on learn.txt


# Git

- git stash, git stash pop
- git clone, git fetch, git pull, git status, git restore, git diff
- git checkout -b new-branch
- git branch -m new-name
- git add -p file-name (partial changes from a file)
- git log
- git diff branch-hash branch-hash
- git merge, git rebase, git squash
- git reflog (recover lost, commited changes, e.x a deleted branch)
- git cherry-pick <commit-hash>
- git worktree add <path> <branch-name> (work on different branches without having to stash or commit changes)
- pre-commit rules, YAML config files
- flags: --staged, -p

# Communicating Ideas

Ideas are important, but they aren't everything. You also need to do a good job explaining your ideas to the world. And if you want the world to care, you need to do so in a way that actually makes sense to people, and in a way that shows them how it might be worth their while to work through the difficulties in understanding your new ideas— because it will allow them to do various new useful things and understand other subjects in useful new ways.

If you're an outsider to a field, rather than focus all your energy on getting the messaging/explanation more rigorous and perfect, or even trying to show how your new ideas in the field can be profitably employed in various applications, you're probably better served trying to find just one well-respected insider to that field and win that one person over completely to the merits of your ideas. Then, that person can serve as your champion, and other important and respected thinkers in that field— who are always extremely busy and don't have unlimited bandwidth to decipher long, impenetrable treatises and mathematical monographs— will have much more of a reason to give your ideas serious consideration; you effectively can piggyback on the accumulated credibility of your mentor.

If people are telling you that your ideas aren't bad, but they should be expressed in a different/better way, maybe take that feedback more seriously, especially if the people who are giving you that feedback are themselves greatly respected and important in your field.

Appeal to intuition first if you want to be understood. You are wasting your great ideas if you don't first discuss how they work and apply in a more tangible and intuitive setting. Then, once you have your audience hooked, you can explain how the ideas actually generalize completely. Start with the simpler cases that are more tangible and intuitive and develop those. That is, start with 2D and 3D, don't start with N-D!


# Leadership

- https://staffeng.com
- https://www.lesswrong.com/posts/KRLGxCaqdgrotyB8z/there-are-only-four-skills-design-technical-management-and

El talento excepcional NO se queda con líderes promedio. Lo he visto demasiadas veces.

Un líder brillante. Un equipo sólido. Resultados que justifican todo. Y de repente: el mejor del equipo renuncia.

¿La razón real?
No fue el salario. No fue otra empresa. Fue que nadie le preguntó a dónde quería llegar.

La diferencia entre un líder que retiene talento y uno que lo pierde... no está en los procesos. Está en las conversaciones.

La mayoría de los líderes "gestiona." Asigna tareas. Revisa resultados. Aprueba o rechaza.
Pero liderar no es gestionar.

¿Cuándo fue la última vez que tuviste una conversación 1:1 que no fuera un reporte de estatus?

Una en la que preguntaste sobre las aspiraciones de esa persona.

Sus fortalezas.  Sus obstáculos.  Su crecimiento real.