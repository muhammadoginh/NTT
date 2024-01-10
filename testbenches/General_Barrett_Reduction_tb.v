`timescale 1ns/1ps
`include "../rtl/General_Barrett_Reduction.v"

module General_Barrett_Reduction_tb;

    // Inputs
    reg [63:0] X;
    reg [31:0] q;

    // Output
    wire [31:0] result;

    // Instantiate the General_Barrett_Reduction module
    General_Barrett_Reduction uut (
        .X(X),
        .q(q),
        .r(result)
    );

    // Initial block for testbench
    initial begin
        $dumpfile("General_Barrett_Reduction_tb.vcd");
        $dumpvars(0, General_Barrett_Reduction_tb);

        // Assign test case values
        X = 21538552;
        q = 7681;

        // Display input values
        $display("Test Case: X = %d, q = %d", X, q);

        // Wait for a few simulation cycles
        #10;

        // Display result
        $display("Result: %d", result);

        // Finish simulation
        $finish;
    end

endmodule