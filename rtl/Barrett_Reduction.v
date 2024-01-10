`timescale 1ns/1ps

module Barrett_Reduction (
    input [31:0] a, // Assuming 32-bit inputs
    input [31:0] b,
    input [31:0] q,
    output reg [31:0] result
);

    // Pre-computation
    reg [31:0] k; // Assuming 32-bit inputs, log2(2^32) = 32
    reg [31:0] r;
    reg [31:0] mu;

    // Multiplication
    reg [63:0] z;
    
    // Barrett Reduction
    reg [63:0] m1;
    reg [63:0] m2;
    reg [31:0] m3;
    reg [63:0] t;

    // Pre-computation
    always @ (*) begin
        k = $clog2(q);
        r = 32'b1 << k;
        mu = r * r / q;
    end

    // Multiplication
    // just for proof of concept, will be change advanced multiplier
    always @ (*) begin
        z = a * b;
    end

    // Barrett Reduction
    always @ (*) begin
        m1 = z >> k;
        m2 = m1 * mu;
        m3 = m2 >> k;
        t = z - m3 * q;

        if (t >= q) begin
            result = t - q;
        end else begin
            result = t;
        end
    end

endmodule