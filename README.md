🎬 Cineplex Ticketing Management System

A Python console-based application that simulates a real-world Cinema Ticket Booking System using Object-Oriented Programming (OOP) principles.
The system allows cinema management to create halls, add shows, view available seats, and book tickets — all while demonstrating core OOP concepts like Encapsulation, Inheritance, Abstraction, and Polymorphism.

🚀 Features
🏢 Star_Cinema Class

Acts as the parent (base) class for all cinema operations.

Maintains a global list of all halls through the class attribute hall_list.

Provides a method entry_hall() to register new halls into the cinema system.

🎞️ Hall Class

Inherits from Star_Cinema.

Represents a single cinema hall with attributes and methods for managing shows and seat bookings.

Main Responsibilities:

Manage shows (add, list).

Manage seats (view, book).

Handle errors (invalid show ID, invalid seat, already booked seat).

⚙️ System Workflow

Initialize Cinema System

Create an instance of Hall with rows, cols, and a unique hall_no.

Automatically registers itself to Star_Cinema.hall_list through inheritance.

Add Shows

Add new shows using entry_show(id, movie_name, time).

Each show creates a 2D list of seats (available “O” by default).

Book Seats

Select a show using its ID.

Provide list of (row, col) pairs to book seats.

Booked seats are marked as “X”.

View Information

view_show_list() → Lists all running shows.

view_available_seats(id) → Displays seat layout for the selected show.

🧩 Error Handling

The system handles common user mistakes with friendly messages instead of crashing:

❌ Invalid show ID → “No show found with this ID.”

🚫 Already booked seat → “Seat already booked. Choose another one.”

📍 Invalid seat number → “Invalid seat coordinates.”

🧱 Object-Oriented Programming (OOP) Concepts Applied
1. Encapsulation 🛡️

All sensitive data (like seat layout, show list, and hall info) are private/protected (__seats, __show_list).

Access and modification happen only through public methods such as entry_show(), book_seats(), and view_available_seats().

This prevents direct modification of internal data, ensuring data integrity.

2. Inheritance 🔁

Hall class inherits from the Star_Cinema class.

Through inheritance, every Hall object is automatically added to Star_Cinema.hall_list when created.

This creates a parent-child relationship that allows centralized hall management.

3. Abstraction 🎭

Complex internal logic (like seat allocation and booking validation) is hidden behind simple method calls.

Users don’t need to know how the 2D seat structure is managed; they just call book_seats() or view_available_seats().

This demonstrates real-world abstraction, focusing on “what to do” instead of “how it’s done.”

4. Polymorphism 🔄

Polymorphism is achieved conceptually by using same-named methods that behave differently depending on the object or context.

For example, different halls can call methods like entry_show() and book_seats(), but each instance manages its own data independently while calling the same method.

This demonstrates method-level polymorphism across multiple objects.

🖥️ Example Console Flow
Welcome to Cineplex Ticketing Management 🎟️

1. View All Shows
2. View Available Seats
3. Book Ticket
4. Exit

Enter choice: 1

Shows Running:
---------------------------------
Show ID: 101 | Movie: Inception | Time: 6:00 PM | Hall: 1
Show ID: 102 | Movie: Interstellar | Time: 9:00 PM | Hall: 1
---------------------------------

Enter choice: 2
Enter Show ID: 101

Available Seats:
O O O O O
O X X O O
O O O O O

🧠 Concepts Demonstrated
Concept	Description	Example in Project
Class & Object	Template and instances for system design	Star_Cinema, Hall
Encapsulation	Restricting access to data	Private attributes (__seats, __show_list)
Inheritance	Reusing code between classes	Hall(Star_Cinema)
Abstraction	Hiding complex logic	Booking, Seat display methods
Polymorphism	Same method name, different behaviors	book_seats() per hall
Error Handling	Graceful handling of runtime issues	try-except blocks
🛠️ Requirements

Python 3.8 or higher

Runs on any standard console (Windows, macOS, Linux)

📂 Project Structure
Cineplex_Ticketing_Management/
│
├── cineplex_ticketing.py     # Main Python source code
├── README.md                 # Project documentation

🔐 Data Protection

Private attributes (__attribute) protect internal data.

Only predefined methods control modification or retrieval.

This ensures data encapsulation and controlled access.

👨‍💻 Author

Developed by: MD AJHARUL ISLAM AKADNA
Language: Python
Project Type: Console Application (OOP-based)
Concept Focus: Complete Implementation of OOP Principles
