`timescale 1ns/1ps
`include "Sum_Generator.v"

module Sum_Generator_tb;

    // input
    reg [127:0] p;
    reg [127:0] c;
    
    // output
    wire [127:0] Sum;

    // instantiate the unit under test
    Sum_Generator uut(.p(p), .c(c), .Sum(Sum));

    // generate moduli
    initial begin
        $dumpfile("Sum_Generator_tb.vcd");
        $dumpvars(0, Sum_Generator_tb);

        p = 0;
        c = 0;

        // Display initial values
        $display("Initial values: %0t p=%0d, c=%0d, Sum=%0d", $time, p, c, Sum);

        // Run the simulation for a certain duration
        #5;

        // Display final values
        $display("Final values: %0t p=%0d, c=%0d, Sum=%0d", $time, p, c, Sum);

        $display ("Test complete!");
    end

    always #1 p = p + 1;
    always #2 c = c + 1;

    // initial $display($time, p, c, Sum);

    initial #4 $finish;

endmodule