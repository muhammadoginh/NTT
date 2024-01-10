`timescale 1ns/1ps
`include "Full_Adder.v"

module Full_Adder_tb;

    // input
    reg A;
    reg B;
    reg Cin;
    
    // output
    wire Cout;
    wire Sum;

    // instantiates the unit under test
    Full_Adder uut(A, B, Cin, Cout, Sum);

    // generate stimuli
    initial begin
        $dumpfile("Full_Adder.vcd");
        $dumpvars(0, Full_Adder_tb);

        A = 1'b0;
        B = 1'b0;
        Cin = 1'b0;

        $display("Test complete!");
    end

    always #1 A = A + 1;
    always #2 B = B + 1;
    always #4 Cin = Cin + 1;

    initial $display($time, A, B, Cin, Cout, Sum);

    initial #10 $finish;
    
endmodule