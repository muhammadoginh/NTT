`timescale 1ns/1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.11.2023 22:34:34
// Design Name: 
// Module Name: Full_Adder
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: A full-adder adds two binary digits A and B and produces the sum (Sum) and the carry-out (Cout).
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module Full_Adder(
    input A,
    input B,
    input Cin,
    output Cout,
    output Sum
);

    // Full Adder using dataflow architectural level of abstaction
    assign Cout = (A & B) | ((A ^ B) & Cin);
    assign Sum = A ^ B ^ Cin;

endmodule