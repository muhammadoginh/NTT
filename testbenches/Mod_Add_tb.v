`timescale 1ns/1ps
`include "../rtl/Mod_Add.v"

module Mod_Add_tb();
    // Input
    reg clk;
    reg rstn;
    reg [47:0] A;
    reg [47:0] M;
    reg [47:0] q;

    // Output
    wire [47:0] B;

    // Instantiate the unit under test
    Mod_Add uut(
        .clk(clk),
        .rstn(rstn),
        .A(A),
        .M(M),
        .q(q),
        .B(B)
    );

    // generate stimuli
    initial
    begin
        $dumpfile("Mod_Add_tb.vcd");
        $dumpvars(0, Mod_Add_tb);
        
        clk = 1'b0;
        rstn = 1'b0;
        // Assign test case values
        A = 48'b111000110100001110111011101001110010000111010;
        M = 48'b100001011111011111110111110101010010100011011100;
        q = 48'b111111111111111111111111111111111111110111110001;
        #1 rstn = 1'b1;        
    end
    
    // Wait for a few simulation cycles
    initial #10 A = 48'b111011110110100000110010000010101110011101011111;   //263230795212639;
    initial #10 M = 48'b1010111001010011110010011101101100000101101101;     //47918723023213;
    
    // Wait for a few simulation cycles
    initial #20 A = 48'b011110111110001101110100111000101101111000001100;    //136216848817676;
    initial #20 M = 48'b101011110100111010010010001000000011001000110111;   //192751993893431;
    
    // Wait for a few simulation cycles
    initial #30 A = 48'b10100010000010110011011011111000000101000010000;    //89084525283856;
    initial #30 M = 48'b101000011111000001101110110000001101010000000010;   //178054022353922;
    
    always #1 clk = ~clk;


    // Display input values
    initial $monitor("Test Case: A = %d, M = %d, q = %d", A, M, q);

    initial #60 $finish;
    
    
endmodule