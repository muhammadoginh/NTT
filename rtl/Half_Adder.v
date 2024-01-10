`timescale 1ns/1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.11.2023 22:34:34
// Design Name: 
// Module Name: Half_Adder
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: A half-adder adds two binary digits A and B and produces the sum (Sum) and the carry-out (Cout).
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Half_Adder(
    input A,
    input B,
    output Cout,
    output Sum
    );

    // implementation using dataflow level architecture
    assign Cout = A & B;
    assign Sum = A ^ B;

endmodule