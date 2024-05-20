INSERT INTO [Transaction] (Transaction_id, Account_Id, Transaction_Type, Amount, Transaction_Date)
VALUES
('T1', 'A1', 'Withdrawal', 1500, '2024-04-29'),
('T10', 'A10', 'Deposit', 1500, '2024-04-29'),
('T11', 'A10', 'Withdrawal', 10000, '2024-05-02'),
('T2', 'A2', 'Deposit', 1000, '2024-04-29'),
('T3', 'A3', 'Transfer', 200, '2024-05-01'),
('T4', 'A4', 'Withdrawal', 800, '2024-04-30'),
('T5', 'A5', 'Deposit', 700, '2024-04-30'),
('T6', 'A6', 'Withdrawal', 600, '2024-04-30'),
('T7', 'A7', 'Deposit', 1200, '2024-04-29'),
('T8', 'A8', 'Transfer', 400, '2024-05-01'),
('T9', 'A9', 'Withdrawal', 300, '2024-05-01');

INSERT INTO Accounts (Account_id, Customer_id, Account_Type, Balance)
VALUES
('A1', 'C1', 'Savings', 1165000),
('A10', 'C10', 'Current', 11000000),
('A2', 'C2', 'Current', 7500000),
('A3', 'C3', 'Savings', 3000),
('A4', 'C4', 'Zero_balance', 10000),
('A5', 'C5', 'Savings', 6000),
('A6', 'C6', 'Current', 8500000),
('A7', 'C7', 'Savings', 4000),
('A8', 'C8', 'Current', 9000000),
('A9', 'C9', 'Zero_balance', 2000);

INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, Address)
VALUES
('C1', 'Anusha', 'Tikarya', '2001-12-29', 'anu@gmail.com', '9109366707', 'Indore'),
('C10', 'Aryan', 'Pardhi', '2001-05-30', 'aryan@gmail.com', '7692256707', 'Pune'),
('C2', 'Anu', 'arya', '2002-05-06', 'arya@gmail.com', '9196456707', 'Bhopal'),
('C3', 'Ansh', 'sharma', '2003-02-24', 'ansh@gmail.com', '9196453806', 'Bhopal'),
('C4', 'Bhanu', 'Gupta', '2002-05-12', 'bhanu@gmail.com', '7196456707', 'Pune'),
('C5', 'chavi', 'Malani', '2002-11-06', 'chavi@gmail.com', '9192346707', 'Bhopal'),
('C6', 'Tony', 'Verma', '2001-11-06', 'tony@gmail.com', '9192346605', 'Delhi'),
('C7', 'Rashi', 'Vyas', '2004-11-01', 'rashi@gmail.com', '7692346707', 'Indore'),
('C8', 'Prachi', 'Joshi', '2001-01-05', 'joshi@gmail.com', '9192346707', 'Indore'),
('C9', 'Prachi', 'Chouhan', '2004-05-06', 'prachi@gmail.com', '8992346707', 'Bhopal');
