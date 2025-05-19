-- Create Category Table
CREATE TABLE Category (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE
);

-- Create Author Table
CREATE TABLE Author (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL
);

-- Create Book Table
CREATE TABLE Book (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ISBN VARCHAR(20) UNIQUE,
    PublishYear YEAR,
    CategoryID INT,
    CONSTRAINT fk_book_category FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);

-- Create BookAuthor Table (Many-to-Many relationship)
CREATE TABLE BookAuthor (
    BookID INT,
    AuthorID INT,
    PRIMARY KEY (BookID, AuthorID),
    CONSTRAINT fk_ba_book FOREIGN KEY (BookID) REFERENCES Book(BookID),
    CONSTRAINT fk_ba_author FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);

-- Create Member Table
CREATE TABLE Member (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    JoinDate DATE NOT NULL
);

-- Create Librarian Table
CREATE TABLE Librarian (
    LibrarianID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL
);

-- Create Loan Table
CREATE TABLE Loan (
    LoanID INT AUTO_INCREMENT PRIMARY KEY,
    BookID INT NOT NULL,
    MemberID INT NOT NULL,
    LibrarianID INT,
    LoanDate DATE NOT NULL,
    ReturnDate DATE,
    CONSTRAINT fk_loan_book FOREIGN KEY (BookID) REFERENCES Book(BookID),
    CONSTRAINT fk_loan_member FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    CONSTRAINT fk_loan_librarian FOREIGN KEY (LibrarianID) REFERENCES Librarian(LibrarianID)
);