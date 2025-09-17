The Information Technology field is a vast and intricate industry.  As a future cloud professional, there is a certain level of required knowledge that one must possess in order to effectively perform the role.  The following documentation will serve as a brief primer on the important information you need to know about some of the most common aspects of computing.  We will focus on the following topics: 

- Computer components
- OS/SW Segmentation
- File vs. Directory vs. Application distinction
- IDEs and code compiling

Computer components

It seems counterintuitive that you should need to know the components of a computer when working in the cloud.  However, this information is important because much of the same material can be related to both physical computing and cloud infrastructure.  

Here is a list of the computer components we will be discussing in this documentation: 

- Computer Case
- Motherboard
- CPU
- RAM
- Video Card
- Storage
- Power Supply
- Monitor
- Keyboard and Mouse

Computer Case
- The computer case is a container that encloses the other parts of the computer.  
- Cases come in various sizes designed to accommodate the size of different computer parts.  It can also come in multiple configurations such cases with colored lights, various shapes, or the ability to assist with cable management.  
- Another important feature of computer cases is the management of airflow.  Computer components naturally give off massive amounts of heat while running.  This heat must be managed properly otherwise computer components can become damaged affecting the computer's performance.  Computer Case account for this temperature management via the use of cooling fans or more advanced cooling systems such as liquid cooling which safely dissipate excess heat.  

Motherboard
- The Motherboard (or main board in some circles) is the device that connects all the other components together.  
- It is also responsible for communication between all of the other components of the computer. 
- Another important attribute of the motherboard is that its size has an influence on the type of computer case that the PC uses.  For example, if a case size is designated as mini-ATX, you would be unable to use an ATX sized motherboard.  The mother board wouldn't be able to fit inside along with its other computer components.  
- Choice of Motherboard influences many other decisions when it comes to the capability of the PC such as CPU, storage, memory, etc.  

CPU
- The CPU, also called the Central Processing Unit, is usually called the "brain" of the computer.  
- This is because it is responsible for all of the complex calculations required by the computer for normal operations.  
- CPUs come in different types and configurations based on the motherboard it is designed for.  The two major manufacturers of CPUs are Intel and AMD.  

RAM
- RAM stands for Random Access Memory.  It is often referred to as just Memory.  This device temporarily stores data for use by the computer during its session.  
- Having a large amount of memory allows the PC work with more types of data at one time.  An example of this would be the ability to run multiple programs at once and seamlessly cycle between them without any noticeable performance issues.  
- RAM comes in different sizes from the tiny kilobyte size all the way up to gigabytes.  Modern PCs typically use as low as 8GB to as high as 64 GB with some specialized servers using even higher ranges.  

Video Card
- The Video Card is a separate device that performs all the graphics related operations and calculations for a computer.  
- A specialized device, it is useful for graphics intensive programs, development of said programs, and operations with demanding front-end applications such the recent AI powered web apps.  Video cards also have physical connections to allow interface between a computer and a monitor or TV.  
- The primary benefit of a Video Card is that it has its own dedicated GPU (Graphical Processing Unit) and RAM so that graphical operations can be handled separately from the CPU and motherboard.  This leads to optimal performance using less computer resources.  
- There are two primary Video card vendors who dominate the space: Nvidia and AMD.  Most cards will be from these two corporations with various other manufacturers making cards using their configuration. 

Storage
- Storage is a device used to contain data for long term use by the computer and its user.  
- Storage comes in two main types which have different uses: HDD and SSD.  
- HDD or Hard Disk Drive is the older technology that is common to all computers.  It consists of physical disks stacked on top of each other in an enclosure.  While slower performance wise compared to an SSD, it is still typically better for long term storage of data.  The newer technology and which is fast becoming the new standard is called SSD or Solid State Drive.  Of the two types, SSDs tend to be faster when accessing data and overall performance.  An application installed on an SSD as opposed to an HDD will have a noticeable performance improvement when running and performing operations. 
- Both drive types come in various sizes based on user requirements.  

Power Supply
- Although these computer components perform necessary functions for the PC, the most important component is called the Power Supply.  
- Also referred to as the PSU or Power Supply Unit, it generates the necessary electricity for the computer to run.  It provides an interface between your wall power outlet and the computer itself.  The Power Supply then has several connectors that plug into the different components of the PC to supply power. 
- PSUs come in different power levels called watts.  The higher the wattage, the greater number of compatible computer components it is able to power.  
- Because the device is responsible for providing power to all the components of the PC, deciding which level of Power Supply is as vital a choice as which Computer Case you use and the Motherboard that should fix inside it.  

Monitor
- While the other components of the PC are doing most of the heavy lifting of computer operations, users still require a way to see the results of these operations.  The Monitor is responsible for this output.
- An important attribute of monitors is its resolution which is the number of pixels displayed at once on the screen.  This attribute is represented by "width x height." For instance, a computer monitor may advertise a high definition resolution by stating that it has a 1920x1080p screen.
- Monitor size and type are as varied as modern televisions.  Because of this and the technology involved, there is a lot of overlap between the two.

