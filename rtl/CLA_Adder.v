`timescale 1ns/1ps
// `include "pg_Generator.v"
// `include "CLA_Generator.v"
// `include "Sum_Generator.v"

module CLA_Adder (
  input signed [127:0] A,      // 128-bit input A
  input signed [127:0] B,      // 128-bit input B
  output [127:0] Sum,   // 128-bit sum output
  output Cout           // Carry-out
);

  wire [127:0] G, P, C;  // Generate, Propagate, and Carry-out signals

  // pg generator
  // Generate and Propagate signals for each bit
  assign G = A & B;
  assign P = A ^ B;

  // CLA generator
  // Carry lookahead logic using generate for-loop
  genvar i;
  generate
    for (i = 0; i < 128; i = i + 1) begin
      assign C[i] = G[i] | (P[i] & (i == 0 ? 1'b0 : C[i - 1]));
    end
  endgenerate

  // Sum generator
  // Sum output for each bit
  assign Sum = A ^ B ^ C;

  // Carry-out
  assign Cout = G[127] | (P[127] & C[127]);

endmodule
