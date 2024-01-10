`timescale 1ns/1ps
`include "Half_Adder.v"

module Half_Adder_tb;

    // input
    reg A;
    reg B;

    // output
    wire Cout;
    wire Sum;

    // instantiate the unit under test
    Half_Adder uut(A, B, Cout, Sum);

    // generate the stimuli
    initial begin
        $dumpfile("Half_Adder.vcd");
        $dumpvars(0, Half_Adder_tb);

        A = 1'b0;
        B = 1'b0;

        $display("Test complete!");
    end

    always #1 A = A + 1;
    always #2 B = B + 1;

    initial $display($time, A, B, Cout, Sum);

    initial #5 $finish;

endmodule