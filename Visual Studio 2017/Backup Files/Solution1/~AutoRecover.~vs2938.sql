

SELECT 
    c.CustomerID,
    c.CustomerName,
    o.OrderID,
    o.Product
    
FROM 

    [dbo].[Customer] c

Left outer JOIN 

    [dbo].[Orders] o ON c.CustomerID = o.CustomerID
