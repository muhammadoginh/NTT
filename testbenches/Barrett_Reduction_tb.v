`timescale 1ns/1ps
`include "Barrett_Reduction.v"

module Barrett_Reduction_tb;

    // Inputs
    reg [31:0] a;
    reg [31:0] b;
    reg [31:0] q;

    // Output
    wire [31:0] result;

    // Instantiate the Barrett_Reduction module
    Barrett_Reduction uut (
        .a(a),
        .b(b),
        .q(q),
        .result(result)
    );

    // Initial block for testbench
    initial begin
        $dumpfile("Barrett_Reduction_tb.vcd");
        $dumpvars(0, Barrett_Reduction_tb);

        // Assign test case values
        a = 4571;
        b = 4712;
        q = 7681;

        // Display input values
        $display("Test Case: a = %d, b = %d, q = %d", a, b, q);

        // Wait for a few simulation cycles
        #10;

        // Display result
        $display("Result: %d", result);

        // Finish simulation
        $finish;
    end

endmodule