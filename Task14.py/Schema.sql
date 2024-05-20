use HMBank
CREATE TABLE [Customers] (
  [customer_id] VARCHAR(255),
  [first_name] VARCHAR(255),
  [last_name] VARCHAR(255),
  [DOB] DATE,
  [email] VARCHAR(255),
  [phone_number] VARCHAR(10),
  [Address] VARCHAR(255),
  PRIMARY KEY ([customer_id])
);

CREATE TABLE [Accounts] (
  [Account_id] VARCHAR(20),
  [Customer_id] VARCHAR(255),
  [Account_Type] VARCHAR(255),
  [Balance] INT,
  PRIMARY KEY ([Account_id]),
  CONSTRAINT [FK_Accounts.Customer_id]
    FOREIGN KEY ([Customer_id])
      REFERENCES [Customers]([customer_id])
);

CREATE TABLE [Transaction] (
  [Transaction_id] VARCHAR(20),
  [Account_Id] VARCHAR(20),
  [Transaction_Type] VARCHAR(255),
  [Amount] INT,
  [Transaction_Date] DATE,
  PRIMARY KEY ([Transaction_id]),
  CONSTRAINT [FK_Transaction.Account_Id]
    FOREIGN KEY ([Account_Id])
      REFERENCES [Accounts]([Account_id])
);
