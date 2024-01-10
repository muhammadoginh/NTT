`timescale 1ns/1ps
`include "CLA_Adder.v"

module CLA_Adder_tb;

  reg [127:0] A, B;
  wire [127:0] Sum;
  wire Cout;

  // Instantiate the 128-bit CLA adder
  CLA_Adder uut (.A(A), .B(B), .Sum(Sum), .Cout(Cout));

  // Test inputs
  initial begin
    $dumpfile("CLA_Adder_tb.vcd");
    $dumpvars(0, CLA_Adder_tb);

    // Initialize input vectors A and B with binary numbers
    A = 1152921504606830593;
    B = 128;

    // Monitor inputs and outputs
    $monitor("A=%b, B=%b, Sum=%b, Cout=%b", A, B, Sum, Cout);

    // Run the simulation
    #10 $finish;
  end

endmodule