Keyboard and Mouse
- Users of the computer need a way to interact with the machine.  The Keyboard and Mouse are the primary way users accomplish this.  


Resources

The Parts of a Computer Explained for the Average Person
by Charles Buege (CharlesBuege-Fuel) | 01-08-2025
https://live.paloaltonetworks.com/t5/fuel-user-group-blogs/the-parts-of-a-computer-explained-for-the-average-person/ba-p/1000912

Basic Components of a Computer: How They Function for Users
Information Technology Blog | American Public University
by Dr. Lindan A. Moya | 04-14-2025 
https://www.apu.apus.edu/area-of-study/information-technology/resources/basic-components-of-a-computer/


OS_SW Segmentation

- When an operating system or a piece of software accesses parts of a function or its code, it tends to attempt access all in sequence and load each action into memory so that everything required by the OS or software is available when needed.  This process is very inefficient for the computer's memory.  This can lead to programs running slowly or unforeseen errors.  Segmentation is a solution to this problem.  
- Segmentation divides these individual actions into related code segments that can then be grouped together more efficiently.  The most common example of this is the use of functions in modern programming.  
- A function is a small section of code that is designed to run separately.  By using functions, a developer can institute different tasks within code and have them available whenever needed.  All without any consistent memory use.  A piece of software or a task in the operating system runs and then when a certain process is needed, the function executes because it is already available within the code.  No extra memory needed to store this information.  

Resources

Segmentation in Operating System (OS): An Ultimate Guide
by Richard Harris | 09-08-2025
https://www.theknowledgeacademy.com/blog/segmentation-in-operating-system/

The Ultimate Guide to Segmentation in Operating Systems
by By Simplilearn | 07-31-2025
https://www.simplilearn.com/segmentation-in-os-article


File vs. Directory vs. Application

- Within computing, the data being manipulated by the computer can come in three different forms.  These are referred to as a file, directory, and application.  
- A file is the basic form of data.  It is a container that data is stored on the computer.  This data can be stored locally on the computer's storage drive or an external drive.  Files can contain different types of information such as text, images, audio, video, or special files which can launch programs.  
- A directory or folder is another type of container that files can be placed into.  Typically, any type of file can be placed in a directory and it is an important means of organizing different files.  
- The final form of data is called an application.  Also known as a program or an app, this data type is a combination of files, folders, code all combined into a special file called and executable.  An executable allows the user to launch an application so that they can use it for its intended purpose.  
- There are many examples of an application such as word processors, image viewers, music players, etc.  The most well known application is the one that the computer absolutely needs to function: the operating system.   

Resources

Difference Between File and Folder: Explained
by The Knowledge Academy | 07-08-2025
https://www.theknowledgeacademy.com/blog/difference-between-file-and-folder/

What is an application?
by Alexander S. Gillis | Oct-22-2024
https://www.techtarget.com/searchsoftwarequality/definition/application


IDEs and code compiling

- An Integrated Development Environment or IDE, is a specialized piece of software that allows Software Developers to create computer programs in an easier fashion.  
- The application centralizes several tools useful to programmers into a single location.  For example, IDEs tend to know the syntax, best practices, and common rules of a particular language.  Therefore, the program can use quality of life tools such as syntax highlighting, code completion, and automation to enable users to build their projects faster.  An IDE can catch mistakes, suggest corrections, and refactor code to be more inline with best coding practices.  
- IDEs also support a number of plugins to increase the functionality of the application.  Many coding languages have additional libraries and add-ons that allow for new ways to perform actions in the language.  
- One of the most important features of an IDE is the ability to build complete programs in an action called compiling.  
- Code compiling is the act of taking the language and syntax of a higher level programming language and converting it into lower level machine language which the computer can directly understand.  
- Along with this action, the compile process adds additional necessary plugins and dependencies and combines them in to a file called an executable.  The executable is the final form of the new software which users can then launch to run the application.  
- IDEs and their ability to code compile are vital tools of the software development process. 

Resources

What is an IDE (Integrated Development Environment)?
by Amazon Web Services Team | Site accessed: 09-02-2025
https://aws.amazon.com/what-is/ide/

What is an IDE? Understanding Integrated Development Environments
by Codecademy Team | Site accessed: 09-02-2025
https://www.codecademy.com/article/what-is-ide

What is a compiler?
by Josh Schneider and Ian Smalley
https://www.ibm.com/think/topics/compiler

What compiling code means: explain like I'm Five
by Arika O
https://dev.to/arikaturika/code-compiling-explain-like-im-five-4mkj

Keep in mind that this is a small introduction to the concepts you will need to learn as a cloud professional.  Further investigation into these topics will be helpful in growing your experience in the cloud industry.
